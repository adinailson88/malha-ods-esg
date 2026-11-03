# Contexto de continuação para o Claude executado no PC do autor (eixo ODS/ESG)

Documento de passagem de trabalho de 03/11/2026, escrito ao fim de uma sessão em nuvem cujo saldo de créditos expira em 05/11/2026. O autor continuará com o Claude no próprio computador. Leia, nesta ordem: `AGENTS.md`, este arquivo, `docs/PLANO_ARTIGO_ODS_ESG.md`, `docs/CONTEXTO_PREPROJETO.md` e `docs/CONTINUIDADE_ARTIGO_ODS_ESG.md`; o manuscrito é `docs/ARTIGO_MALHA_ODS_ESG.md`. Quando um dado não puder ser verificado, declare: `Informação insuficiente para verificar.`

## 1. Objetivo

Preparar o terceiro trabalho do ecossistema Malha IA: o artigo e o instrumento de apoio multicritério ODS/ESG (ODS 9, 11 e 12) para manutenção predial na UFSB, alinhado ao pré-projeto de doutorado (objetivo específico 5 e atividade 7). O pré-projeto está no Drive do autor (documento "2026_PROPOSTA_Biossistemas_Projeto_Doutorado_Governanca_Manutencao", identificador `1SHP8pOe5bu506sT1O24EJrJLnkLT-lGWbumCbCqti-0`); o resumo está em `docs/CONTEXTO_PREPROJETO.md`. Não copie para repositórios públicos dados pessoais presentes em documentos do Drive.

## 2. Repositórios do ecossistema

