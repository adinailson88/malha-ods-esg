# Contrato de dados - ODS/ESG

## Fonte central

O repositorio `adinailson88/malha-ia` permanece como hub central dos dados. Este repositorio usa snapshots pequenos para dashboard, auditoria e reprodutibilidade do eixo ODS/ESG.

## Arquivos pertinentes

| Aba no Google Sheets | Arquivo JSON | Papel |
|---|---|---|
| INDICADORES_ODS | `dados/indicadores_ods.json` | Indicadores brutos por campus |
| PESOS_ODS | `dados/pesos_ods.json` | Pesos ODS por indicador |
| Configuracao local | `dados/classificacao_ods_esg.json` | Classificacao dos indicadores por ODS e ESG |
| Area Manutencao | `dados/area_manutencao.json` | Contexto de area construida e area total |

## Indicadores brutos

1. `N_chamados_total`
2. `N_infra_critica`
3. `Tempo_medio_resolucao_dias`
4. `Taxa_resolucao_no_prazo`
5. `N_criticos_alta`
6. `N_em_espaco_coletivo`
7. `Densidade_chamados_por_1000m2`
8. `Razao_preventiva_corretiva`
9. `Valor_total_gasto_R$`
10. `N_chamados_repetidos`

## Regra de fronteira

`CHAMADOS` nao deve ser duplicado aqui como fonte primaria. Quando for necessario recalcular indicadores, usar `motor_ods.py` com acesso autenticado a planilha operacional.

## Classificacao ODS/ESG

`dados/classificacao_ods_esg.json` e uma configuracao metodologica local do painel. Ela nao substitui `PESOS_ODS`; ela explicita, para leitura academica e visualizacao, como cada indicador se associa a ODS 9, ODS 11, ODS 12 e aos pilares ESG Ambiental, Social e Governanca.
