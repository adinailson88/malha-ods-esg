# Modelo recomendado de planilha ODS/ESG

Este documento descreve a forma recomendada para organizar a planilha que alimenta o eixo ODS/ESG.

## 1. Abas recomendadas

| Aba | Funcao |
|---|---|
| `INDICADORES_ODS` | Indicadores brutos por campus, derivados da base de chamados |
| `PESOS_ODS` | Pesos para ODS 9, ODS 11 e ODS 12 |
| `CLASSIFICACAO_ODS_ESG` | Contrato metodologico de associacao indicador -> ODS/ESG |
| `QUALIDADE_INDICADORES_ODS` | Diagnostico de completude, variacao e uso no score |
| `AREA_MANUTENCAO` | Area construida/total por campus e ano, quando disponivel |
| `AREA_CAMPUS` | Area construida e area total por campus, fonte para densidade e custo por m2 |
| `PATRIMONIO_IMOBILIARIO` | Itens patrimoniais por ano, campus, cidade e coordenada |
| `PATRIMONIO_IMOBILIARIO_CAMPUS_ANO` | Agregacao anual por campus: areas, valores e localizacao media |
| `PATRIMONIO_IMOBILIARIO_MAPA` | Pontos geograficos do ano mais recente para leitura espacial |

## 2. Regra de ouro

A planilha deve separar indicador bruto, peso metodologico e diagnostico de qualidade. Um campo vazio, zerado por ausencia de dado ou sem variacao entre campi nao deve entrar no score como se fosse informacao substantiva.

## 3. Colunas minimas de `INDICADORES_ODS`

| Coluna | Tipo | Sentido | Observacao |
|---|---|---|---|
| `Campus` | texto | chave | unidade institucional |
| `N_chamados_total` | numero | minimizar | pressao operacional; usar com cautela porque campus maior tende a ter mais chamados |
| `N_infra_critica` | numero | minimizar | proxy de risco tecnico de infraestrutura |
| `Tempo_medio_resolucao_dias` | numero | minimizar | depende de data de abertura e conclusao |
| `Taxa_resolucao_no_prazo` | proporcao | maximizar | depende de SLA e data de conclusao |
| `N_criticos_alta` | numero | minimizar | depende de criticidade confiavel |
| `N_em_espaco_coletivo` | numero | contextual | representa exposicao social dos espacos |
| `Densidade_chamados_por_1000m2` | numero | minimizar | exige area por campus |
| `Razao_preventiva_corretiva` | numero | maximizar | exige classificacao preventiva/corretiva consistente |
| `Valor_total_gasto_R$` | moeda | minimizar | gasto registrado, nao necessariamente custo total real |
| `N_chamados_repetidos` | numero | minimizar | exige chave de local/ativo/recorrencia |

## 4. Colunas recomendadas de `QUALIDADE_INDICADORES_ODS`

| Coluna | Significado |
|---|---|
| `Indicador` | Nome do indicador bruto |
| `Status` | `ativo`, `sem_variacao`, `sem_dados`, `parcial` |
| `Usar_no_score` | `SIM` ou `NAO` |
| `N_valores` | Quantidade de valores numericos |
| `N_ausentes` | Quantidade de ausencias |
| `N_zeros` | Quantidade de zeros |
| `Min` | Valor minimo |
| `Max` | Valor maximo |
| `Observacao` | Cuidado metodologico |

## 5. Campos que precisam melhorar na origem

1. Data de conclusao real para calcular tempo medio de resolucao.
2. Regra de SLA por criticidade para taxa de resolucao no prazo.
3. Area por campus e por ano, nao apenas area institucional agregada.
4. Chave de local, ativo ou ambiente para recorrencia.
5. Criticidade padronizada e validada.
6. Classificacao preventiva/corretiva confiavel.

## 5.1 Modelo minimo de area por campus

Enquanto nao houver area por predio, ambiente ou ativo, a unidade minima recomendada e campus.

| Campo | Uso |
|---|---|
| `Campus` | chave para cruzar com `INDICADORES_ODS` |
| `Area_Construida_m2` | denominador preferencial para densidade de chamados e custo por m2 |
| `Area_Total_m2` | contexto territorial e ambiental |
| `Ano_Referencia` | ano da medicao |
| `Fonte` | documento, planilha, relatorio ou base institucional |
| `Status` | `verificado`, `estimado`, `pendente` |
| `Observacao` | limite de interpretacao |

## 5.2 Fonte patrimonial oficial

A fonte recomendada para area, valor patrimonial e localizacao e a planilha Google `Patrimônio Imobiliário`, aba `Patrimônio Imobiliário1`.

Colunas usadas:

| Coluna na origem | Campo derivado | Uso no painel |
|---|---|---|
| `Item` | `Ano` | serie anual patrimonial |
| `Cód.` | `Codigo` | identificador do item patrimonial |
| `Descrição` | `Descricao` | nome do campus, terreno, unidade ou CUNI |
| `Endereço` | `Endereco` | contexto urbano |
| `Cidade` | `Cidade` | rotulo territorial no mapa |
| `Área (m²) - Terreno` | `Area_Terreno_m2` | area territorial |
| `Área (m²) - Utilização` | `Area_Utilizacao_m2` | denominador preferencial para chamados e custos por m2 |
| `Valores (R$) - Terreno` | `Valor_Terreno_R$` | valor patrimonial do terreno |
| `Valores (R$) - Utilização` | `Valor_Benfeitoria_R$` | valor de benfeitorias/utilizacao |
| `Valor Final (Imóvel R$)` | `Valor_Final_R$` | valor patrimonial consolidado |
| `Latitude x Longitude` | `Latitude`, `Longitude` | mapa patrimonial |
| `Campus` | `Campus` | chave de agregacao ODS/ESG |

Os dados devem ser preservados por ano. O painel pode exibir o ano mais recente no mapa e usar a serie `Campus x Ano` para avaliar mudanca de area, valor patrimonial exposto e densidade de chamados ao longo do tempo.

## 6. Uso no artigo

No artigo, a planilha deve ser descrita como um contrato de dados. O resultado cientifico nao e a planilha em si, mas a trilha auditavel entre dado operacional, indicador, peso e decisao.