1. `adinailson88/malha-ia`: hub; fonte da base `CHAMADOS` e dos motores que escrevem na planilha (`motor_ods.py` é executado lá pelo workflow `4 - Indicadores ODS`, diário). Correção de datas dos motores já mergeada (PR malha-ia#6).
2. `adinailson88/malha-ods-esg` (este): painel, snapshots, patrimônio e artigo do eixo ODS/ESG.
3. `adinailson88/malha-previsao-chamados`: Artigo 2 (quantidade de chamados); possui `CLAUDE.md` e `docs/CONTEXTO_CONTINUACAO.md` próprios.
4. `adinailson88/malha-previsao-custos`: Artigo 3 (custos).
5. `adinailson88/classificacao-chamados`: artigo de classificação (RAP).

## 3. Achados críticos (verificados em 03/11/2026; detalhes no plano, seção 3)

1. O snapshot `dados/indicadores_ods.json` traz `Razao_preventiva_corretiva` como contagem de preventivos (925, 1.295, 1.637, 550 e 4), não como razão; o motor atual calcularia 0,234, 0,330, 0,386, 0,224 e 0,364. Causa não determinada; teste: conferir a coluna na aba `INDICADORES_ODS` da planilha.
2. `COL_CRITICIDADE_OUT = 30` ("AD") em `motor_ods.py`; no `chamados.json` a criticidade está no índice 29, e o índice 30 não existe, o que explica `N_criticos_alta` sempre zero (há 149 chamados "Alta"). Conferir a posição da coluna na planilha viva antes de corrigir.
3. Ranking de campi instável entre soma ponderada e TOPSIS (Spearman de -0,4 a 0,4) e dependente da escala: dividir por área inverte o ranking. Perturbar os pesos quase não altera a primeira posição dentro de cada método. Reprodução: `python scripts/diagnostico/mcdm_sensibilidade.py ../malha-ia/dados/chamados.json`.
4. `Valor_total_gasto_R$` é 50% a 61% "Posto de trabalho > Contratação" em cada campus.
5. Área por campus existe em `dados/patrimonio_imobiliario_campus_ano.json` (`Area_Utilizacao_m2`, 2015 a 2025) e a soma bate com a área construída global de `area_manutencao.json` (0,0% de diferença de 2015 a 2021). Ainda não é usada pelos indicadores. Vale também para os Artigos 2 e 3, que dependem de área por campus.
6. O pré-projeto promete AHP-TOPSIS; o repositório declara "não AHP formal". Decisão do autor pendente.

## 4. Decisões já tomadas pelo autor (valem para o ecossistema)

1. Dados editáveis ficam na planilha CHAMADOS (https://docs.google.com/spreadsheets/d/1VgHY6NmCQLtA3lcfQAzGIRqJFZGHwcGhZ4zaXkqOmz4/edit); o repositório lê a planilha e o autor não quer editar o GitHub manualmente.
2. Quando faltar área ou número de pessoas, projetar o ano seguinte como último valor mais 5% ao ano, marcando a origem; dados simulados devem ser rotulados `SIMULADO` e nunca entrar em resultado de artigo.
3. Convenções fixas deste eixo (não reabrir): ranking é comparativo intra-snapshot e não certificação ODS/ESG; pesos operacionais editáveis; cada republicação do artigo no Drive é um novo documento numerado (a próxima é `artigo_2`).
4. Estilo de texto: português, prosa técnica impessoal, sem travessão, sem frases curtas de remate, tabelas somente onde comparam.

## 5. Restrições permanentes

1. Alterações em `motor_ods.py` precisam ser replicadas no hub, que é quem executa; não alterar workflows nem secrets do hub sem pedido explícito do autor.
2. Não fazer push direto na `main`; trabalhar em branch e abrir PR quando o autor pedir (a nota antiga em `docs/CONTINUIDADE_ARTIGO_ODS_ESG.md` sobre push direto na `main` foi superada por esta regra).
3. Não duplicar `dados/chamados.json`; a base bruta pertence ao hub.
4. Citar somente referências verificáveis; os itens "DOI não encontrado" do plano precisam de conferência no editor.

## 6. Pendências em ordem de prioridade

1. Conferir na planilha (aba `INDICADORES_ODS`) a razão preventiva e a coluna de criticidade; localizar a causa do snapshot com contagem; corrigir no hub e neste repositório; regenerar snapshots; recalcular os Resultados do manuscrito.
2. Usar a área por campus do patrimônio nos indicadores (densidade por 1.000 m2 e contagens e gasto normalizados), projetar 2026 com +5% e atualizar `dados/modelo_area_campus.json`.
3. Decidir o tratamento de "Posto de trabalho" no critério de gasto.
4. Implementar a sensibilidade completa (pesos, normalização, método, unidades) a partir de `scripts/diagnostico/mcdm_sensibilidade.py`, com Spearman e Kendall e probabilidade de primeira posição; adicionar um terceiro método (VIKOR ou PROMETHEE II).
5. Decidir sobre AHP formal (elicitação com especialistas; verificar a necessidade de aprovação em comitê de ética) ou reescrever método e projeto como TOPSIS com pesos operacionais.
6. Materializar `INDICADORES_ODS_ESG` por campus e período para tendência e integração das previsões dos Artigos 2 e 3.
7. Itens herdados da nota de continuidade: referencial teórico (seção 2 do manuscrito) em prosa, apagar documentos obsoletos no Drive, executar sensibilidade e correlação de postos.
8. Perguntas abertas ao autor: status da relação com o orientador e coautoria (não presumidos); periódico-alvo e Qualis vigente (Plataforma Sucupira); `Area_Utilizacao_m2` equivale a área construída? CJA, CPF e CSC correspondem a Jorge Amado, Paulo Freire e Sosígenes Costa?

## 7. Como executar no Windows (PowerShell)

Os scripts de diagnóstico usam apenas Python (3.11 ou 3.12) e numpy.

```powershell
git clone https://github.com/adinailson88/malha-ods-esg
git clone https://github.com/adinailson88/malha-ia
cd malha-ods-esg
python -m pip install numpy
python scripts\diagnostico\mcdm_sensibilidade.py ..\malha-ia\dados\chamados.json
python scripts\baixar_dados_hub.py
```

Na máquina do autor, os hosts bloqueados na sessão em nuvem (Apps Script, Google Sheets, Open-Meteo, INMET) provavelmente estão acessíveis.

## 8. Auditoria para artigo de primeiro estrato (rodada posterior)

Em 03/11/2026 foi feita auditoria completa do repositório em `docs/auditoria/` (comece por `00_LEIA-ME.md`): parecer crítico (`01`), auditoria de dados e código (`02`), desenho do estudo (`03`), matriz de dados com o que buscar (`04` e `matriz_dados.csv`), plano de redação e submissão (`05`), plano de execução com portões e riscos (`06`) e protocolo de revisão de literatura (`07`). Scripts novos: `scripts/auditoria/auditar_base.py`. Achados adicionais além dos da seção 3: 40,6% dos chamados com classificação de baixa confiança (concentrada de 2021 em diante), salto de criticidade alta em 2026, `N_infra_critica` por especialidade técnica (30,6% da base), ambiguidade entre desempenho e prioridade, e a lógica de pontuação existente apenas em JavaScript. Recomendação: objeto de medida igual a índice de prioridade de manutenção, alternativas campus e sistema, painel campus, sistema e ano, pesos elicitados e incerteza por SMAA.

Dossiê de literatura (rodada posterior, 03/11/2026): `docs/literatura/` reúne o mapa temático (dez frentes), 51 referências com nível de verificação V1 a V3 (`02_REFERENCIAS_VERIFICADAS.md` e `referencias.csv`), o contexto normativo brasileiro, o plano de leitura e cinco conceitos de artigo com a recomendação de um artigo principal que combine robustez da priorização sob incerteza e validade preditiva. Nenhum texto integral foi lido; conferir DOIs no editor antes de citar.

## 9. Mapa dos arquivos criados nesta rodada

1. `docs/PLANO_ARTIGO_ODS_ESG.md`: diagnóstico, alinhamento ao pré-projeto, melhorias, literatura preliminar e pendências.
2. `docs/CONTEXTO_PREPROJETO.md`: resumo do pré-projeto.
3. `docs/CONTEXTO_CONTINUACAO.md`: este arquivo.
4. `scripts/diagnostico/mcdm_sensibilidade.py`: reprodução em Python de soma ponderada e TOPSIS, sensibilidade e cenários S0 a S3.
5. `CLAUDE.md`: ponteiro de leitura para o Claude Code.
6. `docs/auditoria/` e `scripts/auditoria/`: auditoria completa e reprodutível (ver seção 8).
