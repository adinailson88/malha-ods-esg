# Desenho do estudo para um artigo de primeiro estrato

Este documento propõe o que fazer e como fazer para transformar o eixo ODS/ESG em um artigo submetível a periódico internacional de primeiro estrato, com base no pré-projeto de doutorado (objetivo específico 5, atividade 7, resultados esperados) e nos dados que já existem. Cada decisão aponta para o dado necessário (`04_MATRIZ_DADOS.md`) e para a etapa de execução (`06_PLANO_DE_EXECUCAO.md`). Os limiares numéricos são propostas a calibrar e devem ser fixados em protocolo antes da análise (seção 14). Metas dos ODS são citadas em paráfrase e o texto oficial da Agenda 2030 deve ser conferido antes da submissão.

## 1. Tese central do artigo

Não se propõe mais um ranking de campi, e sim um instrumento de priorização de manutenção predial universitária com três propriedades demonstradas empiricamente: (i) indicadores com validade de conteúdo vinculados a metas dos ODS 9, 11 e 12; (ii) resultado robusto, ou com robustez quantificada, às escolhas de escala, de pesos, de método, de unidades e de erro de classificação; (iii) capacidade de antecipar demanda e custo corretivo do período seguinte, de forma melhor que uma referência simples. A contribuição é metodológica e aplicada: mostrar, com dados reais de uma universidade federal multicampi, o quanto as conclusões de priorização mudam quando as incertezas hoje ignoradas são tratadas, e oferecer um procedimento replicável para fazê-lo.

Contribuições que o texto poderá reivindicar, em ordem de força esperada: C1, um procedimento de construção e validação de índice de prioridade de manutenção alinhado aos ODS, com quantificação de incerteza (SMAA) e validade preditiva; C2, evidência empírica de que a normalização por escala e o erro de classificação alteram a priorização (resultado já visível nos dados atuais); C3, um protocolo de dados e de rastreabilidade (cadeia chamado, indicador, critério, decisão) com pacote de replicação; C4, integração de previsões de demanda e de custo (Artigos 2 e 3) em cenários de prioridade. C1 e C2 sustentam o artigo; C3 e C4 reforçam e dependem dos demais eixos.

## 2. Objeto de medida: prioridade e não desempenho

Define-se o objeto como índice de prioridade de manutenção (necessidade relativa de atenção de gestão), em que maior demanda por exposição, maior criticidade, maior custo corrente e pior tempo de resposta elevam a prioridade. Essa definição é coerente com o pré-projeto (apoio à alocação de recursos e à instrução de ETP e TR), elimina a ambiguidade de direção apontada no parecer (M11) e permite ler a primeira posição como "onde intervir primeiro". Os ODS entram como estrutura de critérios e de leitura (perfil por ODS), não como certificação de desempenho. Os pilares ESG são mantidos como lente de classificação dos critérios, sem pontuação própria, para evitar a dupla contagem.

## 3. Perguntas e hipóteses

1. P1 (validade de conteúdo): quais indicadores operacionais, derivados de dados de manutenção, representam de forma relevante e suficiente os construtos de infraestrutura confiável (ODS 9), espaços seguros e de uso contínuo (ODS 11) e uso responsável de recursos (ODS 12) em uma universidade pública? Hipótese: um subconjunto de indicadores obtém índice de validade de conteúdo igual ou superior a um limiar a definir (proposta: 0,78 ou mais com seis ou mais especialistas, valor usual na literatura de validade de conteúdo, a conferir).
2. P2 (efeito da escala): a prioridade relativa dos pares campus e sistema muda quando contagens e custo são normalizados por área e por usuários? Hipótese: sim, com correlação de postos entre as versões bruta e normalizada abaixo de 0,7 (resultado preliminar com quatro campi: inversão do ranking).
3. P3 (robustez): quão estável é a ordenação sob incerteza conjunta de pesos, normalização, método de agregação, conjunto de unidades e erro de classificação? Hipótese: as posições extremas (maior e menor prioridade) são estáveis (aceitabilidade de posto acima de 0,6) e as intermediárias não são.
4. P4 (validade preditiva): a prioridade do ano t antecipa demanda e custo corretivo por exposição em t mais 1 melhor que (a) a demanda do ano t sozinha e (b) uma ordenação aleatória? Hipótese: a prioridade composta tem correlação de postos com o resultado seguinte superior à de cada indicador isolado.
5. P5 (cenários): a incorporação de previsões de demanda e custo (Artigos 2 e 3) altera a ordem de prioridade do próximo ciclo? Depende dos Artigos 2 e 3; é componente opcional do primeiro artigo e pode ser deslocado para um segundo.

