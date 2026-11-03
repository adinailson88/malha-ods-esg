# Plano do artigo do eixo ODS/ESG: diagnóstico, alinhamento ao pré-projeto e próximos passos

Documento de trabalho de 03/11/2026, elaborado a partir da leitura direta de `adinailson88/malha-ods-esg` (commit `836970b`), do hub `adinailson88/malha-ia` (motores e `dados/chamados.json`, commit `526abb8`, mais o PR de correção de datas já mergeado), do pré-projeto de doutorado no Drive (resumo em `docs/CONTEXTO_PREPROJETO.md`) e de execuções de verificação próprias (`scripts/diagnostico/mcdm_sensibilidade.py`). Quando algo não pôde ser verificado, consta "Informação insuficiente para verificar." O manuscrito canônico continua sendo `docs/ARTIGO_MALHA_ODS_ESG.md`; este plano não o substitui.

## 1. Estado atual do repositório

O eixo calcula indicadores brutos por campus (`motor_ods.py`, executado no hub), mantém pesos multicriterio editáveis, um painel com soma ponderada por ODS e TOPSIS, uma camada de patrimônio imobiliário e um artigo canônico com Introdução, Métodos, Resultados (4.1 a 4.5), Discussão, Limitações e Conclusão, atualizado em 20/06/2026 (`docs/CONTINUIDADE_ARTIGO_ODS_ESG.md`). Os dados em `dados/` são snapshots sincronizados do hub; a base bruta continua no hub.

## 2. Alinhamento com o pré-projeto

O pré-projeto (objetivo específico 5, atividade 7 do cronograma e resultados esperados) promete: MCDM com AHP-TOPSIS, índice sintético de priorização, matriz custo por criticidade, análise de sensibilidade com estabilidade do ranqueamento sob variação controlada de pesos, integração com QGIS e Google Earth Engine, e aderência aos ODS 9, 11 e 12 com indicadores de custos por sistema e território, volume e custo de corretivas e picos de demanda. O estado atual cobre parcialmente:

1. Cobertos: soma ponderada por ODS, TOPSIS, painel, mapa patrimonial, camada de patrimônio e contrato de estrutura preditiva.
2. Não cobertos: AHP formal (matriz pareada e razão de consistência, que o repositório declara explicitamente não ter), análise de sensibilidade e correlação de postos (listadas como pendentes na nota de continuidade), matriz custo por criticidade, indicadores por sistema (a classificação existe, mas os indicadores são por campus), picos de demanda e custo previstos (dependem dos Artigos 2 e 3), integração com Google Earth Engine.
3. Divergência de redação a resolver: o projeto fala em AHP-TOPSIS; o repositório afirma "pesos operacionais, não AHP formal". Ou se realiza a elicitação AHP, ou o texto do projeto e do artigo deve descrever o método como TOPSIS com pesos operacionais.

## 3. Achados verificados nesta análise

### 3.1 O snapshot do indicador de razão preventiva é uma contagem, não uma razão

`dados/indicadores_ods.json` traz `Razao_preventiva_corretiva` igual a 925 (Jorge Amado), 1.295 (Paulo Freire), 1.637 (Sosígenes Costa), 550 (Reitoria) e 4 (Maria Felipa). São exatamente as contagens de chamados com classificação preventiva (coluna Z) em `chamados.json`, o que corresponde ao comportamento antigo do motor (quando `n_corr` era sempre zero e o indicador devolvia `float(n_prev)`). O motor atual do hub e deste repositório calcula a proporção `n_prev / (n_prev + n_corr)` e, com o `chamados.json` atual, daria 0,234 (Jorge Amado), 0,330 (Paulo Freire), 0,386 (Sosígenes Costa), 0,224 (Reitoria) e 0,364 (Maria Felipa). O workflow do hub `4 - Indicadores ODS` roda diariamente com sucesso (a execução de 02/11/2026 registrou "INDICADORES_ODS atualizada para 5 campi"), de modo que a causa da divergência entre o código e o snapshot não foi determinada. Teste para localizar o defeito: abrir a aba `INDICADORES_ODS` da planilha e conferir a coluna `Razao_preventiva_corretiva`; se mostrar 0,234, o defeito está na exportação para JSON; se mostrar 925, está na escrita da aba (por exemplo, outro processo ou versão do motor escrevendo na aba). Consequência: com a razão como contagem, o critério "maximizar razão" premia o tamanho do campus, e todos os números de Resultados do manuscrito (calculados em junho, com razões entre 0,26 e 0,34) não são reproduzíveis com o snapshot atual.

