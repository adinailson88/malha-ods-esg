# Guia de leitura do dashboard ODS/ESG

Este documento explica a funcao de cada bloco do painel `Malha ODS ESG`, quais tabelas alimentam cada visualizacao e como interpretar os resultados sem confundir indicador bruto, peso metodologico e score composto.

## 1. Objetivo do painel

O dashboard ODS/ESG organiza indicadores de manutencao predial universitaria em uma leitura multicriterio associada a ODS 9, ODS 11, ODS 12 e aos pilares ESG Ambiental, Social e Governanca.

O repositorio `malha-ods-esg` nao substitui o hub central `malha-ia`. Ele consome snapshots derivados do hub para permitir um painel especifico, reprodutivel e adequado ao artigo do eixo ODS/ESG.

## 2. Fontes e arquivos usados

| Arquivo | Origem logica | Uso no dashboard |
|---|---|---|
| `dados/indicadores_ods.json` | Aba `INDICADORES_ODS` | Indicadores brutos por campus |
| `dados/pesos_ods.json` | Aba `PESOS_ODS` | Pesos multicriterio para ODS 9, ODS 11 e ODS 12 |
| `dados/classificacao_ods_esg.json` | Configuracao metodologica local | Associacao de cada indicador a ODS e ESG |
| `dados/metadados_indicadores.json` | Contrato local de qualidade | Limites, status esperado e melhorias da fonte por indicador |
| `dados/area_manutencao.json` | Aba `Area Manutencao` | Contexto institucional de area construida e area total |
| `dados_csv/*.csv` | Exportacao local dos JSONs | Apoio a conferencia, artigo e leitura tabular |

## 3. Cards superiores

`Campi avaliados` mostra a quantidade de linhas validas em `dados/indicadores_ods.json`. Cada linha representa um campus ou unidade institucional presente no snapshot ODS.

`Chamados considerados` soma a coluna `N_chamados_total`. Esse numero indica a escala operacional usada para compor os indicadores.

`Gasto registrado` soma a coluna `Valor_total_gasto_R$`. O valor e exibido em reais, com simbolo `R$` e centavos, porque se trata de indicador monetario bruto.

`Melhor score geral` apresenta o maior score composto calculado no navegador a partir de ODS 9, ODS 11 e ODS 12. Esse valor nao e um dado bruto da planilha; e uma sintese normalizada.

## 4. Ranking geral ODS/ESG por campus

Este grafico responde: qual campus apresenta o melhor desempenho multicriterio geral considerando os indicadores e pesos ativos?

O score geral e calculado a partir da media dos scores ODS 9, ODS 11 e ODS 12. Cada indicador bruto e normalizado entre o menor e o maior valor observados no snapshot. Indicadores com sentido `minimizar` favorecem valores menores; indicadores com sentido `maximizar` favorecem valores maiores; indicadores `contextual` sao tratados como equilibrio relativo.

## 5. Comparacao ODS 9, ODS 11 e ODS 12

Este grafico responde: o desempenho de cada campus se concentra em infraestrutura, cidades sustentaveis ou consumo responsavel?

`ODS 9 - Infraestrutura` concentra indicadores de pressao operacional, infraestrutura critica e capacidade de resposta tecnica.

`ODS 11 - Cidades sustentaveis` concentra efeitos sobre uso dos espacos, criticidade, ambientes coletivos e continuidade de funcionamento institucional.

`ODS 12 - Consumo responsavel` concentra eficiencia no uso de recursos, prevencao, recorrencia e gasto.

## 6. Painel de decisao TOPSIS/AHP

Este bloco responde: qual campus esta mais proximo da alternativa ideal considerando simultaneamente os criterios ativos?

O painel usa TOPSIS para ranquear os campi. Os pesos carregados em `dados/pesos_ods.json` funcionam como pesos AHP operacionais, mas ainda nao representam uma matriz pareada formal de especialistas.

O resultado deve ser lido como apoio a decisao multicriterio, nao como certificacao ODS/ESG. Se a planilha estiver incompleta, o proprio bloco de qualidade dos indicadores limita o conjunto de criterios usados no TOPSIS.

## 7. Ranking ESG por campus

Este grafico responde: qual campus tem melhor leitura agregada nos pilares Ambiental, Social e Governanca?

O score ESG usa `dados/classificacao_ods_esg.json`, nao `dados/pesos_ods.json`. A classificacao ESG e uma camada de leitura academica: ela permite interpretar os mesmos indicadores sob os pilares E, S e G.

## 8. Composicao ESG do melhor campus

O grafico radar mostra a distribuicao do melhor campus no ranking ESG entre:

| Pilar | Leitura |
|---|---|
| Ambiental | Uso eficiente do ativo fisico, prevencao, reducao de desperdicios e relacao demanda/area |
| Social | Impacto no uso coletivo dos espacos, seguranca, bem-estar e continuidade das atividades |
| Governanca | Controle, prazo, resolutividade, criticidade operacional e gestao orcamentaria |

Uma composicao equilibrada indica desempenho distribuido entre os tres pilares. Uma composicao concentrada indica que o campus se destaca mais em um pilar do que nos demais.

## 9. Tabela de scores compostos

Esta tabela apresenta, por campus:

