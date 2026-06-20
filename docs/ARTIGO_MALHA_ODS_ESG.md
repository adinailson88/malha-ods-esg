# Artigo — Malha ODS/ESG (fonte canônica)

> **Fonte de verdade do artigo.** Este arquivo, versionado no repositório, é a versão
> canônica do manuscrito. O documento equivalente no Google Drive
> (`ARTIGO_MALHA_ODS_ESG_RASCUNHO`) é uma **republicação** desta fonte, pois o conector
> de Drive em uso não permite edição in-place. Última atualização: 2026-06-20.

> **Restrições assumidas:** (i) o ranking é comparativo dentro do snapshot, não é
> certificação oficial ODS/ESG; (ii) os pesos são operacionais e editáveis, com leitura
> compatível com AHP, mas não constituem AHP formal (sem matriz pareada nem razão de
> consistência); (iii) nenhum número do snapshot é fixado no método — valores vão para a
> seção de Resultados, sempre reconferidos por execução.

## Título provisório

Integração de dados patrimoniais e indicadores ODS/ESG para apoio multicritério à decisão
em manutenção predial universitária.

---

## 1. Introdução

As Instituições Federais de Ensino Superior constituem sistemas construídos complexos e
geograficamente dispersos, nos quais edificações acadêmicas, administrativas e de apoio
coexistem com redes prediais, usuários, custos e rotinas de manutenção que, em conjunto,
condicionam a continuidade do uso institucional dos espaços. A preservação da
funcionalidade dessas edificações depende de uma manutenção predial planejada, cuja
ausência tende a gerar deterioração de ativos, elevação de custos corretivos e riscos à
segurança da comunidade acadêmica. Neste contexto, a manutenção predial pública não se
restringe a uma rotina operacional, mas configura um dever de eficiência, economicidade e
conservação do patrimônio, sobretudo em universidades multicampi que administram
infraestrutura heterogênea com recursos orçamentários limitados.

Os registros de chamados de manutenção, embora tratados habitualmente como simples
expediente administrativo, constituem sinais operacionais do funcionamento desse sistema
construído. Cada chamado carrega informação sobre localização, criticidade, natureza
técnica, custo e recorrência, de modo que a sua organização sistemática permite converter
demanda dispersa em evidência estruturada para decisão. Tendo em vista a agenda de
sustentabilidade no ambiente construído, esses registros podem ser associados a objetivos
de infraestrutura resiliente, de qualidade e segurança dos espaços universitários e de uso
responsável de recursos, aproximando a gestão da manutenção das dimensões ambiental, social
e de governança. A literatura de apoio multicritério à decisão aplicada a facilities
demonstra a pertinência dessa abordagem para a gestão sustentável de edificações públicas
(KLUMBYTĖ et al., 2021; THEILIG et al., 2024), ao passo que os métodos de ordenação por
atributos múltiplos oferecem instrumentos consolidados para hierarquizar alternativas a
partir de critérios conflitantes (HWANG; YOON, 1981).

Persiste, contudo, uma lacuna operacional entre os campos que poderiam sustentar essa
integração. A literatura de manutenção predial pública evidencia o valor dos registros de
ordens de serviço para diagnóstico e eficiência; a literatura de sustentabilidade discute
indicadores ambientais, sociais e de governança no ambiente construído; e a literatura de
decisão multicritério formaliza a agregação de critérios, inclusive por meio de elicitação
estruturada de pesos (SAATY, 2008). Verifica-se, todavia, escassa consolidação de uma
trilha que conecte, de forma auditável, o chamado individual ao indicador agregado por
campus, deste à matriz de pesos multicritério e, por fim, à priorização gerencial. Soma-se
a essa lacuna a exigência, frequentemente negligenciada, de exploração prévia dos dados
para evitar a superinterpretação de indicadores ausentes, constantes ou em escalas
discrepantes (ZUUR; IENO; ELPHICK, 2010).

Diante desse cenário, o presente trabalho propõe um modelo auditável de apoio multicritério
à decisão para a manutenção predial universitária, que integra chamados, custos, indicadores
ODS/ESG e patrimônio imobiliário em uma matriz comparativa entre campi. O modelo articula
duas leituras complementares — a soma ponderada normalizada por Objetivo de Desenvolvimento
Sustentável e a ordenação por proximidade à solução ideal (TOPSIS) — sobre indicadores
derivados dos chamados, preservando a rastreabilidade de cada etapa de cálculo. Cabe
ressaltar, desde já, que o instrumento se destina ao apoio à priorização, e não à
substituição do julgamento do gestor público, e que o ranking produzido é comparativo dentro
do recorte de dados analisado, não constituindo certificação oficial de desempenho ODS ou
ESG. A delimitação desse escopo, longe de fragilizar a proposta, é condição para a
honestidade metodológica e para a reprodutibilidade que o trabalho persegue.