### 3.2 Leitura de criticidade provavelmente em coluna errada

O motor define `COL_CRITICIDADE_OUT = 30` com o comentário "AD". No `chamados.json` a coluna "Criticidade Atribuída por IA" tem índice 29 (AD, contando de zero) e todas as 14.580 linhas têm 30 colunas; com índice 30, a condição `len(l) > 30` nunca é verdadeira e `N_criticos_alta` resulta sempre em zero. Contando a coluna de índice 29, há 149 chamados de criticidade "Alta" (Jorge Amado 46, Paulo Freire 31, Sosígenes Costa 47, Reitoria 25). O indicador é tratado pelo painel como "constante zero" e excluído, quando provavelmente é um erro de leitura de coluna. A planilha ao vivo pode ter colunas diferentes do JSON exportado; Informação insuficiente para verificar sem abrir a planilha.

### 3.3 O ranking depende da escala dos campi e do método, não dos pesos

A reprodução em Python das funções do painel (`scripts/diagnostico/mcdm_sensibilidade.py`) sobre o snapshot publicado dá, para soma ponderada e TOPSIS, ordenações diferentes e correlações de postos baixas ou negativas (Spearman entre métodos de 0,3 com cinco unidades, de -0,4 sem Maria Felipa, de -0,2 com a razão corrigida e de 0,4 com normalização por área). Em sorteios de 5.000 vetores de pesos (cada peso multiplicado por um fator uniforme entre 0,5 e 1,5), a primeira posição quase não muda dentro de cada método: nos cenários com quatro unidades, a soma ponderada elege sempre a mesma unidade e o TOPSIS elege sempre Jorge Amado (nos cenários S1 e S2 a soma ponderada elege sempre a Reitoria e no S3 sempre Sosígenes Costa); com cinco unidades, o TOPSIS elege Jorge Amado em 82% dos sorteios e Maria Felipa em 14%, e a soma ponderada elege sempre Maria Felipa. Ou seja, a instabilidade está entre métodos e entre normalizações, e não nos pesos, que são a única dimensão que a análise de sensibilidade planejada cobriria.

Os indicadores de contagem e de gasto são absolutos e não são normalizados por escala física ou de uso. Ao dividir contagens e gasto por 1.000 m2 de área de utilização de 2025 (patrimônio), o ranking se inverte: Reitoria passa a última (2.454 chamados em 2.606 m2) e Sosígenes Costa e Jorge Amado sobem. A pontuação de Maria Felipa (11 chamados, sem custo) lidera a soma ponderada por artefato de escala (reconhecido no manuscrito e na nota de continuidade). Resumo dos cenários executados:

| Cenário | Soma ponderada (1º ao último) | TOPSIS (1º ao último) | Spearman entre métodos |
|---|---|---|---|
| S0 snapshot publicado, 5 unidades | Maria Felipa, Reitoria, Paulo Freire, Jorge Amado, Sosígenes | Jorge Amado, Reitoria, Maria Felipa, Paulo Freire, Sosígenes | 0,3 |
| S1 sem Maria Felipa | Reitoria, Paulo Freire, Jorge Amado, Sosígenes | Jorge Amado, Paulo Freire, Sosígenes, Reitoria | -0,4 |
| S2 S1 com razão preventiva como proporção | Reitoria, Paulo Freire, Sosígenes, Jorge Amado | Jorge Amado, Reitoria, Paulo Freire, Sosígenes | -0,2 |
| S3 S2 com contagens e gasto por 1.000 m2 | Sosígenes, Paulo Freire, Jorge Amado, Reitoria | Jorge Amado, Sosígenes, Paulo Freire, Reitoria | 0,4 |