| Coluna | Significado |
|---|---|
| `Campus` | Unidade analisada |
| `ODS 9` | Score normalizado para infraestrutura |
| `ODS 11` | Score normalizado para cidades sustentaveis e uso institucional dos espacos |
| `ODS 12` | Score normalizado para consumo responsavel e eficiencia |
| `Score ODS geral` | Media dos tres scores ODS |

Os selos coloridos indicam faixas de leitura: verde para scores maiores ou iguais a 75, amarelo para 50 a 74,9 e vermelho para abaixo de 50.

## 10. Classificacao dos indicadores por ODS e ESG

Esta tabela explica a configuracao metodologica usada no painel. Ela deve ser usada como apoio de escrita do artigo, porque explicita como cada indicador e interpretado.

| Campo | Significado |
|---|---|
| `Indicador` | Nome do indicador bruto presente em `dados/indicadores_ods.json` |
| `Classe principal` | Pilar ESG predominante do indicador |
| `ODS 9`, `ODS 11`, `ODS 12` | Intensidade de associacao com cada ODS |
| `E`, `S`, `G` | Peso interpretativo nos pilares ESG Ambiental, Social e Governanca |
| `Justificativa` | Racional tecnico para a classificacao |

Esta configuracao nao altera a planilha operacional. Ela e um contrato metodologico local para leitura, painel e artigo.

## 11. Pesos multicriterio

A tabela `Pesos multicriterio` permite testar cenarios diretamente no navegador. Os botoes executam apenas calculos locais:

| Acao | Efeito |
|---|---|
| `Aplicar pesos` | Recalcula os scores com os valores digitados |
| `Resetar pesos do JSON` | Restaura os pesos carregados de `dados/pesos_ods.json` |
| `Normalizar por ODS` | Ajusta os pesos para que cada coluna ODS some 1 |

Essas alteracoes nao escrevem no Google Sheets, nao geram commit e nao modificam os arquivos JSON. Para alterar a fonte, e necessario atualizar `PESOS_ODS` pelo fluxo autenticado do motor.

## 12. Area institucional

O grafico `Area institucional` mostra a evolucao de area construida e area total. Ele nao entra diretamente no score geral, mas contextualiza a escala fisica da manutencao.

Se o dado de area estiver ausente, zerado ou com cabecalhos divergentes, o grafico pode perder utilidade. Nesse caso, a correcao deve ser feita no hub ou no snapshot de origem.

## 13. Indicadores brutos por campus

Esta tabela mostra os dados antes da normalizacao. Ela e a principal area de auditoria do dashboard.

| Indicador | Leitura |
|---|---|
| `N_chamados_total` | Volume total de chamados por campus |
| `N_infra_critica` | Chamados associados a infraestrutura critica |
| `Tempo_medio_resolucao_dias` | Tempo medio de resolucao quando disponivel |
| `Taxa_resolucao_no_prazo` | Proporcao de chamados resolvidos no prazo quando disponivel |
| `N_criticos_alta` | Quantidade de chamados de alta criticidade |
| `N_em_espaco_coletivo` | Chamados em espacos de uso coletivo |
| `Densidade_chamados_por_1000m2` | Volume de chamados ponderado por area |
| `Razao_preventiva_corretiva` | Relacao entre manutencao preventiva e corretiva |
| `Valor_total_gasto_R$` | Valor monetario em reais, exibido como `R$` |
| `N_chamados_repetidos` | Recorrencia de chamados |

O campo `Valor_total_gasto_R$` deve aparecer como moeda brasileira na tabela, por exemplo `R$ 8.493.061,74`.

## 14. Qualidade dos indicadores

O bloco `Qualidade dos indicadores` separa indicadores ativos dos indicadores que ainda nao devem entrar no score composto.

| Status | Significado |
|---|---|
| `ativo` | Indicador numerico com variacao entre campi; entra no score |
| `sem_dados` | Indicador sem valores numericos suficientes; aparece apenas como lacuna |
| `sem_variacao` | Indicador preenchido, mas igual para todos os campi; nao diferencia ranking |
| `parcial` | Indicador com dados numericos, mas com ausencias |

Essa camada e essencial porque o snapshot atual ainda possui campos vazios ou zerados por falta de fonte, como tempo de resolucao, taxa no prazo, densidade por area, criticidade alta e chamados repetidos.

## 15. Limites de interpretacao

Os scores sao comparativos dentro do snapshot carregado. Se o conjunto de campi, o periodo ou os dados de origem mudarem, os limites de normalizacao tambem mudam.

O painel nao deve ser lido como certificacao oficial ODS ou ESG. Ele e uma camada analitica e metodologica baseada nos dados operacionais disponiveis no ecossistema Malha IA.

O recalculo completo depende de credencial Google no hub `malha-ia`. Este repositorio consome snapshots publicos versionados e nao precisa de `AUTENTICACAO_GOOGLE` para atualizar o dashboard.

## 16. Sequencia recomendada para o artigo

Primeiro, descreva a origem dos dados e a fronteira do corpus. Depois, apresente os indicadores brutos. Em seguida, explique os pesos ODS e a classificacao ESG. Por fim, use os rankings e composicoes como resultados interpretativos, sempre deixando claro que eles derivam de normalizacao multicriterio aplicada ao snapshot analisado.