---

## 2. Referencial teórico (instrumental)

2.1 MCDM em facilities/edificações — Klumbytė et al. (2021), DOI 10.3390/su13052820;
Theilig et al. (2024), DOI 10.1007/s11367-024-02331-9.
2.2 Soma ponderada normalizada e TOPSIS — Hwang & Yoon (1981), DOI 10.1007/978-3-642-48318-9.
2.3 AHP como referência de elicitação de pesos — Saaty (2008), DOI 10.1504/IJSSCI.2008.017590
(apresentado como horizonte de evolução, não como método aplicado).
2.4 Exploração e qualidade de dados — Zuur, Ieno & Elphick (2010), DOI
10.1111/j.2041-210X.2009.00001.x.
2.5 ODS/ESG no ambiente construído institucional (ODS 9, 11, 12).

---

## 3. Materiais e métodos

Versão detalhada em [`ARTIGO_SECAO_3_MATERIAIS_METODOS.md`](ARTIGO_SECAO_3_MATERIAIS_METODOS.md);
indicadores em [`DICIONARIO_INDICADORES.md`](DICIONARIO_INDICADORES.md). Subseções: 3.1
contexto e unidade de análise; 3.2 fontes e governança (hub × eixo); 3.3 indicadores e
mapeamento ODS/ESG; 3.4 exploração de dados e exclusões (Zuur); 3.5 normalização min–max;
3.6 ponderação (não-AHP); 3.7 agregação e ranking (soma ponderada + TOPSIS); 3.8 camada
patrimonial; 3.9 evolução temporal (pendente); 3.10 reprodutibilidade.

---

## 4. Resultados

> Os valores reportados nesta seção referem-se ao snapshot de 20 de junho de 2026,
> regenerado após a correção do indicador de razão entre manutenção preventiva e corretiva
> (Seção 6), e devem ser reconferidos a cada nova execução do motor, uma vez que a base de
> chamados é incremental.

### 4.1 Caracterização do snapshot

A análise incidiu sobre cinco unidades de decisão — os campi Jorge Amado, Paulo Freire,
Sosígenes Costa e Maria Felipa, em Jequié, além da Reitoria —, tomadas como alternativas
comparáveis no recorte transversal disponível. O volume de chamados classificados por
unidade revela acentuada heterogeneidade de escala: registram-se 4.080 chamados no campus
Sosígenes Costa, 3.740 no campus Jorge Amado, 3.684 no campus Paulo Freire e 2.363 na
Reitoria, ao passo que o campus Maria Felipa contabiliza apenas 5 registros no período. Essa
assimetria é determinante para a leitura subsequente, pois a unidade de volume muito baixo
comprime o intervalo de normalização e, conforme se demonstra adiante, condiciona de modo
expressivo a posição relativa das demais.

### 4.2 Indicadores incluídos e excluídos

Em observância ao protocolo de exploração de dados de Zuur, Ieno e Elphick (2010), cada
indicador foi submetido a uma auditoria de variância antes de integrar o escore composto, de
modo que apenas os critérios com variação efetiva entre as unidades participam da ordenação.
Dos dez indicadores previstos, cinco mostraram-se ativos no snapshot analisado — número total
de chamados, número de chamados de infraestrutura crítica, número de chamados em espaço
coletivo, razão entre manutenção preventiva e corretiva, e valor total gasto. Os cinco
restantes foram exibidos na auditoria como lacunas e mantidos fora do cálculo: o tempo médio
de resolução e a taxa de resolução no prazo permanecem vazios por ausência de data de
conclusão padronizada; o número de chamados críticos de alta criticidade apresenta-se
constante e nulo; a densidade de chamados por área não pôde ser computada enquanto a área
construída por campus não estiver materializada; e o número de chamados repetidos depende de
uma chave de recorrência ainda inexistente. Convém registrar que o indicador de razão entre
manutenção preventiva e corretiva só se incorporou ao conjunto ativo após a correção da
heurística descrita na Seção 6, sem a qual permaneceria como quase-lacuna por variância
praticamente nula.

### 4.3 Ranking por ODS e escore geral

