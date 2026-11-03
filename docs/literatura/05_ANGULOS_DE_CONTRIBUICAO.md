# Ângulos de contribuição e arquitetura do argumento

Objetivo: escolher o recorte que torna este o melhor artigo possível dentro do seu projeto, com a literatura mapeada em `01_MAPA_TEMATICO.md` e os dados descritos em `docs/auditoria/`. As lacunas citadas são provisórias até a revisão sistemática; os resultados são hipóteses e não devem ser lidos como achados.

## 1. Cinco conceitos de artigo comparados

| Conceito | Afirmação central | Por que seria novo (provisório) | Dados necessários | Risco principal | Periódicos de aderência provável |
|---|---|---|---|---|---|
| A. Robustez da priorização | Prioridades de manutenção em universidade multicampi dependem mais de escala, viés de notificação, erro de classificação e método do que dos pesos; quantificar cada fonte | Decomposição conjunta da incerteza em dados reais de chamados; SMAA e sensibilidade global aplicados à manutenção universitária (não localizado na busca) | Painel campus, sistema e ano; área; matriz de confusão; (pesos opcionais, SMAA aceita pesos incertos) | Resultado "tudo é incerto" sem recomendação prática | Construção e decisão: Expert Systems with Applications, Socio-Economic Planning Sciences; ambiente construído: Sustainable Cities and Society, Building and Environment |
| B. Validade preditiva | O índice de prioridade em t antecipa demanda e custo corretivo por exposição em t+1 melhor que referências simples | Validação preditiva raramente testada em índices de priorização (estudos de caso usam validade de face) | Oito anos de painel; datas de solução (melhora) | Poder preditivo fraco (resultado honesto, ainda publicável) | Journal of Building Engineering, Building and Environment, Facilities |
| C. Validade de conteúdo e alinhamento aos ODS | Conjunto de indicadores de manutenção com validade de conteúdo para os ODS 9, 11 e 12 em universidades | Instrumentos de ODS em universidades não usam registros de manutenção (R26, R27); estudos de indicadores em IES (R31, R33) não os têm | Painel de especialistas; texto oficial dos ODS | Depende de painel e ética; menor peso de dados | International Journal of Sustainability in Higher Education, Facilities |
| D. Viés de notificação e equidade entre campi | Diferenças de registro entre campi distorcem a priorização e podem ser medidas e corrigidas | Viés de notificação estudado em solicitações urbanas (R44), não em manutenção universitária | Painel campus e ano; usuários e área | Causalidade e interpretação de práticas locais | Sustainable Cities and Society, Facilities |
| E. Priorização orientada por previsões | Previsões de demanda e custo (Artigos 2 e 3) mudam a ordem de prioridade do próximo ciclo | MCDA temporal com critérios previstos não localizado | Resultados dos Artigos 2 e 3 | Dependência de outros eixos e do hub | Journals de decisão e de gestão |

## 2. Recomendação

Escrever um artigo principal que combine A e B, com D como mecanismo explicativo e com a validação de conteúdo (C) como insumo dos pesos e dos critérios, em vez de dispersar a contribuição. Motivos: (i) A e B respondem à crítica central do parecer (validação e incerteza) e são as lacunas mais bem sustentadas pela literatura de indicadores compostos (R02, R05) e de SMAA (R08); (ii) D explica por que a escala e o registro importam, e há dados para medi-lo agora; (iii) os dados mínimos de A, B e D já existem (painel campus, sistema e ano; área; erro de classificação); (iv) C e E viram artigos seguintes (C como artigo de medida em periódico de ensino superior; E após os Artigos 2 e 3), sem fatiamento, porque cada um reivindica uma contribuição distinta.

Afirmação central proposta: em priorização de manutenção em universidade pública multicampi, a ordem de prioridade é sensível a escolhas de escala, de notificação e de classificação que a literatura costuma ignorar; ao modelar essas incertezas explicitamente e ao validar a prioridade contra a demanda e o custo seguintes, obtém-se um índice cujas posições robustas e instáveis são conhecidas e que antecipa a demanda melhor que referências simples. A segunda metade da frase é hipótese a testar e deve ser rebaixada para "estimamos o quanto" se a validação preditiva falhar.

