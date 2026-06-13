# Malha ODS ESG

Repositorio do eixo ODS/ESG do ecossistema Malha IA: indicadores multicriterio para manutencao predial universitaria, com foco em ODS 9, ODS 11 e ODS 12.

Repositorio-hub de dados: [adinailson88/malha-ia](https://github.com/adinailson88/malha-ia)  
Dashboard previsto: `https://adinailson88.github.io/malha-ods-esg/`

## Escopo

Este repositorio separa o painel ODS/ESG do repositorio central `malha-ia`. O objetivo e manter um produto tecnico-cientifico especifico para indicadores de sustentabilidade, governanca e apoio a decisao multicriterio aplicados aos chamados de manutencao predial.

Ficam fora deste repositorio:

1. Classificacao de chamados.
2. Previsao temporal de chamados.
3. Previsao de custos.
4. Atualizacao reversa GLPI.
5. Base bruta completa `CHAMADOS` como fonte primaria.

## Componentes

1. `motor_ods.py`: calcula indicadores brutos por campus e cria/preserva pesos ODS.
2. `dashboard.html`: painel ODS/ESG com pesos editaveis, rankings e graficos.
3. `dados/indicadores_ods.json`: snapshot dos indicadores brutos.
4. `dados/pesos_ods.json`: snapshot dos pesos multicriterio.
5. `dados/classificacao_ods_esg.json`: configuracao de classificacao dos indicadores por ODS e ESG.
6. `dados/area_manutencao.json`: serie de area usada como contexto institucional.
7. `scripts/baixar_dados_hub.py`: baixa do hub os JSONs publicos usados pelo dashboard.
8. `.github/workflows/ods_indicadores.yml`: workflow pesado para recalcular indicadores no Google Sheets.
9. `.github/workflows/atualizar-dados-hub.yml`: workflow leve para atualizar snapshots a partir do hub.
10. `docs/GUIA_LEITURA_DASHBOARD.md`: documentacao de leitura do painel, tabelas, indicadores, pesos e limites de interpretacao.

## Leitura do painel

O dashboard exibe:

1. Cards de escala da base: campi avaliados, chamados considerados, gasto registrado em reais e melhor score geral.
2. Ranking geral ODS/ESG por campus.
3. Comparacao separada de ODS 9, ODS 11 e ODS 12.
4. Ranking ESG por campus e composicao E/S/G do melhor campus.
5. Tabelas de scores compostos, classificacao metodologica ODS/ESG, pesos multicriterio e indicadores brutos.

Documentacao detalhada: [`docs/GUIA_LEITURA_DASHBOARD.md`](docs/GUIA_LEITURA_DASHBOARD.md).

## Execucao local

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r execucao_offline\requirements.txt
```

Validacao sintatica:

```powershell
python -m py_compile motor_ods.py
python -m py_compile scripts\baixar_dados_hub.py
python -m py_compile scripts\exportar_dados_csv.py
```

Atualizar snapshots a partir do hub:

```powershell
python scripts\baixar_dados_hub.py
python scripts\exportar_dados_csv.py
```

Executar recalculo completo contra Google Sheets:

```powershell
python motor_ods.py --apenas-ods
```

## Secret necessario

O workflow `ods_indicadores.yml` precisa do secret:

`AUTENTICACAO_GOOGLE`

O mesmo secret deve ser reaproveitado nos repositorios derivados que acessarem a mesma planilha operacional.

## Licenca

Informação insuficiente para verificar.
