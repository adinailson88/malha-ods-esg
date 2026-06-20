# Artigo — Seção 3: Materiais e Métodos (rascunho)

Rascunho da seção de métodos do artigo do eixo `malha-ods-esg`. Redigido a partir do que
está **versionado no repositório**, diferenciando o que **já existe**, o que é
**limitação** e o que é **proposta**. Não contém números do snapshot (que devem ser
revalidados e inseridos na Seção 4 — Resultados). Estilo final deve passar pela skill
`meu-estilo-textual`.

> Restrições assumidas: (i) o ranking é comparativo **dentro do snapshot**, não
> certificação oficial ODS/ESG; (ii) os pesos são **operacionais e editáveis**, com
> leitura compatível com AHP, mas **não** constituem AHP formal — não há matriz pareada
> nem razão de consistência (CR).

---

## 3.1 Contexto e unidade de análise

O estudo trata da manutenção predial de uma universidade pública federal multicampi. A
unidade de análise (alternativa de decisão) é o **campus** (incluída a Reitoria como
unidade administrativa). O recorte temporal corresponde ao snapshot de chamados
consolidado no momento da execução; por se tratar de base administrativa dinâmica, o
número de registros e de unidades é reconferido a cada sincronização e reportado na
Seção 4.

## 3.2 Fontes de dados e governança da informação

Os dados originam-se do sistema de chamados de manutenção (GLPI) do ecossistema Malha IA.
A arquitetura separa dois repositórios com papéis distintos:

- **Hub central (`malha-ia`):** mantém a base bruta de chamados e executa o recálculo
  autenticado contra o Google Sheets, publicando *snapshots* públicos.
- **Eixo ODS/ESG (`malha-ods-esg`):** consome esses snapshots e mantém apenas os dados
  **derivados** necessários ao painel, ao artigo e à auditoria. A base bruta de chamados
  **não** é duplicada aqui (contrato de fronteira de dados).

A camada patrimonial provém da planilha institucional `Patrimônio Imobiliário`
(aba `Patrimônio Imobiliário1`), lida por conta de serviço via GitHub Actions e
normalizada para padrão brasileiro de área (`10.000,00 m²`) e moeda (`R$ 10.000,00`).
Os snapshots derivados são versionados em formato aberto (JSON e CSV), o que sustenta a
reprodutibilidade e a auditoria do estudo.

*Existe:* pipeline autenticado funcional, snapshots versionados, separação hub/eixo
documentada em contrato de dados. *Limitação:* a cobertura de alguns campos depende da
qualidade do registro na fonte (ver 3.4).

## 3.3 Indicadores e mapeamento ODS/ESG

Foram definidos dez indicadores operacionais derivados dos chamados, cada um com um
**sentido de otimização** (`maximizar`, `minimizar` ou `contextual`) e uma associação a
ODS (9, 11, 12) e aos pilares ESG (Ambiental, Social, Governança). A definição completa,
a fonte e o status de cada indicador constam do
[dicionário de indicadores](DICIONARIO_INDICADORES.md) (Quadro Q1). Os indicadores são:

`N_chamados_total`, `N_infra_critica`, `Tempo_medio_resolucao_dias`,
`Taxa_resolucao_no_prazo`, `N_criticos_alta`, `N_em_espaco_coletivo`,
`Densidade_chamados_por_1000m2`, `Razao_preventiva_corretiva`, `Valor_total_gasto_R$` e
`N_chamados_repetidos`.

O mapeamento indicador→ODS e indicador→ESG é **interpretativo** (proxy institucional),
registrado em `dados/classificacao_ods_esg.json` com justificativa por indicador, e não
constitui classificação oficial dos Objetivos de Desenvolvimento Sustentável.

## 3.4 Exploração de dados e critérios de exclusão

Antes da composição dos scores, os indicadores são submetidos a um passo de exploração
de dados adaptado do protocolo de Zuur, Ieno e Elphick (2010), com foco em valores
ausentes, zeros estruturais, escalas discrepantes e ausência de variância entre unidades.
Disso resulta uma **regra de exclusão objetiva**:

1. indicador **vazio** no snapshot é tratado como **lacuna de qualidade** e não entra no
   score;
2. indicador com **variância nula ou quase nula** entre campi é excluído do score, por
   não discriminar alternativas (sua inclusão inflaria artificialmente os resultados);
3. distingue-se **zero verdadeiro** de **dado ausente**: a ausência não é tratada como
   zero, pois isso distorceria a normalização min–max e o TOPSIS;
4. todo indicador excluído permanece visível na auditoria do painel, com o motivo
   registrado.

*Existe:* artefato de diagnóstico (`scripts/gerar_protocolo_zuur.py`,
`dados/protocolo_zuur.json`) e a regra de não pontuar indicadores sem dado ou sem
variação. *Limitação:* ainda faltam matriz de correlação/VIF entre indicadores, regra
formal para zeros estruturais e diagnóstico de dependência por campus/área. *Proposta:*
incorporar correlação/VIF e teste de sensibilidade à exclusão de unidades quase-vazias.

## 3.5 Normalização

Cada indicador bruto é convertido para escala 0–1 (apresentada 0–100 no score) por
normalização **min–max dentro do snapshot**, com inversão conforme o sentido:

- maximizar: `r_ij = (x_ij - min_j) / (max_j - min_j)`
- minimizar: `r_ij = 1 - (x_ij - min_j) / (max_j - min_j)`
- contextual: `n_ij = (x_ij - min_j) / (max_j - min_j)` ; `r_ij = 1 - |n_ij - 0,5| × 2`

A transformação contextual favorece valores intermediários, adequada a indicadores que
representam exposição/uso institucional (não "quanto maior melhor").

