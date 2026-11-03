# Parecer crítico do manuscrito (como avaliador de periódico de primeiro estrato)

Objeto: `docs/ARTIGO_MALHA_ODS_ESG.md` (versão de 20/06/2026, 3.230 palavras) e `docs/ARTIGO_SECAO_3_MATERIAIS_METODOS.md`, avaliados contra os dados e o código do repositório em 03/11/2026. Critério de avaliação: o padrão esperado de um periódico internacional de primeiro estrato em ambiente construído e sustentabilidade ou em ciência da decisão (equivalente ao estrato A1 do Qualis, cuja classificação vigente deve ser conferida na Plataforma Sucupira). O parecer é deliberadamente exigente: o objetivo é indicar o que um revisor atacaria e o que precisa existir para o artigo resistir a esse ataque. As referências a números usam as execuções documentadas em `docs/PLANO_ARTIGO_ODS_ESG.md` e `docs/auditoria/dados/auditoria_base.json`.

## 1. Síntese do manuscrito

O texto propõe um modelo auditável de apoio multicritério à decisão para manutenção predial universitária, que transforma chamados de manutenção da UFSB em dez indicadores por campus, os mapeia por proxy aos ODS 9, 11 e 12 e aos pilares ESG, normaliza por mínimo e máximo, pondera por pesos operacionais editáveis e ordena os campi por soma ponderada e por TOPSIS. Os resultados apresentam um ranking de cinco unidades (uma delas com cinco ou onze chamados) e observam que soma ponderada e TOPSIS divergem no topo. A conclusão afirma que a contribuição transferível é o método auditável e não os valores obtidos.

## 2. Recomendação

Recomendação como se o manuscrito fosse submetido hoje a um periódico de primeiro estrato: rejeição editorial na triagem, com convite a ressubmissão após reformulação substancial. A decisão não se deve à redação, que é cuidadosa quanto a limites, e sim à ausência dos três elementos que sustentam um artigo desse tipo: contribuição teórica ou metodológica demonstrável, validação do instrumento e evidência empírica com poder inferencial. O caminho para torná-lo submetível existe e é viável com os dados disponíveis e com um conjunto delimitado de dados novos; está desenhado em `03_DESENHO_DO_ESTUDO_A1.md`.

## 3. Avaliação por critério

| Critério | Nota (1 a 5) | Fundamento |
|---|---|---|
| Originalidade e lacuna | 2 | A lacuna é afirmada ("escassa consolidação"), não demonstrada; a revisão da literatura tem 7 referências e não cobre indicadores de ODS em universidades, MCDM com incerteza, nem manutenção predial universitária |
| Relevância e contribuição | 2 | O tema é relevante para a gestão pública; a contribuição declarada (método auditável) é de engenharia de software e governança, não de método de decisão ou de medição |
| Validade de construto | 1 | Os indicadores medem demanda operacional por proxy textual; a definição de "infraestrutura crítica" é por especialidade técnica e a de "espaço coletivo" é busca de palavras no título |
| Rigor metodológico | 2 | Pesos sem proveniência, normalização que inverte o ranking quando se divide por área, agregação com dupla contagem, nenhuma incerteza propagada |
| Validação | 1 | Não há validação interna, convergente nem preditiva; a comparação entre dois métodos de agregação é apresentada como validação interna |
| Dados e qualidade | 2 | Snapshot incremental, cruzamento transversal, 40,6% dos chamados classificados com baixa confiança, defeitos de leitura de coluna e de razão preventiva |
| Reprodutibilidade | 2 | Artefatos versionados e públicos (ponto forte), porém os números do texto não são reproduzíveis com o snapshot atual e a lógica de pontuação existe apenas no HTML |
| Ética e conformidade | 2 | Sem declaração de ética, de dados pessoais (LGPD), de disponibilidade de dados nem de conflito de interesses |
| Redação e apresentação | 3 | Prosa clara e honesta quanto a limites; falta resumo, seção 2 está em tópicos, não há tabela nem figura, e há repetição de fórmulas de ressalva |

## 4. Objeções maiores

### M1. A lacuna e a contribuição não estão estabelecidas

A introdução afirma "escassa consolidação de uma trilha que conecte, de forma auditável, o chamado individual ao indicador agregado por campus" e sustenta a afirmação com sete referências, quatro delas metodológicas gerais. Um revisor responderá que existem literaturas amplas e consolidadas sobre (a) indicadores de sustentabilidade e dos ODS em instituições de ensino superior, (b) construção de indicadores compostos (OECD e JRC, 2008), (c) MCDM com análise de incerteza (SMAA e simulação de Monte Carlo) e (d) gestão de facilities em campi. O texto não dialoga com nenhuma delas. A rastreabilidade, por si, não é contribuição científica de periódico de primeiro estrato: precisa ser acompanhada de um resultado que a ausência de rastreabilidade impediria. É necessário reformular a pergunta de pesquisa em torno de algo testável (por exemplo, em que medida a priorização de manutenção muda quando se corrigem escala, incerteza de pesos e erro de classificação) e construir a revisão de literatura que identifique, com busca documentada, a lacuna real.

