# Design do painel

## 1. Princípios

1. Responder perguntas, não exibir dados: cada seção tem uma pergunta explícita (seção 3 de `01_CONCEITO_E_ESCOPO.md`).
2. Incerteza sempre visível: nenhuma posição de prioridade aparece sem o intervalo de postos; o posto pontual é secundário (Goldstein e Spiegelhalter, 1996, DOI 10.2307/2983325).
3. Versão e limites sempre à vista: hash do dado, data de geração, faixa de aviso "protótipo metodológico, não é resultado de artigo", seção de método e limites.
4. Honestidade antes de estética: se o índice não supera a persistência da demanda, o painel mostra isso (Quadro 3).
5. Leitura de relatório, não de produto: o painel é um documento técnico navegável, com figuras numeradas, legendas de leitura e números em tipografia monoespaçada. Evita a linguagem visual de painel de negócios (cartões, indicadores grandes, sombras, cantos arredondados).
6. Acessível por padrão: contraste, teclado, cor não é o único canal, tabela equivalente aos gráficos principais, impressão.

## 2. Arquitetura de informação

Página única de rolagem, com índice numerado fixo à esquerda (trilho) e faixa de aviso no topo. Em telas estreitas o trilho vira cabeçalho e os controles passam para o fluxo.

| Seção | Pergunta | Conteúdo no protótipo v0 | Próximas evoluções |
|---|---|---|---|
| 01 Estado da carteira | Como está a carteira hoje? | Quadro 1 (abertos, faixas de idade, chamados por ano por 1.000 m², proporção com OS, baixa confiança da IA); Figura 1, média móvel de 12 meses da demanda por área, com rótulos diretos | Filtro por sistema; tempo de resolução (com dado do GLPI) |
| 02 Prioridade com incerteza | Onde intervir primeiro, com que firmeza? | Figura 2, intervalos de postos (5% a 95%, SMAA-2) com P(1º), P(top 5) e posto na outra normalização; Figura 3, gráfico de inclinação entre contagem bruta e por área, com Spearman | Pesos elicitados com intervalo; outranking; exportação para estudo técnico preliminar |
| 03 Qualidade dos dados | Quanto confiar? | Figuras 4 e 5, mapas de calor de baixa confiança e de proporção de OS por campus e ano | Cobertura de campos do GLPI; completude; regime do classificador |
| 04 Cenários de pesos | E se eu mudar os pesos? | Quatro controles de peso e o Quadro 2 (12 primeiras prioridades, com situação "dentro" ou "fora" do intervalo de 90%) | Cenários de previsão e de orçamento |
| 05 Método e limites | Como foi calculado e o que não vale? | Critérios, SMAA, Quadro 3 (validade preditiva exploratória), lista numerada de limites, sombra versus gêmeo, comando de reprodução | Versões anteriores do dado; changelog |

## 3. Interações

1. Seletor de ano (2022 a 2025) e de normalização (por 1.000 m² ou bruto) no trilho, valendo para as seções 02 e 04.
2. Controles de peso de 0 a 100, com recálculo imediato no navegador e situação frente ao intervalo de 90%.
3. Índice com realce da seção corrente (IntersectionObserver), âncoras por seção (`#prioridade`), rolagem suave que respeita `prefers-reduced-motion`.
4. Tema claro e escuro, com a preferência do sistema como padrão e botão de alternância.
5. Evoluções: seleção de alternativa para detalhar, exportação de CSV e imagem, cabeçalho de versão na impressão.

## 4. Sistema visual

1. Base: papel quente (`--paper`), tinta quase preta (`--ink`), filetes finos em vez de bordas e sombras, cantos retos, destaque único em vermelhão (`--a`). Tema escuro derivado dos mesmos tokens.
2. Tipografia: corpo e títulos em serifa de sistema; rótulos, números e metadados em monoespaçada; sem fontes externas. Rótulos em caixa alta com espaçamento (`Quadro 1`, `Figura 2`).
3. Cores de dados: quatro cores de campus (azul, vermelhão, verde, magenta) escolhidas para distinção por pessoas com daltonismo, sempre com rótulo direto ou texto ao lado; escala sequencial azul para mapas de calor.
4. Componentes: tabela com filetes, faixas empilhadas de idade, gráfico de intervalos, gráfico de inclinação, mapa de calor de células quadradas, controles com trilho fino. Sem cartões, sem pílulas, sem ícones decorativos.
5. Gráficos: SVG em `viewBox`, contêiner rolável em telas estreitas para preservar a legibilidade; legenda "Leitura" abaixo de cada figura, dizendo o que olhar e o que não concluir.
6. Texto: português técnico e sucinto, sem promessas; avisos com linguagem de limite ("protótipo", "a confirmar", "projetado").

## 5. Acessibilidade e desempenho

1. `role="img"` com descrição nos gráficos, foco visível, navegação por teclado, `prefers-reduced-motion` e `prefers-color-scheme`.
2. Tabelas equivalentes para o Quadro 1, Quadro 2 e Quadro 3; a ampliar para as figuras 2 a 5.
3. Arquivo único de página sem dependências externas e cerca de 190 KB de dados; uso offline por `file://` (dados em `dados/dados.js`).
4. Validação feita em 1280 e 390 pixels, claro e escuro, sem erros de console e sem rolagem horizontal da página. Teste automático de contrato dos dados e de ausência de recursos externos em `tests/test_gemeo.py`.

## 6. Estados e falhas

1. Dado ausente: mensagem com o comando de geração.
2. Dado antigo: aviso quando a data de geração exceder o limite (a implementar).
3. Alternativas com poucos chamados: supressão ou agrupamento conforme limiar de privacidade (a definir).
4. Divergência de versão entre painel e artigo: o trilho traz o início do hash do dado e o rodapé, a identificação completa.
5. Área ausente em um ano (Reitoria em 2018): usa-se o ano mais próximo com valor e isso deve constar no método.

## 7. Evolução do design

1. Mapa dos campi com prioridade (coordenadas do patrimônio) e camada de risco climático.
2. Detalhe por alternativa, com a incerteza decomposta por fonte (pesos, escala, notificação, classificação).
3. Frase de leitura gerada com limites ("a posição X é robusta; a Y não").
4. Página de decisão para gestor: as três prioridades robustas e os três pontos que exigem dados.
5. Visão para avaliador: reprodução, versões, testes e lista de verificação de replicação.
