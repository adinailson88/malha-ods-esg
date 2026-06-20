# Regra de peso por chamado para ODS/ESG

Este documento define como cada chamado pode receber pontuacao ODS/ESG a partir de seus campos operacionais.

## 1. Objetivo

Transformar cada chamado em uma unidade de evidencia ODS/ESG, sem depender apenas do indicador agregado por campus. A regra usa categoria, classificacao IA, importancia, titulo, descricao GLPI, titulo OSM, descricao OSM, solucao, valor, campus/area, periodo, clima e decisao governamental.

## 2. Arquivos de contrato

| Arquivo | Funcao |
|---|---|
| `dados/pesos_categorias_ods_esg.json` | Define pesos ODS/ESG por familia tecnica de chamado |
| `dados/regras_peso_chamado_ods_esg.json` | Define peso de evidencia de cada campo do chamado |
| `dados/multiplicadores_importancia_chamado.json` | Define multiplicadores por importancia, criticidade, preventiva e recorrencia |

## 3. Campos usados

| Campo | Peso | Papel |
|---|---:|---|
| Categoria completa | 3.0 | principal fonte da familia tecnica |
| Classificacao IA | 2.5 | apoio quando houver confianca e auditoria |
| Importancia/Criticidade | 2.5 | multiplicador de risco |
| Titulo do chamado | 2.0 | sintoma e local em texto curto |
| Descricao GLPI | 2.0 | contexto, impacto e recorrencia |
| Titulo OSM | 1.5 | confirmacao da execucao |
| Descricao OSM | 2.0 | causa, solucao, material e escopo executado |
| Solucao OSM | 1.8 | resolutividade, material, desperdicio, recorrencia |
| Valor/Custo | 1.3 | pressao orcamentaria |
| Campus/Area | 1.0 | normalizacao por escala fisica |
| Data/Periodo | 0.8 | sazonalidade |
| Fonte climatica | 1.2 | condicionante ambiental |
| Decisao governamental | 1.2 | condicionante de governanca |

## 4. Formula operacional

Para cada chamado:

1. identificar a familia tecnica pelo campo mais forte disponivel;
2. herdar os pesos de `pesos_categorias_ods_esg.json`;
3. somar evidencias textuais por campo usando `regras_peso_chamado_ods_esg.json`;
4. aplicar multiplicadores de importancia/criticidade;
5. aplicar condicionantes de chuva, calor, custo previsto, demanda prevista e decisao governamental quando existirem;
6. gerar os campos finais: `peso_ODS9`, `peso_ODS11`, `peso_ODS12`, `peso_E`, `peso_S`, `peso_G`.

Forma conceitual:

`peso_dimensao_chamado = peso_familia_dimensao * evidencia_campos * multiplicador_importancia * condicionantes_contextuais`

## 5. Regra de evidencia insuficiente

Quando categoria, classificacao IA, titulo, descricao GLPI e OSM nao trouxerem evidencia minima para familia tecnica ou impacto, o chamado deve receber:

`Informação insuficiente para verificar.`

Esse caso nao deve ser forcado para ODS/ESG apenas por campus, valor ou data.

## 6. Como isso alimenta o painel

A pontuacao por chamado permite agregar:

1. por campus;
2. por campus-periodo;
3. por familia de categoria;
4. por ODS;
5. por pilar ESG;
6. por custo executado;
7. por custo previsto;
8. por demanda prevista;
9. por cenario de chuva, calor ou decisao governamental.

Essa agregacao prepara a aba futura `Cenarios futuros` do dashboard e permite que o TOPSIS/AHP ranqueie nao apenas campi, mas tambem campus-categoria-periodo.