A soma ponderada normalizada por Objetivo de Desenvolvimento Sustentável produz, para o
escore geral, a seguinte ordenação decrescente: campus Maria Felipa (53,9), Reitoria (48,4),
campus Jorge Amado (36,8), campus Paulo Freire (34,3) e campus Sosígenes Costa (23,3). A
decomposição por dimensão evidencia, contudo, que essa hierarquia não é uniforme entre os
objetivos. No ODS 9, voltado à infraestrutura, o campus Maria Felipa alcança o valor máximo
(80,0), seguido a distância pela Reitoria (39,4), enquanto as unidades de maior volume obtêm
escores baixos (16,1; 15,2; 10,0), efeito direto do sentido minimizador dos indicadores de
contagem combinado à compressão do intervalo pela unidade de baixo volume. No ODS 12,
associado ao consumo responsável e ao gasto, a ordenação se inverte parcialmente, com
destaque para os campi Paulo Freire (71,8) e a Reitoria (69,3). Essa divergência dimensional
constitui, em si, um resultado relevante, pois desaconselha a leitura do escore geral de
forma isolada e recomenda que a priorização orçamentária considere o perfil de cada unidade
em cada objetivo.

### 4.4 TOPSIS e concordância com a soma ponderada

A ordenação por proximidade à solução ideal produz hierarquia distinta da soma ponderada:
campus Jorge Amado (56,7), Reitoria (52,6), campus Maria Felipa (44,0), campus Paulo Freire
(39,3) e campus Sosígenes Costa (33,8). A comparação entre os dois métodos revela
convergência nos extremos inferiores e na posição intermediária — a Reitoria figura em
segundo lugar em ambas as abordagens e o campus Sosígenes Costa ocupa a última posição nas
duas —, mas diverge de modo expressivo no topo: a unidade de baixo volume, que lidera a soma
ponderada por força da normalização min–max, recua à terceira posição sob o TOPSIS, ao passo
que o campus Jorge Amado ascende à liderança. Tal divergência confirma que a primazia do
campus Maria Felipa na soma ponderada é, em larga medida, artefato de escala, e não expressão
de desempenho efetivo. Recomenda-se, por isso, quantificar a concordância entre as
ordenações por meio de coeficiente de correlação de postos e reportar o ranking com e sem a
unidade de baixo volume, procedimento que isola as posições estáveis daquelas sensíveis à
composição do conjunto de alternativas.

### 4.5 Leitura patrimonial

A dimensão patrimonial, ainda que não integre diretamente o escore composto, oferece contexto
indispensável à interpretação. O valor total registrado em chamados concentra-se no campus
Sosígenes Costa (R$ 8,50 milhões), seguido pelos campi Jorge Amado (R$ 5,95 milhões) e Paulo
Freire (R$ 3,07 milhões) e pela Reitoria (R$ 2,21 milhões), sem valor apreciável no campus
Maria Felipa. Observa-se que as unidades de maior dispêndio são justamente as penalizadas no
escore geral pelo sentido minimizador dos indicadores de volume e de gasto, o que reforça a
necessidade de normalizar tais critérios por exposição física. Essa normalização permanece,
todavia, latente enquanto a área construída por campus não for materializada, mantendo
indisponível o indicador de densidade de chamados por área e limitando, no estado atual, a
leitura ambiental do modelo.

---

## 5. Discussão

A articulação entre a soma ponderada normalizada por Objetivo de Desenvolvimento Sustentável
e a ordenação por proximidade à solução ideal confere ao modelo duas leituras
complementares, e a comparação entre ambas constitui, em si, um elemento de validação
interna. Verifica-se que a soma ponderada favorece a interpretação dimensional, ao explicitar
o desempenho de cada campus em ODS 9, ODS 11 e ODS 12 separadamente, ao passo que o TOPSIS
sintetiza os critérios ativos em um único índice de proximidade comparativa. Diante disso,
recomenda-se reportar a concordância de ordenação entre as duas abordagens por meio de
coeficientes de correlação de postos, de modo que a convergência entre métodos reforce a
estabilidade da hierarquia, enquanto eventuais divergências apontem os critérios responsáveis
pela inversão de posições.

Constata-se, todavia, que a robustez da ordenação está condicionada à estrutura de pesos
adotada. Como os pesos são operacionais e editáveis, e não derivam de elicitação formal com
verificação de consistência, a interpretação dos resultados deve acompanhar-se de uma análise
de sensibilidade que perturbe os pesos e contraste o ranking obtido com um cenário de pesos
iguais. Tal procedimento, longe de enfraquecer o modelo, fortalece a sua credibilidade, pois
distingue as posições que se mantêm sob diferentes hipóteses de ponderação daquelas que são
artefato de uma configuração específica de pesos. A literatura de apoio multicritério à
decisão em facilities sustenta essa cautela, ao tratar a ponderação como etapa sujeita a
juízo de valor e, portanto, a teste (KLUMBYTĖ et al., 2021).