## 4. Unidade de análise, janela e amostra

1. Alternativas de decisão: pares campus e sistema técnico (quatro campi principais por seis a oito sistemas, de acordo com as famílias da taxonomia: elétrica, hidrossanitária, climatização, estrutura predial, TI e rede, segurança contra incêndio, instalação de acessórios, outros), o que dá de 24 a 32 alternativas por período. Maria Felipa (11 chamados, 2026) e Reitoria (sem área de campus comparável) entram em análise de sensibilidade, não no conjunto principal.
2. Janela: 2018 a 2025 (oito anos completos), com 2026 parcial para validação externa e para previsão. Os anos de 2015 a 2017 (adoção do sistema) ficam fora; 2020 é sinalizado como choque.
3. Painel: campus, sistema e ano, com 4 campi, 6 a 8 sistemas e 8 anos (192 a 256 observações), o que permite avaliar tendência e validade preditiva. O limite é a classificação por sistema, que depende da categoria (histórica ou por IA) e do seu erro.
4. Painel mínimo alternativo, se a classificação por sistema se mostrar insuficiente: campus e ano (32 observações), com ênfase na robustez e na validação preditiva por campus.

## 5. Quadro conceitual e critérios

Quadro conceitual: o campus como biossistema construído (componentes físico, humano, tecnológico e ambiental, conforme o pré-projeto) cujo estado é observado por registros de manutenção. Critérios agrupados por dimensão ODS; a atribuição de cada critério a uma meta é hipótese a validar pelo painel de especialistas.

| Critério (direção na prioridade) | Construto | Meta ODS indicativa | Definição operacional | Fonte | Situação |
|---|---|---|---|---|---|
| C1 Demanda por exposição (mais demanda, mais prioridade) | pressão sobre a infraestrutura | 9.1 | chamados por 1.000 m2 de área construída, por sistema e campus (área só existe por campus) | chamados e patrimônio | área por campus disponível; demanda disponível |
| C2 Severidade (mais severo, mais prioridade) | risco à continuidade e à segurança | 9.1, 11.7 | proporção de chamados de prioridade alta nativa do GLPI ou de sistemas essenciais definidos por especialistas | GLPI; painel de especialistas | prioridade nativa a extrair; criticidade por IA instável |
| C3 Tempo de resposta (pior, mais prioridade) | resiliência operacional | 9.1 | mediana e percentil 90 do tempo entre abertura e solução; aderência a meta de SLA | GLPI (datas de solução e fechamento) | dado a extrair |
| C4 Reincidência (maior, mais prioridade) | retrabalho e falha de causa raiz | 12.2 | proporção de chamados repetidos no mesmo local ou ativo em janela fixa | GLPI (localização, ativo) | dado a extrair |
| C5 Custo corrente por exposição (maior, mais prioridade) | pressão orçamentária | 12.2, 12.7 | valor de OS corrente (sem contratação), deflacionado, por 1.000 m2 | chamados (coluna de valor) e índice de preços | disponível, com ressalvas |
| C6 Razão corretiva (maior, mais prioridade) | maturidade da gestão | 12.2 | proporção de chamados corretivos entre os chamados do sistema | plano de manutenção e chamados | requer marcação explícita |
| C7 Tendência (crescente, mais prioridade) | trajetória | 9.1 | inclinação robusta da demanda por exposição em três anos | chamados | disponível |
| C8 Uso e segurança de espaços coletivos (mais exposição, mais prioridade) | exposição de usuários | 11.7 | proporção de chamados em espaços de uso coletivo, por localização estruturada | GLPI (localização) | requer localização |
| C9 Usuários por área (mais, mais prioridade) | densidade de ocupação | 11.7 | estudantes, docentes e técnicos por 1.000 m2 | registros acadêmicos e de pessoal | dado a obter |
| C10 Demanda e custo previstos (maiores, mais prioridade) | antecipação | 9.1, 12.2 | previsões a 12 meses dos Artigos 2 e 3 | modelos dos Artigos 2 e 3 | dependente dos outros artigos |
| C11 Consumo de energia e água por área (maior, mais prioridade) | eficiência de recursos | 12.2 | kWh e m3 por 1.000 m2 | faturas e contratos de concessionárias | dado a obter (opcional) |

