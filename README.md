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
6. `dados/metadados_indicadores.json`: contrato de qualidade, limites e melhorias esperadas por indicador.
7. `dados/pesos_categorias_ods_esg.json`: familias de chamados e pesos metodologicos por ODS/ESG.
8. `dados/regras_peso_chamado_ods_esg.json`: peso de evidencia de cada campo do chamado.
9. `dados/multiplicadores_importancia_chamado.json`: multiplicadores por criticidade, urgencia, preventiva e recorrencia.
10. `dados/estrutura_preditiva_ods_esg.json`: contrato conceitual para custo previsto, demanda prevista, clima e decisao governamental.
11. `dados/patrimonio_imobiliario.json`: snapshot normalizado da aba `Patrimônio Imobiliário1`.
12. `dados/patrimonio_imobiliario_campus_ano.json`: agregacao anual por campus.
13. `dados/patrimonio_imobiliario_mapa.json`: pontos geograficos do ano mais recente para mapa patrimonial.
14. `dados/area_manutencao.json`: serie de area institucional agregada usada como contexto.
15. `dados/modelo_area_campus.json`: contrato para area construida/total por campus.
16. `scripts/gerar_patrimonio_imobiliario.py`: gera snapshots patrimoniais a partir da planilha de patrimonio imobiliario.
17. `scripts/baixar_dados_hub.py`: baixa do hub os JSONs publicos usados pelo dashboard.
18. `.github/workflows/ods_indicadores.yml`: workflow de compatibilidade que sincroniza indicadores publicos do hub.
19. `.github/workflows/atualizar-dados-hub.yml`: workflow periodico para atualizar snapshots a partir do hub.
20. `docs/GUIA_LEITURA_DASHBOARD.md`: documentacao de leitura do painel, tabelas, indicadores, pesos e limites de interpretacao.
21. `docs/METODOLOGIA_MCDM_ODS_ESG.md`: metodologia multicriterio, referencias e cautelas de interpretacao.
22. `docs/MODELO_PLANILHA_ODS_ESG.md`: modelo recomendado para organizar a planilha ODS/ESG.
23. `docs/ESTRUTURA_PREDITIVA_ODS_ESG.md`: desenho da camada futura de cenarios preditivos.
24. `docs/REGRA_PESO_CHAMADO_ODS_ESG.md`: regra de pontuacao ODS/ESG por chamado.

## Leitura do painel

O dashboard exibe:

1. Cards de escala da base: campi avaliados, chamados considerados, gasto registrado em reais e melhor score geral.
2. Ranking geral ODS/ESG por campus.
3. Comparacao separada de ODS 9, ODS 11 e ODS 12.
4. Painel de decisao TOPSIS/AHP para ranquear campi como alternativas.
5. Ranking ESG por campus e composicao E/S/G do melhor campus.
6. Tabelas de scores compostos, classificacao metodologica ODS/ESG, pesos multicriterio e indicadores brutos.
7. Diagnostico de qualidade dos indicadores, separando indicadores ativos de lacunas da planilha.

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
python scripts\gerar_patrimonio_imobiliario.py --csv caminho\Patrimonio_Imobiliario1.csv
python scripts\exportar_dados_csv.py
python scripts\gerar_protocolo_zuur.py
python scripts\gerar_analise_gam.py
```

## Patrimonio imobiliario

A camada patrimonial usa a planilha Google `Patrimônio Imobiliário`, aba `Patrimônio Imobiliário1`, com as colunas `Item`, `Cód.`, `Descrição`, `Endereço`, `Cidade`, `Área (m²) - Terreno`, `Área (m²) - Utilização`, `Valores (R$) - Terreno`, `Valores (R$) - Utilização`, `Valor Final (Imóvel R$)`, `Latitude x Longitude` e `Campus`.

Como a planilha pode estar restrita, o script `scripts/gerar_patrimonio_imobiliario.py` aceita tres rotas:

1. `--google-auth`: leitura autenticada por conta de servico, recomendada para GitHub Actions.
2. `--csv caminho\arquivo.csv`: CSV exportado manualmente da aba.
3. URL CSV publica, apenas se a planilha estiver liberada para leitura por link.

O workflow `.github/workflows/patrimonio_imobiliario.yml` roda manualmente ou uma vez a cada tres meses. Para funcionar no GitHub, configure o secret `GCP_SA_KEY` com o JSON da conta de servico e compartilhe a planilha `Patrimônio Imobiliário` com o e-mail dessa conta. Os dados sao preservados por ano e agregados por campus, permitindo densidade de chamados por area, custo por area, valor patrimonial exposto e mapa por cidade/coordenada.

## Protocolo de exploracao de dados

O diagnostico transversal baseado em Zuur, Ieno & Elphick (2010) e gerado por `scripts/gerar_protocolo_zuur.py`, publicado em `dados/protocolo_zuur.json` e resumido em `dados_csv/protocolo_zuur.csv`. A metodologia reutilizavel no artigo esta em [`docs/METODOLOGIA_PROTOCOLO_ZUUR.md`](docs/METODOLOGIA_PROTOCOLO_ZUUR.md).

## Metodo multicriterio ODS/ESG

O dashboard usa soma ponderada normalizada para leitura ODS e TOPSIS/AHP para apoio a decisao. Indicadores sem dados numericos suficientes ou sem variacao entre campi sao exibidos na auditoria, mas nao entram no score composto ou no ranking TOPSIS. Isso evita ranking artificial quando a planilha ainda nao contem tempo de resolucao, SLA, area por campus, criticidade validada ou chave de recorrencia.

Referencias e criterio de leitura: [`docs/METODOLOGIA_MCDM_ODS_ESG.md`](docs/METODOLOGIA_MCDM_ODS_ESG.md).

Modelo recomendado de planilha: [`docs/MODELO_PLANILHA_ODS_ESG.md`](docs/MODELO_PLANILHA_ODS_ESG.md).

## Camada preditiva ODS/ESG

A evolucao prevista do painel conecta categorias de chamados, custo executado, custo previsto por IA, quantidade observada, quantidade prevista, chuva, calor e decisao governamental. Essa camada permite estimar como o ranking TOPSIS/AHP pode mudar em cenarios futuros, sem confundir previsao com dado observado.

Contrato metodologico: [`docs/ESTRUTURA_PREDITIVA_ODS_ESG.md`](docs/ESTRUTURA_PREDITIVA_ODS_ESG.md).

## Camada GAM explicavel

A adequacao de Generalized Additive Models e registrada por `scripts/gerar_analise_gam.py`, com saida em `dados/analise_gam.json` e `dados_csv/analise_gam.csv`. No snapshot ODS/ESG atual, GAM nao e recomendado como ajuste inferencial por insuficiencia de unidades observacionais; fica documentado como extensao futura para painel campus-mes. A metodologia esta em [`docs/METODOLOGIA_GAM.md`](docs/METODOLOGIA_GAM.md).

## Recalculo autenticado

O recalculo completo contra Google Sheets fica centralizado no repositorio `malha-ia`, que publica os snapshots em `dados/*.json`. Este repositorio nao precisa de `AUTENTICACAO_GOOGLE` para atualizar o dashboard.

## Licenca

Informação insuficiente para verificar.