A camada patrimonial cumpre, nesse arranjo, papel que excede a mera contextualização. Ao
disponibilizar área e valor de ativos por campus, ela permite normalizar indicadores por
exposição física, aproximando unidades de portes distintos e reduzindo o viés de escala que
penalizaria, de outro modo, os campi de maior dimensão construída. Cabe ressaltar que essa
normalização permanece parcialmente latente enquanto a área construída por campus não estiver
materializada, o que mantém indisponível o indicador de densidade de chamados por área e
limita, no estado atual, a leitura ambiental do modelo.

Em perspectiva mais ampla, a contribuição do trabalho não reside em mensurar diretamente a
sustentabilidade institucional, mas em constituir um mecanismo verificável e auditável que
aproxima a manutenção predial, a governança e os Objetivos de Desenvolvimento Sustentável. A
decisão multicritério deve ser compreendida como apoio à priorização de recursos escassos, e
não como substituição do julgamento do gestor público, de modo que o instrumento se presta a
fundamentar escolhas orçamentárias e a conferir transparência ao processo decisório. Observa-
se, por fim, que a honestidade quanto às lacunas — em particular o fato de que apenas parte
dos indicadores apresenta variação suficiente no snapshot analisado — não compromete a
proposta, mas delimita com precisão o alcance das inferências possíveis e orienta as
melhorias prioritárias na fonte de dados.

---

## 6. Limitações e riscos de interpretação

A limitação mais relevante do modelo diz respeito à natureza do ranking produzido.
Constata-se que a ordenação dos campi é comparativa dentro do recorte de dados analisado,
e não uma certificação oficial de desempenho em relação aos Objetivos de Desenvolvimento
Sustentável ou aos pilares ambiental, social e de governança. Dessa forma, os escores não
devem ser lidos como medida absoluta de sustentabilidade, mas como posição relativa de cada
unidade no conjunto de critérios ativos, condicionada ao snapshot vigente.

Quanto à ponderação dos critérios, cabe destacar que os pesos adotados são operacionais e
editáveis, com leitura compatível com o método de análise hierárquica, porém não constituem
elicitação formal segundo Saaty (2008). Não foram construídas matrizes de comparação pareada
entre critérios, não se extraiu autovetor de pesos e não se calculou a razão de
consistência. Por conseguinte, evita-se neste trabalho a afirmação de que houve aplicação de
AHP formal, e a elicitação estruturada de pesos por especialistas é remetida a etapa
posterior.

Observa-se, ainda, que tanto a normalização min–max quanto o TOPSIS são sensíveis à
composição do conjunto de alternativas. O escore de um campus depende dos valores mínimo e
máximo observados entre as unidades, de modo que a inclusão ou a exclusão de um campus altera
a ordenação dos demais. Diante disso, e na ausência de uma análise de sensibilidade
sistemática dos pesos, a ordenação não deve ser apresentada como robusta sem o devido teste,
recomendando-se reportar a estabilidade do ranking sob perturbação dos pesos e sob cenário de
pesos iguais.

A qualidade e a cobertura dos dados administrativos impõem cautela adicional. Os indicadores
são derivados de registros de chamados sujeitos a subnotificação e a heterogeneidade de
preenchimento entre campi, e o mapeamento de cada indicador às dimensões ODS e ESG é
interpretativo, configurando uma associação por proxy institucional, e não uma classificação
oficial. No snapshot analisado, apura-se que apenas parte dos indicadores apresenta variação
suficiente entre as unidades; os demais permanecem vazios ou constantes e, conforme o
protocolo de exploração de dados de Zuur, Ieno e Elphick (2010), são exibidos na auditoria
como lacunas de qualidade, sem integrar o escore composto.