O conjunto mínimo para um primeiro artigo é C1, C2, C3, C5, C6 e C7, que combinam dados existentes e dois dados a extrair do GLPI (datas de solução e prioridade nativa). C4, C8, C9, C10 e C11 são extensões que elevam o valor, mas não são condição de submissão.

## 6. Qualidade dos dados e erro de classificação

1. Tratar a baixa confiança da classificação: reportar todos os indicadores em duas versões (todos os chamados e apenas chamados de confiança alta ou média) e testar a diferença; usar a categoria histórica como comparador.
2. Propagar o erro: usar a matriz de confusão do artigo de classificação (83,07% de acurácia contra referência humana) para simular reclassificação (amostragem de rótulos verdadeiros plausíveis dado o rótulo da IA e a confiança) e medir a variação dos índices e do ranking.
3. Corrigir as quebras de regime: incluir indicador de regime do classificador (confiança baixa antes e depois de 2021) e usar apenas indicadores por proporção estável ou ajustados por regime; documentar a mudança de criticidade de 2026.
4. OS e valor: tratar o valor como custo de OS (não como custo total), registrar a taxa de OS por campus e ano como indicador de qualidade de registro, separar contratação de "Posto de trabalho", deflacionar por índice de preços da construção ou do consumo (escolha do autor, com fonte oficial a verificar).
5. Dado ausente versus zero: distinguir zero verdadeiro de ausência de registro (protocolo de Zuur já adotado); imputar apenas com regra documentada e testar a sensibilidade.

## 7. Normalização

Comparar, no mesmo conjunto de dados, (a) mínimo e máximo, (b) padronização por escore z robusto (mediana e MAD), (c) posto, (d) distância a metas de referência quando houver meta normativa ou de especialistas, e (e) normalização por exposição (área e usuários) antes de qualquer das anteriores. A normalização por exposição é obrigatória nas versões principais, porque a raiz da distorção atual é de escala. A versão principal deve usar referência fixa (metas ou percentis de uma janela de referência) e não o mínimo e máximo do conjunto do período, para evitar inversão de ranking por inclusão de unidades e permitir comparação entre anos.

## 8. Pesos

1. Esquemas: iguais; entropia ou CRITIC (objetivos, derivados dos dados); elicitação por especialistas (AHP ou Best-Worst Method). O pré-projeto promete AHP; recomenda-se AHP para manter a coerência, com BWM como alternativa se o número de critérios tornar a matriz pareada cansativa (BWM exige menos comparações).
2. Painel de especialistas: de 8 a 15 profissionais com experiência em manutenção predial e gestão de contratos em IFES (gestores de infraestrutura e de contratos, engenheiros e arquitetos, fiscais de contrato, membros de comissões de planejamento), de pelo menos dois campi e de uma instituição externa para a validação cruzada. Os números são proposta; a literatura de AHP aceita painéis pequenos desde que homogêneos em competência.
3. Instrumento: questionário eletrônico com comparações pareadas (escala de 1 a 9), cálculo do autovetor, razão de consistência por respondente (aceitar abaixo de 0,10 ou reconduzir a resposta) e agregação por média geométrica dos julgamentos individuais (AIJ) ou prioridades individuais (AIP) com análise de dispersão. Inclui também o instrumento de validade de conteúdo dos indicadores (relevância e clareza em escala de 4 pontos) aplicado ao mesmo painel.
4. Produto: vetor de pesos com intervalo (por reamostragem de especialistas), registrado com proveniência em tabela versionada (quem, quando, instrumento, versão).
5. Verificação da necessidade de apreciação ética antes da coleta (ver seção 15).

