# Camada GAM no eixo ODS/ESG

Neste repositorio, GAM nao e adotado como ajuste inferencial principal no snapshot atual. O eixo ODS/ESG e multicriterio e trabalha com poucos campi, portanto curvas suaves seriam instaveis e poderiam superinterpretar a base.

## Papel metodologico

O uso correto, no estado atual, e registrar a inadequacao amostral para GAM e manter a metodologia MCDM/ESG como abordagem principal. GAM so passa a ser tecnicamente defensavel se os indicadores forem materializados como painel temporal, por exemplo campus-mes, com numero suficiente de observacoes por unidade e variacao temporal.

## Artefatos

- `scripts/gerar_analise_gam.py`: gera o diagnostico local de adequacao.
- `dados/analise_gam.json`: contrato consumido pelo dashboard.
- `dados_csv/analise_gam.csv`: resumo tabular para auditoria e artigo.

## Criterio de leitura

O dashboard deve explicitar que a ferramenta foi avaliada, mas nao aplicada como modelo inferencial ao snapshot atual. Isso evita inserir sofisticação estatistica sem suporte empírico.

Enquanto nao houver painel temporal ou mais unidades observacionais, a conclusao deve ser: Informação insuficiente para verificar.
