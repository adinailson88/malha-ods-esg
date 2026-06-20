# Estrutura preditiva ODS/ESG para o painel de decisao

Este documento organiza a camada futura do painel ODS/ESG, alinhada ao projeto de tese `Modelo Preditivo de Governanca Sustentavel na Manutencao Predial de Universidades Publicas sob a Perspectiva dos Biossistemas Construidos`.

## 1. Ideia central

O painel ODS/ESG nao deve mostrar apenas o que ja ocorreu. Ele deve evoluir para mostrar o que pode ocorrer no biossistema construido universitario quando se combinam:

1. custo executado;
2. custo previsto por IA;
3. quantidade observada de chamados;
4. quantidade prevista de chamados;
5. area por campus;
6. previsao de chuva;
7. previsao de calor;
8. decisoes governamentais ou institucionais, como contingenciamento, liberacao orcamentaria, prioridade normativa ou renovacao contratual.

A leitura correta e prospectiva: as previsoes nao certificam impacto ODS/ESG, mas alteram cenarios de risco, prioridade e ranqueamento no TOPSIS/AHP.

## 2. Como isso entra no painel

| Camada | Papel no painel | Efeito esperado |
|---|---|---|
| Custo executado | Mostra pressao orcamentaria ja materializada | Afeta ODS 12 e Governanca |
| Custo previsto por IA | Projeta gasto futuro por campus/categoria | Antecipa risco de estouro, priorizacao e contratacao |
| Chamados observados | Mede pressao operacional atual | Afeta ODS 9, ODS 11 e Governanca |
| Chamados previstos por IA | Projeta pico de demanda | Antecipa piora ou melhora futura do score |
| Area por campus | Normaliza escala fisica das unidades | Permite custo por m2, chamados por 1000 m2 e comparacao justa entre campi |
| Chuva prevista | Condicionante ambiental | Aumenta risco de infiltracao, drenagem, hidrossanitaria, area externa |
| Calor previsto | Condicionante ambiental | Aumenta risco de climatizacao, eletrica, conforto termico e espacos coletivos |
| Decisao governamental | Condicionante de governanca | Altera pesos de custo, contrato, prazo, obrigacao normativa e ODS 12 |

## 2.1 Area por campus

No estado atual, o repositorio possui apenas a serie institucional agregada `dados/area_manutencao.json`, com area construida e area total por ano. Essa serie ajuda a contextualizar a expansao fisica da instituicao, mas ainda nao permite calcular densidade por campus.

Para corrigir essa lacuna, foi criado o contrato `dados/modelo_area_campus.json`, com uma linha por campus e campos para area construida, area total, ano de referencia, fonte e status. Enquanto esses valores nao forem preenchidos por fonte verificavel, indicadores como `Densidade_chamados_por_1000m2`, `Custo_executado_por_m2`, `Custo_previsto_por_m2` e `Chamados_previstos_por_1000m2` devem permanecer como pendentes.

## 3. Categorias e pesos ODS/ESG

O arquivo `dados/pesos_categorias_ods_esg.json` define familias de chamados e sua associacao metodologica com ODS 9, ODS 11, ODS 12 e pilares ESG.

Essas familias nao substituem a classificacao automatica do eixo `classificacao-chamados`; elas formam uma camada interpretativa para que a previsao de custo e demanda tenha efeito no painel ODS/ESG.

A pontuacao por chamado usa tambem `dados/regras_peso_chamado_ods_esg.json` e `dados/multiplicadores_importancia_chamado.json`, cruzando categoria, importancia, titulo, descricao GLPI, titulo OSM, descricao OSM, solucao e custo. A regra completa esta em `docs/REGRA_PESO_CHAMADO_ODS_ESG.md`.

Exemplo:

1. se a IA prever aumento de chamados de `Climatizacao_Ar_Condicionado` em periodo de calor, o painel pode elevar o risco associado a conforto termico, consumo energetico e continuidade de uso dos espacos;
2. se houver previsao de chuva intensa e historico de `Estrutura_Telhado_Infiltracao_Calhas`, o painel pode elevar risco social e ambiental por salubridade, protecao da edificacao e area externa;
3. se houver restricao orcamentaria e custo previsto alto em categorias corretivas, o TOPSIS pode reordenar prioridades pela combinacao entre risco, custo e governanca.

## 4. Relacao com AHP/TOPSIS

O AHP define pesos dos criterios. No estado atual, os pesos sao operacionais e documentados, mas ainda nao derivam de matriz pareada formal de especialistas.

O TOPSIS ranqueia as alternativas. No painel atual, as alternativas sao campi. Na evolucao preditiva, as alternativas podem ser:

1. campus;
2. campus-categoria;
3. campus-periodo;
4. pacote de intervencao;
5. cenario orcamentario.

## 5. Estrutura de cenario recomendada

Cada cenario futuro deve ter:

| Campo | Exemplo |
|---|---|
| `cenario_id` | `chuva_alta_custo_restrito_2026_07` |
| `periodo` | `2026-07` |
| `campus` | `Campus Jorge Amado` |
| `area_construida_m2` | area por campus, quando houver fonte verificavel |
| `area_total_m2` | area territorial por campus, quando houver fonte verificavel |
| `familia_categoria` | `Estrutura_Telhado_Infiltracao_Calhas` |
| `chamados_previstos` | valor do modelo de demanda |
| `custo_previsto` | valor do modelo de custo |
| `chuva_prevista_mm` | valor meteorologico |
| `temperatura_maxima_prevista` | valor meteorologico |
| `decisao_governamental` | `restricao_orcamentaria`, `liberacao_orcamentaria`, `prioridade_normativa` |
| `peso_ODS9` | herdado da familia de categoria |
| `peso_ODS11` | herdado da familia de categoria |
| `peso_ODS12` | herdado da familia de categoria |
| `peso_E` | herdado da familia de categoria |
| `peso_S` | herdado da familia de categoria |
| `peso_G` | herdado da familia de categoria |

## 6. Cuidados metodologicos

1. Nao tratar previsao climatica como causa unica de chamados.
2. Nao afirmar impacto ODS real sem indicador observado.
3. Nao misturar custo executado com custo previsto sem rotulo claro.
4. Nao usar decisao governamental como dado tecnico; ela e cenario de governanca.
5. Validar os modelos preditivos por MAE, RMSE, MAPE, R2 ou validacao temporal antes de usar como resultado cientifico.
6. Preservar a frase `Informacao insuficiente para verificar.` quando a categoria nao tiver evidencia textual suficiente.

## 7. Proximo passo tecnico

Criar um arquivo futuro `dados/cenarios_preditivos_ods_esg.json` com linhas por campus-periodo-categoria, alimentado pelos repositorios de previsao de chamados, previsao de custos e por fonte climatica rastreavel. Esse arquivo deve ser consumido pelo dashboard como aba separada: `Cenarios futuros`.