## 9. Agregação e métodos

1. Método principal: soma ponderada normalizada por ODS, que preserva o perfil por ODS, mais um método de outranking (PROMETHEE II) com limiares de indiferença e de preferência fixados por especialistas, que lida melhor com compensação parcial; TOPSIS permanece como comparador, com a ressalva de sua sensibilidade a inversão de ranking. A escolha final de método principal deve resultar da análise de robustez e não de preferência a priori, e deve ser declarada no protocolo.
2. Evitar a dupla contagem: cada critério pertence a um único ODS principal (atribuição por especialistas); associações secundárias são apenas informativas.
3. Apresentar o perfil por ODS (três escores) e o índice global, com o aviso de compensação, e reportar o índice global também por agregação geométrica como verificação de não compensação.

## 10. Incerteza e sensibilidade

Seguir a estrutura de construção de indicadores compostos da OECD e do Centro Comum de Pesquisa da Comissão Europeia (2008) e a literatura de análise de incerteza e sensibilidade de indicadores compostos (a conferir: Saisana, Saltelli e Tarantola, 2005), com:

1. Análise de incerteza conjunta por Monte Carlo (5.000 a 10.000 simulações), amostrando simultaneamente pesos (da distribuição de especialistas), normalização, método de agregação, conjunto de unidades e reclassificação por erro de IA.
2. Análise de aceitabilidade estocástica (SMAA-2, Lahdelma e Salminen, 2001, DOI 10.1287/opre.49.3.444.11220) com índices de aceitabilidade de postos, vetores centrais de pesos e fator de confiança, adequada a poucas alternativas e a pesos incertos.
3. Métricas de estabilidade: correlação de postos (Spearman e Kendall) entre cenários, sobreposição das k primeiras posições, deslocamento médio de posto e probabilidade de cada alternativa ocupar o primeiro e o último quartil.
4. Decomposição da incerteza por fonte (qual das cinco escolhas explica mais do deslocamento de postos), em lugar de apenas variar pesos, que é o único eixo que o painel atual cobre.
5. Apresentação: gráfico de aceitabilidade de postos empilhado, gráfico de inclinação (bump chart) entre cenários e tabela de posições robustas.

## 11. Validação

1. Conteúdo: índice de validade de conteúdo por indicador e por escala (seção 3, P1), com revisão iterativa estilo Delphi de duas rodadas se a concordância for baixa.
2. Convergente: painel de especialistas (ou parte dele, sem acesso aos escores) ordena às cegas um subconjunto de pares campus e sistema; compara-se com o índice por correlação de postos e concordância nos extremos. Quando existirem laudos de inspeção predial (a norma brasileira de inspeção predial, ABNT NBR 16747, deve ser conferida), usá-los como referência independente de condição.
3. Preditiva: validação cronológica com origem móvel (ordenação em t, resultado em t mais 1) em demanda por exposição e custo corretivo por exposição; comparar com referências simples (demanda do ano anterior, média histórica) por correlação de postos, precisão nos k primeiros e erro de ranqueamento; evitar vazamento (indicadores de t calculados sem usar o resultado de t mais 1 e sem a classificação reajustada com dados futuros).
4. De face e de uso: apresentação a gestores e coleta estruturada de percepção de utilidade (opcional, depende de ética).
5. Replicação interna: refazer o índice em um segundo recorte temporal e em um segundo conjunto de especialistas.

## 12. Integração com previsões (Artigos 2 e 3) e análise espacial

1. Previsão de demanda por campus e sistema (Artigo 2) e de custo (Artigo 3) entram como C10, em cenários que mantêm separadas as quantidades observadas e as previstas, com propagação do intervalo preditivo à incerteza do índice. Dependem da correção de datas (já mergeada no hub), de reexecução e das covariáveis reais por campus.
2. Camada espacial (QGIS ou Google Earth Engine): mapa de prioridade por campus com as coordenadas do patrimônio; é produto complementar do pré-projeto e não condição do primeiro artigo.

## 13. Modelo de dados do painel