Com quatro ou cinco alternativas, a correlação de postos tem poder muito baixo e o método tem pouco conteúdo discriminante; o valor científico do eixo está no arcabouço, nos critérios e na sensibilidade, e não no ranking de campi em si.

### 3.4 O indicador de gasto é dominado por contratação, não por manutenção

`Valor_total_gasto_R$` soma a coluna Q (valor das ordens de serviço). Os 93 chamados da categoria "Posto de trabalho > Contratação..." respondem por 50% a 61% do gasto de cada campus (Reitoria 61%, Jorge Amado 54%, Paulo Freire 52%, Sosígenes Costa 50%). O indicador do ODS 12 (peso 0,2 a 0,35) mede em boa parte eventos de contratação e, como o valor existe apenas nos chamados com ordem de serviço (16,5% do total), não representa o custo de manutenção. Fica pendente decidir se esses eventos entram, saem ou formam critério separado.

### 3.5 Área por campus já existe no próprio repositório

`dados/patrimonio_imobiliario_campus_ano.json` traz, por campus (CJA, CPF, CSC e Reitoria) e ano de 2015 a 2025, `Area_Utilizacao_m2` e `Area_Terreno_m2`. A soma de `Area_Utilizacao_m2` entre campi coincide com a área construída global de `dados/area_manutencao.json`: igual em 2015 a 2021 (diferença 0,0%), 0,3% maior em 2022 a 2024 e 4,8% maior em 2025. É forte indício de mesma fonte e de que `Area_Utilizacao_m2` é a área construída por campus, o que a camada ainda não usa: `Densidade_chamados_por_1000m2` está zerada e `dados/modelo_area_campus.json` está "pendente" para todos os campi. A equivalência entre "utilização" e "construída" é inferida e deve ser confirmada pelo autor. A correspondência de nomes (CJA, CPF, CSC) com os campi dos chamados também é inferida, e a área da Reitoria (2.606 m2) pode não cobrir todas as edificações atendidas pelos chamados lançados como "Reitoria". Não há área para 2026 nem para Maria Felipa.

### 3.6 Outros pontos observados

