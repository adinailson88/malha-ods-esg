# Metodologia MCDM para o eixo ODS/ESG

Este documento registra a organizacao metodologica do painel ODS/ESG do repositorio `malha-ods-esg`.

## 1. Papel do painel

O painel nao certifica desempenho oficial ODS ou ESG. Ele organiza dados operacionais de manutencao predial em uma matriz multicriterio auditavel, permitindo comparar campi ou unidades institucionais a partir de indicadores derivados do ecossistema Malha IA.

A cadeia metodologica recomendada e:

`chamado -> indicador operacional -> dimensao ODS/ESG -> normalizacao -> peso multicriterio -> score comparativo -> decisao gerencial`

## 2. Referencias metodologicas de apoio

1. `An MCDM Model for Sustainable Decision-Making in Municipal Residential Buildings Facilities Management`, Sustainability, v. 13, n. 5, art. 2820, DOI: `10.3390/su13052820`.
   - Uso no projeto: reforca o uso de MCDM para gestao sustentavel de facilities em edificios publicos ou residenciais municipais.
2. `Life cycle assessment and multi-criteria decision-making for sustainable building parts`, International Journal of Life Cycle Assessment, 2024, DOI: `10.1007/s11367-024-02331-9`.
   - Uso no projeto: apoia a integracao entre criterios ambientais, sociais/economicos e decisao multicriterio no ambiente construido.
3. Zuur, Ieno & Elphick (2010), DOI: `10.1111/j.2041-210X.2009.00001.x`.
   - Uso no projeto: protocolo de exploracao de dados antes de compor scores, evitando superinterpretar indicadores ausentes, zerados ou colineares.

## 3. Forma atual do metodo

O metodo atual tem duas leituras complementares:

1. soma ponderada normalizada por ODS, usada para explicar ODS 9, ODS 11 e ODS 12 separadamente;
2. painel de decisao TOPSIS/AHP, usado para ranquear os campi como alternativas de decisao.

Na leitura ODS, cada indicador bruto e convertido para escala 0-100 por normalizacao min-max dentro do snapshot carregado.

1. Indicadores com sentido `minimizar`: menor valor recebe melhor score.
2. Indicadores com sentido `maximizar`: maior valor recebe melhor score.
3. Indicadores com sentido `contextual`: valores intermediarios sao favorecidos, pois o indicador representa exposicao/uso institucional e nao "quanto maior melhor".

O dashboard deve ignorar, no score composto, indicadores sem dados suficientes ou sem variacao no snapshot. Esses indicadores continuam aparecendo na auditoria, mas nao devem distorcer rankings.

## 4. Painel de decisao TOPSIS/AHP

O painel de decisao usa a combinacao AHP + TOPSIS em forma operacional:

1. `AHP`: os pesos atuais em `dados/pesos_ods.json` funcionam como pesos de criterios. Nesta etapa, eles sao pesos metodologicos editaveis, ainda nao derivados de matriz pareada formal de especialistas.
2. `TOPSIS`: os campi sao as alternativas. Os indicadores ativos sao os criterios. O ranking e calculado pela proximidade de cada campus em relacao a uma solucao ideal positiva e a uma solucao ideal negativa.

A interpretacao correta e:

- maior proximidade TOPSIS indica melhor posicao relativa no conjunto de criterios ativos;
- o resultado e comparativo dentro do snapshot, nao absoluto;
- indicadores sem dados ou sem variacao nao entram no calculo;
- indicadores `minimizar` favorecem menor valor;
- indicadores `maximizar` favorecem maior valor;
- indicadores `contextual` sao transformados em proximidade de equilibrio antes do TOPSIS.

Para uma versao AHP formal, a proxima etapa e criar uma matriz pareada por especialistas ou pelo pesquisador, calcular autovetor de pesos e registrar razao de consistencia. Ate isso ocorrer, nao declarar que houve elicitação AHP formal.

## 5. Indicadores atuais e cautelas

No snapshot atual, parte dos indicadores ainda e incompleta:

1. `Tempo_medio_resolucao_dias`: depende de data de conclusao padronizada.
2. `Taxa_resolucao_no_prazo`: depende de data de conclusao e regra de SLA.
3. `N_criticos_alta`: depende de criticidade confiavel.
4. `Densidade_chamados_por_1000m2`: depende de area por campus.
5. `N_chamados_repetidos`: depende de local, ativo ou chave de recorrencia.

Quando esses campos estiverem vazios ou sem variacao, o painel deve exibi-los como lacuna de qualidade, nao como resultado negativo ou positivo.

## 6. Estrutura ODS recomendada

| ODS | Leitura operacional | Indicadores mais aderentes |
|---|---|---|
| ODS 9 | Infraestrutura resiliente, confiabilidade tecnica e sistemas criticos | `N_infra_critica`, `Tempo_medio_resolucao_dias`, `Taxa_resolucao_no_prazo`, `Densidade_chamados_por_1000m2` |
| ODS 11 | Qualidade, seguranca e continuidade de uso dos espacos universitarios | `N_em_espaco_coletivo`, `N_criticos_alta`, `Tempo_medio_resolucao_dias`, `N_chamados_total` |
| ODS 12 | Uso responsavel de recursos, desperdicio, recorrencia e custo | `Razao_preventiva_corretiva`, `Valor_total_gasto_R$`, `N_chamados_repetidos`, `Densidade_chamados_por_1000m2` |

## 7. Estrutura ESG recomendada

| Pilar | Leitura operacional |
|---|---|
| Ambiental | agua, energia, climatizacao, desperdicio, densidade de demanda por area, recorrencia e manutencao preventiva |
| Social | seguranca, salubridade, acessibilidade, continuidade de uso, espacos coletivos e conforto da comunidade academica |
| Governanca | prazo, resolutividade, controle orcamentario, criticidade, rastreabilidade e gestao preventiva |

## 8. Proxima evolucao

O melhor desenho futuro e materializar uma tabela `INDICADORES_ODS_ESG` com uma linha por campus e periodo, preferencialmente campus-mes. Isso permitiria:

1. diagnostico temporal;
2. reducao de instabilidade dos scores;
3. avaliacao de tendencia;
4. uso futuro de modelos GAM ou outros modelos explicaveis;
5. validacao estatistica mais robusta.
6. AHP formal com matriz pareada e razao de consistencia.