### M2. Validade de construto dos indicadores

1. `N_infra_critica` (4.457 chamados, 30,6% da base) conta toda categoria cujo texto contém "elétric", "hidráulic", "telhado" e similares, o que inclui troca de iluminação (855), quadros elétricos preventivos (652) e instalações elétricas em geral (997). Mede especialidade técnica, não criticidade, e é fortemente colinear com o volume total.
2. `N_em_espaco_coletivo` é a contagem de chamados cujo título contém uma de dez expressões ("sala de aula", "corredor", "estacionamento"); o título é texto livre, a sensibilidade e a especificidade da regra não foram medidas, e o indicador é tratado como "contextual" com ótimo em 0,5 do intervalo normalizado, o que não tem justificativa.
3. `N_chamados_total` com sentido "minimizar" supõe que mais chamados significam pior desempenho; o volume reflete também propensão a reportar, canais de abertura e tamanho da comunidade usuária. Sem normalização por usuários ou área e sem controle de subnotificação, a direção de preferência é contestável.
4. `Valor_total_gasto_R$` não é custo de manutenção: é a soma do valor das ordens de serviço, presentes em 16,5% dos chamados, e de 50% a 61% desse valor em cada campus pertence a 93 chamados de contratação de "Posto de trabalho".
5. O mapeamento aos ODS é "interpretativo" e não faz referência a metas e indicadores oficiais da Agenda 2030 (por exemplo, às metas 9.1, 11.6, 12.2, 12.5 e 12.7, cujo texto oficial deve ser conferido). Um revisor da área de ODS exigirá o vínculo indicador, meta e fundamento normativo ou teórico, com avaliação de validade de conteúdo por especialistas.

### M3. Unidade de análise e tamanho amostral

Há quatro alternativas efetivas (Jorge Amado, Paulo Freire, Sosígenes Costa e Reitoria) mais uma de 11 chamados registrados apenas em 2026. Um ranking de quatro unidades em corte transversal não permite inferência, e a correlação de postos entre dois métodos com n igual a 4 ou 5 tem amplitude de valores possíveis tão discreta que não discrimina concordância de acaso. O artigo precisa de uma unidade de análise com mais observações. O desenho recomendado usa o par campus e sistema técnico como alternativa de decisão (cerca de 24 alternativas por período) e o painel campus por ano para avaliação temporal.

### M4. Escala e normalização

Contagens e gasto absolutos refletem o porte do campus. Ao dividir contagens e gasto por 1.000 m2 de área de utilização (patrimônio, 2025), o ranking se inverte (a Reitoria passa à última posição e Sosígenes Costa e Jorge Amado sobem). Esse resultado, reproduzido em `scripts/diagnostico/mcdm_sensibilidade.py`, mostra que a conclusão substantiva do ranking depende de uma escolha de normalização que o texto reconhece como "latente". A normalização min–max sobre quatro ou cinco pontos é, além disso, sensível à presença de uma unidade extrema (efeito que o próprio texto observa com Maria Felipa) e provoca inversão de ranking quando o conjunto de alternativas muda.

### M5. Pesos sem proveniência

Os pesos de `pesos_ods.json`, `classificacao_ods_esg.json`, `pesos_categorias_ods_esg.json` e `multiplicadores_importancia_chamado.json` (por exemplo 0,30, 0,35 e multiplicadores de 0,85) são atribuídos pelo pesquisador sem fundamentação, consulta a especialistas ou comparação com esquemas alternativos. A afirmação de "leitura compatível com AHP" não tem conteúdo, porque AHP é um procedimento de elicitação, não uma propriedade de um vetor de pesos. O pré-projeto promete AHP-TOPSIS; o manuscrito declara que não o aplicou. Para primeiro estrato, é necessário elicitar pesos formalmente (AHP ou Best-Worst Method) com painel de especialistas e razão de consistência, ou assumir explicitamente incerteza total nos pesos e reportar resultados em termos de aceitabilidade de postos (SMAA).

### M6. Agregação, compensação e dupla contagem