1. `Tempo_medio_resolucao_dias` e `Taxa_resolucao_no_prazo` dependem de `COL_DATA_CONCLUSAO`, definida como `None`. A existência de data de conclusão na base não foi verificada (o `chamados.json` tem 30 colunas, 12 sem nome).
2. A categoria usada para "infraestrutura crítica", "preventiva" e "corretiva" vem da classificação por IA (coluna Z, executor "Reclass_LSTM" nas linhas observadas), cuja acurácia contra referência humana é de 83,07% no artigo de classificação (RAP). Os indicadores herdam esse erro, e a incerteza não é propagada.
3. O parse de datas dos motores foi corrigido no hub (PR malha-ia#6, mergeado em 03/11/2026). Os indicadores atuais do eixo não dependem de série temporal, mas o fluxo de indicadores por período (campus e mês ou ano), necessário para sensibilidade temporal e para o uso de previsões, depende dessa correção e de reexecução.
4. O eixo mede 4 unidades reais (Jorge Amado, Paulo Freire, Sosígenes Costa, Reitoria) mais uma de 11 chamados. Um painel campus por período (4 unidades por 9 a 11 anos) amplia as observações para sensibilidade e tendência.

## 4. Melhorias propostas, em ordem de prioridade

1. Corrigir e reexecutar a cadeia de indicadores: localizar por que o snapshot traz contagem em `Razao_preventiva_corretiva` (seção 3.1), corrigir `COL_CRITICIDADE_OUT` se a planilha confirmar o índice 29 (seção 3.2), regenerar `INDICADORES_ODS` e os snapshots, e recalcular os Resultados do manuscrito. Alterações em `motor_ods.py` devem ser feitas também no hub, que é quem executa.
2. Normalizar por escala: usar `Area_Utilizacao_m2` por campus (e, quando existir, número de usuários) para expressar chamados, infraestrutura crítica, espaços coletivos e gasto por 1.000 m2; ativar `Densidade_chamados_por_1000m2`; atualizar `modelo_area_campus.json` com os dados do patrimônio e projetar 2026 com a regra do autor (último valor mais 5% ao ano) marcando a origem.
3. Separar o custo de contratação do custo corrente no critério de gasto e documentar a escolha.
4. Sensibilidade completa: executar e reportar (i) pesos (varredura global e por critério), (ii) normalização (min-max contra área), (iii) método (soma ponderada, TOPSIS, e ao menos um terceiro método, por exemplo VIKOR ou PROMETHEE II), (iv) exclusão de unidades, com correlação de postos (Spearman e Kendall), probabilidade de primeira posição e intervalos de estabilidade; manter `scripts/diagnostico/mcdm_sensibilidade.py` como base.
5. AHP formal ou redação honesta: se o autor decidir por AHP, elicitar matrizes pareadas com especialistas (gestores de manutenção e de contratos da UFSB), calcular o autovetor, a razão de consistência (CR menor que 0,10) e agregar julgamentos (média geométrica); registrar protocolo, amostra de especialistas e termo de consentimento conforme exigência do comitê de ética aplicável (a necessidade de submissão ao CEP não foi verificada).
6. Painel por período: materializar `INDICADORES_ODS_ESG` campus por ano (e mês), prevista em `docs/METODOLOGIA_MCDM_ODS_ESG.md`, para tendência e para integrar previsões.
7. Integrar previsões: usar a previsão de chamados (Artigo 2) e de custo (Artigo 3) como critérios de cenário (contrato em `docs/ESTRUTURA_PREDITIVA_ODS_ESG.md`), somente depois de corrigidas e validadas, preservando a separação entre observado e previsto.
8. Matriz custo por criticidade e indicadores por sistema (climatização, elétrica, hidrossanitária, estrutura), conforme o pré-projeto, com a ressalva de erro de classificação.
9. Camada geoespacial: mapa de incidência por campus (QGIS ou Earth Engine) com coordenadas verificadas do patrimônio.

## 5. Posicionamento científico e risco de fatiamento

O artigo ODS/ESG é o terceiro eixo do ecossistema, após classificação (RAP), previsão de chamados (Artigo 2) e custos (Artigo 3). Para evitar fatiamento, o eixo deve reivindicar apenas: o arcabouço multicritério ODS/ESG auditável para manutenção predial universitária, a normalização por escala, a análise de sensibilidade e robustez, e a rastreabilidade entre chamado, indicador, critério e decisão. Resultados de classificação e de previsão entram apenas como insumo citado, com remissão aos outros artigos. O título provisório do manuscrito ("Integração de dados patrimoniais e indicadores ODS/ESG para apoio multicritério à decisão em manutenção predial universitária") é compatível com esse recorte.

## 6. Literatura (busca preliminar, 03/11/2026, não sistemática)

A busca geral não encontrou artigo de periódico que aplique AHP-TOPSIS à priorização de manutenção de edificações de um campus universitário com ODS 9, 11 e 12; encontrou trabalhos vizinhos. Os itens abaixo são pontos de partida, com DOI apenas quando apareceu nos resultados ou já constava na documentação do repositório; todos exigem conferência no editor antes de citar.

1. Griebeler, Brandli, Salvia, Leal Filho e Reginatto (2021). Framework para implantação de indicadores dos ODS em instituições de ensino superior (61 indicadores). *International Journal of Sustainability in Higher Education*. Título exato e DOI: DOI não encontrado.
2. Artigo de *Sustainability* v. 13, n. 21 (art. 11770, 2021) sobre contribuição dos indicadores do UI GreenMetric aos ODS (DOI provável 10.3390/su132111770, inferido da URL; título e autoria não verificados).
3. Modelo MCDM para gestão sustentável de facilities em edifícios residenciais municipais, *Sustainability*, v. 13, n. 5, art. 2820, DOI 10.3390/su13052820 (já citado em `docs/METODOLOGIA_MCDM_ODS_ESG.md`; autoria não verificada nesta análise).
4. Estudo de AHP-TOPSIS para escala de prioridade de manutenção de componentes de escolas públicas em Bogor, Indonésia (2024), citado em lista de referências; periódico e DOI não confirmados.
5. Estudo de MCDM fuzzy (AHP, TOPSIS e ELECTRE) para modelo de campus sustentável da Universidade de Istambul Gelisim, *Journal of Intelligent & Fuzzy Systems*, 2023 (identificador de DOI 10.3233/JIFS-223778 apareceu na busca; autoria não verificada).
6. Literatura sobre inversão de ranking (rank reversal) no TOPSIS e sensibilidade a pesos e normalização: Triantaphyllou (2000) é citado como origem do problema em fonte secundária; estudos de 2024 e 2025 sobre distâncias, normalização e detecção algorítmica de inversão foram encontrados sem DOI nos resultados. DOI não encontrado.
7. Zuur, Ieno e Elphick (2010), DOI 10.1111/j.2041-210X.2009.00001.x, já usado no repositório para exploração de dados.

A lacuna provisória é a ausência de um arcabouço MCDM auditável, normalizado por escala e com sensibilidade formal, aplicado a dados reais de chamados de manutenção de universidade pública multicampi brasileira e ancorado nos ODS 9, 11 e 12; ela precisa ser confirmada por busca sistemática (Scopus e Web of Science) antes da submissão. Periódicos-alvo e Qualis vigente não foram verificados; as candidatas do plano do Artigo 2 (*Facilities* com rota verde gratuita, *Ambiente Construído*) também servem aqui, com ressalva de que a política de taxas e o Qualis precisam ser conferidos.

## 7. Pendências por responsável

Autor:

1. Confirmar na planilha o valor de `Razao_preventiva_corretiva` (0,234 ou 925) e a posição da coluna de criticidade (AD ou AE).
2. Decidir: AHP formal com especialistas ou TOPSIS com pesos operacionais; terceiro método comparador; tratamento de "Posto de trabalho".
3. Confirmar que `Area_Utilizacao_m2` equivale à área construída e que CJA, CPF e CSC correspondem a Jorge Amado, Paulo Freire e Sosígenes Costa; fornecer área de 2026 e de Maria Felipa.
4. Informar o status da relação com o orientador, a coautoria e o periódico-alvo (não presumidos).
5. Resolver os itens pendentes de `docs/CONTINUIDADE_ARTIGO_ODS_ESG.md` (apagar docs obsoletos no Drive, passar o referencial teórico para prosa).

Dados novos: número de usuários por campus e período (hoje inexistente), data de conclusão e de empenho das OS, calendário e área por campus em 2026, painel por período.

Experimentos: correção e reexecução dos indicadores, sensibilidade completa, terceiro método, AHP (se aprovado), painel campus por ano, integração de previsões após os Artigos 2 e 3.

## 8. Limites desta análise

1. Não foi possível abrir a planilha viva nem o Apps Script (hosts externos bloqueados na sessão em nuvem); as conclusões sobre o snapshot vêm dos JSON e do código.
2. A causa do snapshot com contagem em lugar de razão não foi determinada.
3. Os cenários S0 a S3 replicam as funções do painel em Python e não foram comparados com a execução do navegador; os pesos usados são os do snapshot.
4. A literatura foi buscada de modo não sistemático e vários DOIs não puderam ser confirmados.
5. A necessidade de aprovação em comitê de ética para elicitação AHP não foi verificada.