*Limitação:* min–max é sensível a outliers e à composição do snapshot — em particular, a
presença de uma unidade quase-vazia comprime o intervalo e desloca os scores; a função
contextual embute o juízo de que o ótimo está em 0,5, o que precisa de fundamentação por
indicador. *Proposta:* reportar, como teste de robustez, o efeito de winsorização/intervalo
robusto e da exclusão da unidade quase-vazia, mantendo o min–max como método principal.

## 3.6 Ponderação dos critérios

Os pesos por critério estão em `dados/pesos_ods.json` (pesos por ODS) e
`dados/classificacao_ods_esg.json` (pesos por pilar ESG). No estado atual, são **pesos
operacionais editáveis**, atribuídos metodologicamente pelo pesquisador, com leitura
compatível com AHP.

> **Não há AHP formal.** Não foi construída matriz de comparação pareada entre critérios,
> não foi extraído autovetor de pesos e não foi calculada razão de consistência (CR).
> A elicitação AHP formal — com painel de especialistas, matriz pareada e CR — é
> registrada como trabalho futuro (Seção 7), e o termo "AHP" não é empregado como método
> aplicado neste estudo.

*Proposta:* registrar a **proveniência** de cada peso e versionar suas alterações, de modo
que mudança de peso não seja confundida com mudança real do fenômeno; e conduzir análise
de sensibilidade dos pesos (perturbação e cenário de pesos iguais como baseline).

## 3.7 Agregação e ranking

Adotam-se duas leituras complementares sobre os indicadores ativos:

**(a) Soma ponderada normalizada por ODS** — para cada campus *i* e ODS *d*:

`S_i,d = 100 × Σ_j (r_ij × w_j,d) / Σ_j (w_j,d)`

e score geral como média das três dimensões:

`Score_geral_i = (S_i,ODS9 + S_i,ODS11 + S_i,ODS12) / 3`

**(b) TOPSIS operacional** — os campi são as alternativas e os indicadores ativos são os
critérios. Usa-se peso agregado entre as três ODS:

`w_j,T = (w_j,ODS9 + w_j,ODS11 + w_j,ODS12) / Σ_j (w_j,ODS9 + w_j,ODS11 + w_j,ODS12)`

normalização vetorial e ponderação:

`v_ij = (x_ij / sqrt(Σ_i x_ij²)) × w_j,T`

e proximidade relativa à solução ideal:

`C_i = D_i⁻ / (D_i⁺ + D_i⁻) × 100`

onde `D_i⁺` e `D_i⁻` são as distâncias às soluções ideais positiva e negativa. Indicadores
`contextual` são convertidos em proximidade de equilíbrio antes do TOPSIS; indicadores em
estado de lacuna não entram no cálculo.

*Proposta de robustez:* reportar a concordância de ordenação entre a soma ponderada e o
TOPSIS (correlação de postos de Spearman/Kendall), evidenciando estabilidade do ranking.

## 3.8 Camada patrimonial como normalizador de escala

A camada patrimonial (`dados/patrimonio_imobiliario*.json`) fornece área e valor de ativos
por campus/ano, permitindo normalizar indicadores por exposição física — por exemplo,
chamados por área e custo por m² — reduzindo o viés de escala entre campi de portes
diferentes.

*Existe:* snapshots patrimoniais (por imóvel, agregado por campus/ano e mapa geográfico),
gráfico, mapa e tabela patrimoniais. *Limitação:* o indicador
`Densidade_chamados_por_1000m2` depende de área construída **por campus**, hoje pendente
em `dados/modelo_area_campus.json` (a série `area_manutencao.json` é agregada
institucional, não por campus). *Proposta:* materializar a área por campus para ativar a
densidade e a normalização por m².

## 3.9 Evolução temporal

A leitura temporal está **prevista, porém pendente**: o snapshot `indicadores_ods.json` é
um corte transversal por campus, **sem coluna de ano**. Afirmações de tendência
("melhorou/piorou") exigem a materialização de `dados/indicadores_ods_historico.json`
(campos mínimos: Ano, Campus, indicadores brutos, pesos aplicados, scores por ODS, score
geral, score ESG e ranking do ano). Até que exista série histórica validada — e com pesos
e conjunto de indicadores estáveis ou com quebras metodológicas sinalizadas — o estudo
**não** reporta evolução temporal. A camada GAM explicável é registrada como extensão
futura (painel campus-mês), não aplicada no snapshot atual por insuficiência de unidades
observacionais.

## 3.10 Reprodutibilidade e auditabilidade

Todos os artefatos — snapshots (JSON/CSV), pesos, classificação, dicionário de indicadores,
memória de cálculo e scripts — são versionados em repositório público. O painel exibe a
memória de cálculo (fórmulas, critérios, pesos por ODS, peso TOPSIS agregado, mínimos e
máximos por indicador e detalhe TOPSIS por campus), o que permite refazer o cálculo a
partir dos dados publicados. *Proposta:* fixar o estado usado no artigo por meio de
*release* versionado e identificador citável (tag/DOI), e centralizar o cálculo canônico
de scores e TOPSIS em script versionado que **gera** os JSON do painel.

---

### Notas para integração no artigo

- Mover os valores brutos, mínimos/máximos e scores para a Seção 4 (Resultados), sempre
  reconferindo o número de registros e de unidades do snapshot citado.
- Esta seção pressupõe a seção de Limitações (riscos de interpretação): ranking
  intra-snapshot, pesos não-AHP, dependência do conjunto de alternativas, cobertura de
  dados e ausência de série histórica validada.
- Referências de método a citar: Hwang & Yoon (1981, TOPSIS); Saaty (2008, AHP — como
  horizonte futuro); Klumbytė et al. (2021) e Theilig et al. (2024, MCDM em facilities);
  Zuur, Ieno & Elphick (2010, exploração de dados).
