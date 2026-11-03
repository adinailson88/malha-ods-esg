# Contexto do pré-projeto de doutorado (resumo para continuidade)

Resumo, em linguagem própria, do documento de Drive "2026_PROPOSTA_Biossistemas_Projeto_Doutorado_Governanca_Manutencao" (Google Doc, versão de 20/05/2026, identificador `1SHP8pOe5bu506sT1O24EJrJLnkLT-lGWbumCbCqti-0`, pasta do doutorado no Drive de adinailson.oliveira@cja.ufsb.edu.br), lido em 03/11/2026 pelo conector de Drive. Existem versões anteriores com títulos "PRÉ - PROJETO BIOSSISTEMAS" (`1GsVd8fVg7rxn2lLR6i1svaVHTuPnV7eJx3vuhXsDZK4`, 04/01/2026) e "PROJETO DOUTORADO" (`1TF8Ih16w5zYFGPFWi4LXtNTktjBH29NIEhiYHKO0bk4`, 02/12/2025, escopo anterior de previsão de custos e cartilha para ETP e TR). Documentos do Drive trazem dados pessoais (CPF) que não devem ser copiados para repositórios públicos.

## Identificação

Título: Modelo preditivo de governança sustentável na manutenção predial de universidades públicas sob a perspectiva dos biossistemas construídos. Doutorado em Biossistemas, UFSB, Itabuna, 2026. Orientador indicado no documento: Prof. Dr. Fabrício Berton Zanchi. A versão anterior registrava "possível orientador" e a de 2025 listava outros nomes; a situação atual da orientação não é presumida e deve ser confirmada pelo autor.

## Problema e hipótese

Fragilidade da gestão de manutenção predial nas IFES (registros fragmentados, predominância corretiva, restrição orçamentária). O campus é tratado como biossistema construído (infraestrutura, usuários, recursos, processos e fluxos de informação) e a manutenção como mecanismo de retroalimentação. Pergunta: em que medida a integração entre modelagem preditiva por IA e biossistemas construídos promove governança preditiva e sustentável nas IFES. Hipótese H1: a integração entre governança de dados, modelagem preditiva e apoio multicritério eleva (i) a acurácia da previsão do custo anual em relação a um baseline e (ii) a auditabilidade da priorização por registros verificáveis (relatórios, matrizes custo por criticidade, bases estruturadas). Questões Q1 (planejamento de custos e sazonalidade multicampi) e Q2 (instrumento de priorização baseado em evidências que reduza decisões ad hoc).

## Objetivos específicos (resumo)

1. Arquitetura de dados e governança da informação (OS e contratos, integridade e rastreabilidade).
2. Modelagem do ecossistema de biossistemas construídos (variáveis físicas, humanas, tecnológicas e ambientais).
3. Arquitetura de IA com PLN para classificação de falhas e criticidade.
4. Modelos preditivos de demanda e custos com validação temporal.
5. Método multicritério de apoio à decisão (MCDM) integrando pilares ESG, com índice sintético de priorização.
6. Validação de escalabilidade e transferibilidade (estudo de caso UFSB e manual de governança e boas práticas).

## Método e produtos que tocam este repositório (ODS/ESG e MCDM)

1. Eixo 1 (IA/PLN) e Eixo 2 (previsão: RLM, SES e ARIMA, com MAE, RMSE e R2 contra baseline) alimentam a camada de integração.
2. Integração geoespacial com QGIS e Google Earth Engine (mapas de incidência e criticidade por campus).
3. MCDM com AHP e TOPSIS, índice sintético de priorização, matriz custo por criticidade e análise de sensibilidade (cronograma, atividade 7: "Integrar (QGIS/GEE) e priorizar (MCDM TPM+ESG/ODS) com análise de sensibilidade").
4. Associação aos ODS: ODS 9 (objetivos 1, 4 e 5: governança, predição e MCDM), ODS 11 (objetivos 2 e 5: leitura territorial e priorização) e ODS 12 (objetivos 1 e 5: rastreabilidade e eficiência).
5. Produtos: conjunto de indicadores alinhados aos ODS 9, 11 e 12 (custos por sistema e território, volume e custo de corretivas, picos de demanda), instrumento decisório com critérios e pesos documentados, protocolo replicável para ETP e TR, mapas por campus, painel interativo, dicionário de dados, manual de governança, ao menos 2 artigos em periódicos Qualis A1 a B1 e 2 eventos.
6. Critério de mensurabilidade declarado: comparação com baseline (modelo ingênuo ou média histórica) e estabilidade do ranqueamento sob variação controlada de pesos.
7. Normas citadas: NBR 5674, NBR 14037 e NBR ISO 41001.

## Cronograma (8 semestres, 4 anos)

Revisão de literatura e arquitetura de dados no ano 1; IA/PLN e modelos no ano 2; previsão, validação, integração geoespacial e MCDM no ano 3; consolidação do manual, artigos e qualificação no ano 4 (a defesa também aparece no ano 4).

## Diferença relevante entre o pré-projeto e o estado do repositório

O pré-projeto promete AHP-TOPSIS (pesos derivados de comparação pareada com razão de consistência) e análise de sensibilidade. O repositório declara pesos operacionais editáveis, "não AHP formal". Essa lacuna precisa ser fechada ou o texto do projeto deve ser ajustado. Detalhes em `docs/PLANO_ARTIGO_ODS_ESG.md`.
