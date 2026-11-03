# Auditoria para artigo de primeiro estrato: leia primeiro

Conjunto de documentos produzido em 03/11/2026 para auditar o repositório `malha-ods-esg` com a postura de um parecerista exigente e de um redator de artigos científicos, e para desenhar o que fazer e como fazer para que o eixo ODS/ESG origine um artigo de primeiro estrato (equivalente ao Qualis A1; o estrato vigente deve ser conferido na Plataforma Sucupira), com base no projeto de doutorado. Nada foi apagado ou alterado fora de `docs/auditoria/`, `scripts/auditoria/` e dos ponteiros de leitura (`README.md`, `CLAUDE.md`, `AGENTS.md`, `docs/CONTEXTO_CONTINUACAO.md`).

## Veredito resumido

O estado atual não é submetível a um periódico de primeiro estrato. O problema central não é de redação: faltam contribuição demonstrável, validação, poder inferencial (quatro alternativas efetivas em corte transversal) e correção de defeitos de dados e de código que invalidam os números do manuscrito. O tema, a infraestrutura de dados e a disciplina de rastreabilidade já existentes são ativos reais. O caminho para o artigo forte está desenhado, depende de poucos dados novos (datas de solução e prioridade do GLPI, usuários por campus, painel de especialistas com aprovação ética) e é viável dentro do cronograma do doutorado.

## Os onze achados que mais pesam

1. A razão preventiva do snapshot é uma contagem (925, 1.295, 1.637, 550 e 4), não uma proporção; causa não determinada.
2. A criticidade é lida na coluna de índice 30, que não existe (a coluna está no 29); `N_criticos_alta` é sempre zero, embora haja 149 chamados de criticidade alta.
3. A área por campus existe no patrimônio (`Area_Utilizacao_m2`, soma igual à área global de 2015 a 2021), mas o motor a trata como inexistente e o manuscrito afirma que não está materializada.
4. O ranking depende da escala e do método: dividir por área inverte a ordem, e soma ponderada e TOPSIS discordam (Spearman de -0,4 a 0,4).
5. Os indicadores medem demanda por proxy textual (infraestrutura crítica é por especialidade técnica, 30,6% da base; espaço coletivo é busca de palavras no título).
6. O valor é de ordens de serviço (16,5% dos chamados) e 50% a 61% dele, por campus, é contratação de "Posto de trabalho".
7. A classificação por IA tem 40,6% de baixa confiança, concentrada de 2021 em diante (50% a 80% desde 2022); o erro não é propagado.
8. A criticidade alta salta em 2026 (12 e 13 em dois campi, contra zero a quatro nos anos anteriores): mudança de critério.
9. O pré-projeto promete AHP-TOPSIS e análise de sensibilidade; o repositório não aplica AHP e não executa a sensibilidade.
10. O objeto de medida é ambíguo (desempenho ou prioridade); recomenda-se prioridade de manutenção.
11. Os números do manuscrito não são reproduzíveis com o snapshot atual e o cálculo canônico existe só em JavaScript.

## Mapa dos documentos

| Arquivo | Conteúdo |
|---|---|
| `01_PARECER_CRITICO.md` | Parecer como avaliador: recomendação, notas, objeções maiores e menores, auditoria de afirmações e condições para mudar a recomendação |
| `02_AUDITORIA_DADOS_CODIGO.md` | Auditoria da base, indicador por indicador, do código, dos dados derivados e da higiene do repositório |
| `03_DESENHO_DO_ESTUDO_A1.md` | Desenho do estudo: tese, perguntas, unidade de análise, critérios, pesos, agregação, incerteza, validação, protocolo, ética e critérios de aceite |
| `04_MATRIZ_DADOS.md` e `matriz_dados.csv` | O que já existe e o que buscar, com prioridade, fonte candidata, como obter e modelo de solicitação |
| `05_PLANO_DE_REDACAO.md` | Periódicos candidatos, títulos, resumo-esqueleto, estrutura, figuras e tabelas, guia de escrita, perguntas de revisores, declarações e checklist |
| `06_PLANO_DE_EXECUCAO.md` | Fases, portões de decisão, riscos, estrutura-alvo do repositório e dez primeiros passos |
| `../literatura/README.md` | Dossiê de literatura, temas e contexto (mapa temático, 51 referências verificadas por nível, contexto brasileiro, plano de leitura, ângulos de contribuição) |
| `07_REVISAO_DE_LITERATURA.md` | Protocolo da revisão sistemática, referências identificadas com nível de verificação e lacunas do acervo |
| `dados/auditoria_base.json` | Saída agregada da auditoria da base (reprodutível por `scripts/auditoria/auditar_base.py`) |

## Reprodução

```powershell
git clone https://github.com/adinailson88/malha-ia
git clone https://github.com/adinailson88/malha-ods-esg
cd malha-ods-esg
python scripts\auditoria\auditar_base.py ..\malha-ia\dados\chamados.json
python scripts\diagnostico\mcdm_sensibilidade.py ..\malha-ia\dados\chamados.json
```

## O que depende de você

As decisões e confirmações estão no fim de `06_PLANO_DE_EXECUCAO.md` (dez passos) e em `04_MATRIZ_DADOS.md`. Três respostas destravam o resto: o valor real da razão preventiva e a posição da coluna de criticidade na planilha; a equivalência entre `Area_Utilizacao_m2` e área construída; e a situação da orientação e da coautoria, que não foram presumidas.

## Limites desta auditoria

1. A planilha viva, o Apps Script e o GLPI não foram acessados (hosts externos bloqueados na sessão em nuvem); as conclusões vêm dos arquivos versionados e do `chamados.json` do hub.
2. A literatura foi buscada de forma não sistemática; vários DOIs constam como "DOI não encontrado" e o estrato Qualis dos periódicos não foi verificado.
3. Os cenários de sensibilidade replicam o painel em Python e não foram comparados com a execução do navegador.
4. Metas dos ODS, normas da ABNT e referências de métodos (por exemplo, valores usuais de validade de conteúdo) são citadas em paráfrase e precisam de conferência na fonte oficial.
5. Nenhuma solicitação de dados foi enviada a ninguém e nenhum processo ético foi iniciado.