O mesmo indicador entra nos três ODS com pesos diferentes, e o escore geral é a média aritmética simples dos três ODS, de modo que os critérios com maior soma de pesos são contados mais de uma vez e o desempenho ruim em um ODS é compensado por bom desempenho em outro. O TOPSIS usa a soma dos pesos dos três ODS, perdendo a estrutura por ODS que a soma ponderada preserva; as duas leituras partem, portanto, de modelos diferentes e sua discordância (correlações de postos de 0,3, -0,4, -0,2 e 0,4 nos quatro cenários) não pode ser interpretada como "validação interna", como o texto afirma na Discussão. Os ODS são objetivos não substituíveis; uma agregação parcialmente compensatória ou não compensatória (por exemplo, PROMETHEE II, ELECTRE III ou agregação geométrica) e a apresentação do perfil por ODS são mais defensáveis.

### M7. Ausência de validação e de incerteza

O manuscrito não apresenta (i) validade de conteúdo dos indicadores, (ii) validade convergente (concordância com uma priorização independente de especialistas ou com laudos de inspeção predial), (iii) validade preditiva (a priorização do período t antecipa maior demanda ou custo corretivo em t mais 1) nem (iv) análise de incerteza e sensibilidade. A análise de sensibilidade aparece como "recomendação" repetida em quatro seções e não é executada. No diagnóstico desta auditoria, perturbar cada peso entre 50% e 150% de seu valor quase não altera a primeira posição dentro de cada método, ou seja, a instabilidade está entre métodos e entre normalizações, dimensões que o texto não examina.

### M8. Qualidade e homogeneidade temporal dos dados

1. A classificação por IA, da qual derivam infraestrutura crítica, preventiva e corretiva, tem acurácia de 83,07% contra referência humana no artigo de classificação, e 40,6% dos chamados (5.921 de 14.580) foram classificados com a etiqueta de baixa confiança; essa fração é inferior a 6% de 2018 a 2020 nos quatro campi principais, sobe a 28% a 48% em 2021 e fica entre 50% e 80% de 2022 em diante, o que indica mudança de regime do classificador (ou dos dados) ao longo do tempo. O erro de classificação não é propagado aos indicadores.
2. A criticidade "Alta" oscila entre zero e quatro ocorrências por campus ao ano de 2020 a 2025 e salta para 12 e 13 em 2026 nos campi Jorge Amado e Paulo Freire, comportamento compatível com alteração do critério de atribuição e não com mudança real da demanda.
3. A proporção de chamados com ordem de serviço difere entre campi em um fator de 2 a 3 (Paulo Freire entre 20% e 34% de 2020 a 2025; Jorge Amado entre 9% e 19%), o que evidencia práticas de registro diferentes e invalida a comparação direta de indicadores baseados em OS.
4. A base tem 69,9% de linhas vazias, 15 colunas sem nome e vazias, categoria histórica e categoria de IA coincidem em 36,6% dos chamados (comparação textual exata, afetada por diferenças de taxonomia), e três regimes de uso do sistema (adoção em 2015 a 2017, queda em 2020, recuperação).

### M9. O cálculo canônico não está no código nem no snapshot

A pontuação por soma ponderada e TOPSIS existe apenas em JavaScript no `dashboard.html`; `motor_ods.py` gera indicadores brutos. O snapshot publicado traz a razão preventiva como contagem (925, 1.295, 1.637, 550 e 4), enquanto o texto reporta proporções de 0,26 a 0,34; a criticidade é lida em coluna inexistente (índice 30 em vez de 29), o que anula `N_criticos_alta` embora existam 149 chamados de criticidade alta; a área por campus é um stub que devolve dicionário vazio, embora a área exista no patrimônio. Os números da seção de resultados (que citam 4.080, 3.740, 3.684, 2.363 e 5 chamados) não coincidem com o snapshot atual (4.245, 3.946, 3.924, 2.454 e 11) e não podem ser reproduzidos. Um periódico de primeiro estrato exige pacote de replicação congelado (dados, código, ambiente) com identificador persistente.

### M10. Ética, privacidade e conflito de interesses

Não há declaração sobre dados pessoais (os chamados contêm texto livre e podem conter nomes, locais e telefones; o repositório público deve conter somente agregados), sobre a necessidade de apreciação por comitê de ética para a consulta a especialistas (a ser verificada com o CEP da UFSB), nem sobre o conflito de interesses de o autor administrar o sistema de chamados e ser servidor da instituição avaliada. Também faltam declarações de disponibilidade de dados, de contribuição dos autores e de uso de ferramentas de IA.

### M11. Ambiguidade entre desempenho e prioridade

O painel e o texto tratam o escore como desempenho ODS/ESG, no qual menos chamados e menos gasto significam melhor posição. O pré-projeto, porém, descreve um instrumento de priorização de manutenção e de alocação de recursos, no qual maior demanda, maior criticidade e maior custo significam maior prioridade de intervenção. Os dois usos têm direções de preferência opostas para os mesmos indicadores e respondem a perguntas diferentes (quem vai melhor, contra onde investir primeiro). O manuscrito mistura as duas leituras ("ranking comparativo", "apoio à priorização", "desempenho"), o que impede definir o que significa a primeira posição. O estudo deve declarar um único objeto de medida (recomenda-se índice de prioridade de manutenção, coerente com o pré-projeto) e derivar a direção de cada critério dessa definição.