Tabela `painel_prioridade` (uma linha por campus, sistema e ano): identificadores; área construída do campus e do ano; usuários do campus e do ano; contagens de chamados por classe de confiança; contagem de OS e valor corrente e de contratação; tempos de resolução (mediana e p90); contagem de reincidências; proporção corretiva; sinalizadores de qualidade (taxa de OS, fração de baixa confiança, regime do classificador); versão do dado e do código. O pipeline deve gerar a tabela por script versionado a partir do dado congelado e registrar o hash.

## 14. Protocolo e pré-registro

Antes de executar a análise principal, redigir e registrar (por exemplo, em plataforma de pré-registro aberta, cuja escolha é do autor) o protocolo com: perguntas e hipóteses, definições operacionais, critérios de inclusão e de exclusão, esquemas de normalização, pesos e métodos, plano de sensibilidade, métricas de validação, limiares de aceitação e regra de decisão para resultados negativos. O pré-registro protege o estudo da crítica de flexibilidade analítica, que é decisiva em índices compostos.

## 15. Ética e conformidade

1. Dados pessoais: usar apenas agregados e campos estruturados; remover ou não publicar texto livre (título e descrição), que pode conter nomes, locais sensíveis e telefones; avaliar a conformidade com a Lei 13.709/2018 (LGPD) com o encarregado de dados da instituição.
2. Participantes: a consulta a especialistas pode exigir apreciação pelo comitê de ética em pesquisa; verificar com o CEP da UFSB o enquadramento (a necessidade não foi verificada), obter termo de consentimento e anonimizar respostas.
3. Conflito de interesses: declarar que o autor administra o sistema de chamados e é servidor da instituição estudada; mitigar com protocolo pré-registrado e com extração de dados por terceiro quando possível.
4. Autorização institucional para uso dos dados e para publicação de agregados por unidade.

## 16. Ameaças à validade e mitigação

| Ameaça | Natureza | Mitigação |
|---|---|---|
| Indicadores medem propensão a reportar | construto | normalização por exposição; validade de conteúdo; indicadores de qualidade de registro |
| Quebra de regime do classificador | interna | indicador de regime; versões por confiança; simulação de erro |
| Poucas alternativas e período curto | estatística | painel campus e sistema e ano; SMAA; reportar incerteza em vez de ponto |
| Pesos de especialistas locais | externa e construto | painel multicampi e externo; intervalo de pesos; esquemas objetivos como comparador |
| Flexibilidade analítica | estatística | pré-registro; relatório completo de cenários |
| Dado extraído de sistema administrativo dinâmico | reprodutibilidade | congelamento, hash, release com DOI |
| Estudo em uma instituição | externa | descrever o procedimento como replicável; piloto em segunda instituição como trabalho futuro |
| Conflito de interesses | ética | declaração, protocolo e auditoria externa dos dados extraídos |
| Dependência de Artigos 2 e 3 | cronograma | tornar C10 opcional no primeiro artigo |

## 17. Replicação e ciência aberta

Release versionado com dado agregado congelado, dicionário de dados, scripts de construção do painel, de pesos, de sensibilidade e de figuras, ambiente (versão do Python e dos pacotes), protocolo pré-registrado e resultados intermediários; arquivamento com identificador persistente; licenças explícitas; declaração de disponibilidade de dados. Os dados brutos permanecem no hub e só agregados são publicados.

## 18. Critérios de aceite do estudo (propostas)

1. Validade de conteúdo: pelo menos seis indicadores com índice de validade de conteúdo acima do limiar acordado.
2. Consistência: razão de consistência individual abaixo de 0,10 em pelo menos 80% dos especialistas após uma rodada de reconsideração.
3. Robustez: relatório de aceitabilidade de postos com decomposição por fonte de incerteza.
4. Validade preditiva: correlação de postos entre a prioridade em t e o resultado em t mais 1 estatisticamente superior à de cada indicador isolado, com intervalo por reamostragem em blocos.
5. Reprodutibilidade: reconstrução integral de tabelas e figuras por um único comando a partir do dado congelado.
Se os critérios 4 e 5 falharem, o artigo permanece publicável como estudo de robustez e de incerteza em priorização de manutenção, com ênfase em C2, sem afirmação de capacidade preditiva.