Duas ressalvas de implementação, identificadas no código do motor de indicadores, merecem
registro explícito. A primeira refere-se ao indicador de razão entre manutenção preventiva e
corretiva, que demandou correção em dois níveis. No primeiro, relativo ao cálculo, a rotina
anterior, quando a contagem de chamados corretivos era nula, retornava a contagem absoluta de
chamados preventivos em lugar de uma razão, introduzindo valores em escala incompatível que
comprometiam a normalização de um indicador de sentido maximizador; o cálculo foi corrigido
para a proporção de manutenção preventiva, limitada ao intervalo unitário, de modo que a
unidade indica predominância integral de preventiva e o valor nulo indica predominância
integral de corretiva. No segundo nível, relativo à fonte, a inspeção dos chamados
classificados revelou que a taxonomia de categorias não possui rótulo explícito de
"corretiva": apenas o ramo de manutenção preventiva é nomeado, de sorte que a heurística
original, ao buscar o termo "corretiva", fixava a contagem de corretivos em zero e reduzia o
indicador a uma quase-lacuna de variância praticamente nula. Adotou-se, então, a definição de
corretiva por exclusão — todo chamado classificado que não seja preventiva é contabilizado
como corretivo —, o que restituiu a variação efetiva entre as unidades, com proporções de
manutenção preventiva entre 0,26 e 0,34 nos campi de volume regular. Ambas as correções foram
replicadas no motor do repositório hub, que constitui a fonte autenticada dos dados, e os
snapshots foram regenerados; registra-se, contudo, que a definição por exclusão é uma medida
provisória, a ser substituída pela marcação explícita de "corretiva" na classificação de
origem quando esta estiver disponível. A segunda ressalva diz respeito à presença de uma
unidade com volume muito baixo de chamados no snapshot, a qual comprime o intervalo de
normalização e pode dominar artificialmente o resultado — efeito que se materializou na
liderança do campus Maria Felipa na soma ponderada e na sua queda à terceira posição sob o
TOPSIS (Seção 4.4) —, justificando que o ranking seja reportado com e sem essa unidade, ou
que se estabeleça um volume mínimo de elegibilidade.

Por fim, a ausência de série histórica validada impede, no estado atual, qualquer afirmação
de tendência temporal, uma vez que o snapshot disponível é transversal e não contempla a
dimensão anual. Ademais, por se tratar de estudo de caso circunscrito a uma universidade, a
validade externa dos resultados é limitada, de modo que a contribuição transferível reside no
método auditável proposto, e não nos valores específicos obtidos.

---

## 7. Conclusão e trabalhos futuros

O trabalho demonstrou a viabilidade metodológica de uma trilha auditável que converte
registros de chamados de manutenção predial em indicadores agregados por campus e, destes, em
uma ordenação multicritério para apoio à decisão. Constata-se que a integração entre dados
operacionais, custos, indicadores ODS/ESG e camada patrimonial, articulada por soma ponderada
normalizada e por ordenação de proximidade à solução ideal, permite hierarquizar unidades de
forma transparente e reprodutível, com cada etapa de cálculo passível de inspeção. A
contribuição transferível reside, portanto, no método proposto e na sua arquitetura de
rastreabilidade, e não nos valores específicos obtidos para a instituição estudada.

Diante das limitações reconhecidas, delineiam-se as direções de continuidade da pesquisa. É
imperativo materializar a série histórica por campus, em recorte anual ou mensal, para
habilitar a análise de tendência e a avaliação do que efetivamente se altera entre períodos,
bem como a área construída por campus, sem a qual a leitura ambiental do modelo permanece
incompleta. Em paralelo, a elicitação formal de pesos por painel de especialistas, com
construção de matriz de comparação pareada e cálculo da razão de consistência, elevaria o
rigor da ponderação ao patamar da análise hierárquica, hoje apenas aproximado. Recomenda-se,
ainda, incorporar a análise de sensibilidade dos pesos como rotina de validação e, em estágio
mais avançado, explorar modelos aditivos generalizados como camada explicável, condicionada à
disponibilidade de unidades observacionais suficientes. Cabe ressaltar, por fim, que o modelo
não autoriza a afirmação de impacto causal sobre os Objetivos de Desenvolvimento Sustentável,
limitando-se a oferecer um instrumento verificável de priorização para a gestão da manutenção
predial universitária.

---

## Controle de versão

- 2026-06-20 — Estrutura de seções, Seção 3 detalhada (arquivo próprio), Introdução,
  Limitações, Discussão e Conclusão em prosa final (estilo do autor), plano de
  figuras/tabelas. Correção do indicador razão preventiva/corretiva aplicada no
  `motor_ods.py` do eixo e do hub (`repo_malha_atual`); Limitações ajustadas para refletir
  a correção.
- 2026-06-20 (atualização) — Correção em segundo nível do mesmo indicador: definição de
  corretiva por exclusão (heurística da fonte), reativando-o como ativo (proporções
  0,26–0,34). Snapshots regenerados na nuvem via GitHub Actions (hub recalcula a planilha →
  hub exporta JSON → eixo puxa). Seção 4 (Resultados) redigida em prosa final com os números
  do snapshot corrigido, incluindo ranking por ODS, escore geral, TOPSIS e leitura
  patrimonial. Limitações e Controle de versão atualizados.