## 3. Arquitetura do argumento

1. P1 (problema): a manutenção predial das IFES é predominantemente corretiva, com registros fragmentados e controle externo recorrente sobre planos e estudos técnicos (T8 e contexto brasileiro; pré-projeto).
2. P2 (necessidade): gestores precisam ordenar onde intervir com recursos escassos, e os instrumentos de ODS para universidades não usam a manutenção como evidência (T3).
3. P3 (limite dos métodos atuais): a priorização por MCDA costuma apresentar ordenação pontual com pesos e normalização fixos, sem incerteza nem validação além da de face (T1, T4, T5).
4. P4 (mecanismos de distorção): escala, propensão a reportar e erro de classificação alteram os dados de base (T6 e achados desta auditoria).
5. P5 (método): construir um índice com critérios de validade de conteúdo, normalização por exposição, pesos elicitados ou incertos (SMAA), incerteza conjunta e validação cronológica (T4, T5, T7).
6. P6 (resultado hipotético a demonstrar): [medida de quanto cada fonte desloca os postos; aceitabilidade de postos; correlação preditiva].
7. P7 (implicação): o gestor pode usar posições robustas para ETP e TR e tratar posições instáveis como zona de decisão que exige mais dados.
8. Conclusão: a priorização sob incerteza, com dados administrativos auditados, é mais informativa e mais defensável que um ranking pontual.

## 4. Esboço da introdução em quatro movimentos (sem resultados)

1. Problema público: manutenção predial em universidades federais, evidência de fragilidades e de controle externo, escassez de recursos.
2. Necessidade de medida: como ordenar onde intervir, e por que os instrumentos existentes de ODS em universidades não resolvem (R26, R27, R31).
3. Estado da arte e lacuna: priorização por MCDA em campi e edificações, com casos isolados e sem incerteza nem validação preditiva; indicadores compostos exigem robustez (R01, R02, R05); registros administrativos têm vieses (R44).
4. Contribuição e roteiro: perguntas P1 a P5 do desenho do estudo, contribuições C1 a C4 e estrutura do texto.

## 5. Elementos que elevam a competitividade em primeiro estrato

1. Pré-registro do protocolo e do plano de análise, com regra para resultados negativos.
2. Pacote de replicação com dado agregado congelado e um comando que gera tabelas e figuras.
3. Decomposição da incerteza por fonte (quantificação inédita no contexto, se a revisão confirmar).
4. Validação preditiva com origem móvel e comparadores simples.
5. Painel de especialistas multicampi e uma instituição externa.
6. Declaração explícita do conflito de interesses e protocolo de extração de dados auditável.
7. Figuras de padrão editorial (aceitabilidade de postos, deslocamento de postos, mapa de qualidade) e resumo gráfico.
8. Discussão voltada a decisão pública (ETP, TR, prestação de contas), com limites claros.

## 6. Riscos e planos alternativos

1. Se a validação preditiva for fraca: reposicionar para o conceito A, com ênfase em robustez e em incerteza.
2. Se o painel de especialistas não puder ser formado: usar SMAA com pesos incertos e reportar sensibilidade a esquemas de pesos objetivos.
3. Se faltarem datas de solução e prioridade nativa: manter o conjunto mínimo de critérios e declarar a limitação.
4. Se a classificação por sistema for imprecisa: reduzir ao painel campus e ano.
5. Se a revisão sistemática encontrar trabalho que ocupe a lacuna: ajustar a contribuição para a combinação (decomposição de incerteza com validação preditiva em manutenção universitária).

## 7. Pergunta final e título provisório

Pergunta: quanto da ordem de prioridade de manutenção em uma universidade multicampi é explicada por escolhas de escala, de notificação, de classificação, de pesos e de método, e a prioridade robusta antecipa a demanda e o custo corretivo do período seguinte?
Título provisório: Priorização de manutenção predial em universidade federal multicampi sob incerteza: índice alinhado aos ODS, robustez dos postos e validade preditiva.
