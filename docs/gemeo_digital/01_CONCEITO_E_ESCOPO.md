# Conceito e escopo

## 1. O que se constrói e como chamá-lo

Na classificação de Kritzinger et al. (2018, IFAC-PapersOnLine, 51(11), 1016-1022, DOI 10.1016/j.ifacol.2018.08.474), um modelo digital não tem fluxo automático de dados com o sistema físico, uma sombra digital recebe dados automaticamente do sistema físico para o modelo, e um gêmeo digital completo também devolve automaticamente ao sistema físico. Esse trabalho observa ainda que o nível de gêmeo completo é raro na literatura.

O objeto aqui é uma sombra digital da manutenção predial da UFSB: os registros de chamados, a área física dos campi e a classificação por IA alimentam, de forma reprodutível, um modelo que representa o estado da carteira, a prioridade de intervenção com incerteza e a qualidade dos dados. A decisão e qualquer ordem de serviço continuam humanas. O nome "gêmeo digital" é usado como convenção do projeto; no texto científico deve-se escrever "sombra digital" ou "gêmeo digital de apoio à decisão (nível sombra)", para não prometer o que o sistema não faz.

Evidência de contexto, encontrada em busca e ainda não lida em texto integral (V3): um protótipo de arcabouço de gêmeo digital de edifícios de campus com varredura a laser, BIM e sensores de IoT cujos dados eram em grande parte simulados (preprint de 2025), um estudo de campus no Japão com modelo 3D e dados de inspeção em formato COBie (conferência de 2024) e um artigo de 2026 em *Buildings* que une gêmeo digital e entrevistas com partes interessadas. Esses trabalhos partem de BIM e sensores, que a UFSB não tem em formato utilizável neste conjunto; o diferencial aqui é o uso de registros administrativos de manutenção com incerteza explícita.

## 2. Níveis de maturidade

| Nível | Descrição | Dados exigidos | Estado |
|---|---|---|---|
| L0 Sombra de registros | Estado da carteira de chamados, demanda por área, qualidade dos dados, prioridade com incerteza de pesos, cenários de pesos | Chamados agregados e área por campus | Protótipo v0 entregue |
| L1 Sombra com condição | Inclui datas de solução, prioridade nativa, localização e ativo, usuários, laudos de inspeção | GLPI completo, usuários, laudos | Depende de dados D03 a D05, D11 e D16 da matriz de dados |
| L2 Sombra preditiva | Inclui previsões de demanda e custo (Artigos 2 e 3) e cenários climáticos | Resultados validados dos outros eixos, clima por campus | Depende dos Artigos 2 e 3 |
| L3 Apoio à decisão com retorno | Recomenda lotes de ordens de serviço e registra a decisão do gestor para aprendizado, com aprovação humana | Fluxo institucional e governança | Horizonte; exige decisão institucional |

## 3. Usuários e decisões que o painel deve apoiar

1. Gestor de infraestrutura: onde concentrar equipe e recursos no próximo ciclo; quais chamados abertos estão mais antigos; quais sistemas pressionam cada campus.
2. Fiscal e gestor de contratos: que sistemas justificam serviços contínuos, e com que incerteza; efeito da normalização por área sobre a comparação entre campi.
3. Alta gestão (pró-reitorias): leitura resumida do estado e da prioridade, com avisos de limite.
4. Pesquisador e avaliador: reprodutibilidade, versão do dado, incerteza e limites, para examinar o método.

Pergunta que cada tela responde: Estado, "como está a carteira hoje?"; Prioridade, "onde intervir primeiro e quão firme é essa ordem?"; Qualidade, "quanto posso confiar nos dados?"; Cenários, "e se eu mudar a importância dos critérios?"; Método, "como isto foi calculado e o que não vale?".

## 4. O que o painel não é

1. Não é certificação ODS ou ESG, nem ranking de desempenho institucional.
2. Não substitui julgamento técnico nem laudo de inspeção predial.
3. Não prevê o futuro (nível L0); a validade preditiva é testada de modo exploratório e declarada.
4. Não contém texto de chamados nem dados pessoais.
5. Não é resultado do artigo: ilustra o desenho de `docs/auditoria/03_DESENHO_DO_ESTUDO_A1.md`.

## 5. Relação com o artigo

O painel é o produto técnico do pré-projeto (painel gerencial interativo, indicadores e instrumento de priorização) e serve de material suplementar do artigo: cada tabela e figura do artigo deve ser reproduzível a partir da mesma cadeia de dados, com a versão do dado exibida no painel. A diferença entre painel e artigo é de função: o painel explora e comunica; o artigo prova, com protocolo pré-registrado.
