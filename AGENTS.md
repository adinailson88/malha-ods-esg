# AGENTS.md - Malha ODS ESG

## Regime de trabalho

Atuar em modo tecnico, objetivo e verificavel. Quando houver insuficiencia de dados, declarar exatamente: `Informação insuficiente para verificar.`

## Fronteira do repositorio

Este repositorio corresponde ao eixo ODS/ESG do ecossistema Malha IA: indicadores brutos por campus, pesos multicriterio e painel de decisao para ODS 9, ODS 11 e ODS 12.

O repositorio `adinailson88/malha-ia` permanece como hub central dos dados. Este repositorio pode manter snapshots JSON/CSV derivados para reprodutibilidade, mas nao deve se tornar a fonte primaria da base `CHAMADOS`.

## Arquivos principais

1. `motor_ods.py`: calcula `INDICADORES_ODS` e garante `PESOS_ODS`.
2. `dashboard.html`: painel ODS/ESG especifico.
3. `dados/*.json`: snapshots de leitura vindos do hub `malha-ia`.
4. `dados_csv/*.csv`: tabelas derivadas para auditoria.
5. `scripts/baixar_dados_hub.py`: sincroniza snapshots publicos do hub.
6. `scripts/exportar_dados_csv.py`: gera CSVs canonicos.
7. `.github/workflows/ods_indicadores.yml`: recalcula ODS no Google Sheets.
8. `.github/workflows/atualizar-dados-hub.yml`: atualiza snapshots deste repo a partir do hub.

## Limites

Nao trazer motores de classificacao, previsao de chamados ou previsao de custos para este repositorio.

Nao duplicar `dados/chamados.json` por padrao. A base bruta pertence ao hub `malha-ia`.