### M12. Redação

O texto é correto, mas apresenta traços que revisores associam a redação padronizada: fórmulas de ressalva repetidas ("Cabe ressaltar" duas vezes, "Constata-se" três vezes, "longe de fragilizar" duas vezes, "Diante disso" duas vezes), afirmações sobre a própria honestidade metodológica ("a honestidade quanto às lacunas ... não compromete a proposta") em lugar da demonstração, a seção 2 em tópicos, ausência de resumo e de palavras-chave, ausência de tabelas e figuras, e conclusão que reafirma limitações antes de dizer o que se encontrou. Para publicação internacional é indispensável versão em inglês de qualidade editorial.

## 5. Objeções menores

1. O título provisório ("Integração de dados patrimoniais...") promete integração patrimonial, mas a camada patrimonial não entra no escore.
2. A seção 4.5 afirma que a área por campus "não está materializada"; ela existe em `dados/patrimonio_imobiliario_campus_ano.json`.
3. O texto cita Saaty (2008) para AHP, mas não discute alternativas de elicitação (BWM, SMART) nem a literatura de comparação de métodos MCDM.
4. Não há definição operacional de "chamado classificado" (a base total tem 14.580 chamados com data).
5. A regra de quase-lacuna (valor dominante em N-1 das N unidades) é arbitrária com N igual a 5 e deve ser substituída por critério com justificativa estatística ou por ponderação por qualidade.
6. O indicador "contextual" (ótimo em 0,5) deve ser justificado ou removido.
7. O texto usa "snapshot" sem definir o congelamento (data, hash, commit do hub).
8. Faltam referências normativas citadas no pré-projeto (NBR 5674, NBR 14037, NBR ISO 41001) e a norma de inspeção predial, que fundamentariam a dimensão de governança.
9. O dashboard não é descrito como produto do estudo nem avaliado quanto a usabilidade; se for contribuição, precisa de avaliação.

## 6. Auditoria de afirmações (afirmação, evidência, avaliação)

| Afirmação do manuscrito | Evidência disponível | Avaliação |
|---|---|---|
| "A comparação entre ambas constitui, em si, um elemento de validação interna" (Discussão) | Spearman entre métodos de 0,3 a -0,4 nos cenários reproduzidos | Não sustentada: concordância entre agregadores não valida o construto, e a concordância observada é baixa |
| "Maria Felipa lidera a soma ponderada por artefato de escala" | Reproduzido (53,9) | Sustentada, mas a consequência (excluir a unidade) é tratada só em recomendação |
| "A área construída por campus não estava materializada" | Existe em `patrimonio_imobiliario_campus_ano.json` | Contraditada pelos dados do próprio repositório |
| "Ambas as correções foram replicadas no hub e os snapshots regenerados" | Snapshot atual traz contagem, não razão | Não reproduzida; causa não determinada |
| "Razão preventiva entre 0,26 e 0,34 nos campi regulares" | Recalculada hoje: 0,224 a 0,386 | Desatualizada (base incremental e reclassificação) |
| "A ausência de data de conclusão impede tempo e prazo" | A coluna de conclusão não está no JSON; o GLPI padrão registra datas de solução e de fechamento | Parcialmente sustentada: a lacuna é de extração, não de existência do dado (a confirmar) |
| "O instrumento não substitui o julgamento do gestor" | Declaração de escopo | Adequada, mas sem estudo de uso por gestores |
| "Nenhum impacto causal é afirmado" | Declaração de escopo | Adequada |

## 7. O que mudaria a recomendação

1. Uma pergunta de pesquisa testável e uma lacuna demonstrada por busca sistemática documentada.
2. Indicadores com validade de conteúdo avaliada por painel de especialistas e vinculados a metas oficiais dos ODS.
3. Unidade de análise com número suficiente de observações (campus e sistema, por período) e normalização por escala.
4. Pesos elicitados formalmente ou incerteza total de pesos tratada por SMAA, com análise de sensibilidade global executada.
5. Validação convergente (priorização independente de especialistas) e preditiva (priorização em t versus demanda e custo corretivo em t mais 1).
6. Tratamento explícito do erro e da baixa confiança de classificação.
7. Pacote de replicação congelado, com identificador persistente, e cálculo canônico em código versionado.
8. Declarações de ética, de dados, de conflito de interesses e de uso de IA, e versão em inglês de qualidade editorial.
