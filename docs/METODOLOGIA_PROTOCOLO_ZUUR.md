# Protocolo de exploracao de dados - Zuur et al. (2010)

Este eixo adapta o protocolo de oito passos de Zuur, Ieno & Elphick (2010) aos indicadores ODS/ESG multicriterio por campus.

Referencia: Zuur, A.F., Ieno, E.N. & Elphick, C.S. (2010). A protocol for data exploration to avoid common statistical problems. Methods in Ecology and Evolution, 1(1), 3-14. doi:10.1111/j.2041-210X.2009.00001.x.

Aplicacao no artigo: antes de compor scores ODS/ESG, os indicadores brutos devem ser inspecionados quanto a outliers, zeros estruturais, escalas discrepantes, colinearidade e dependencia por unidade institucional. Os passos de relacao Y-X e interacao sao reinterpretados como pesos indicador-ODS e leitura indicador-ODS-ESG.

Artefatos:

1. `scripts/gerar_protocolo_zuur.py`
2. `dados/protocolo_zuur.json`
3. `dados_csv/protocolo_zuur.csv`
4. Bloco "Protocolo de exploracao de dados" em `dashboard.html`

Diagnostico atual: faltam matriz de correlacao/VIF entre indicadores, regra explicita para zeros estruturais versus dados ausentes e diagnostico de dependencia por campus ou area institucional.
