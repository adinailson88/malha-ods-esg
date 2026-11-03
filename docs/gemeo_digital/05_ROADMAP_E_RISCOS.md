# Roadmap, riscos e decisões do autor

## 1. Versões

| Versão | Escopo | Critério de aceite | Dependências |
|---|---|---|---|
| v0 (entregue) | Painel estático com estado, prioridade com incerteza, qualidade, cenários e método; gerador e testes | Abre sem servidor; sem erros de console; testes passam; sem rolagem horizontal em 390 px; avisos visíveis | Dados agregados do hub e patrimônio |
| v0.2 | Detalhe por alternativa; exportação CSV; modo de impressão; aviso de dado antigo; tabela equivalente aos gráficos | Navegação por teclado completa; contraste conferido; exportação reproduz a tela | Nenhuma |
| v1 | Pesos elicitados com intervalo, tempo de resolução e prioridade do GLPI, usuários, referência fixa de normalização, versão congelada | Critérios de aceite do estudo (seção 18 de `docs/auditoria/03_DESENHO_DO_ESTUDO_A1.md`) | Dados D03, D04, D11 e painel de especialistas |
| v2 | Critérios previstos (Artigos 2 e 3), cenários climáticos e de orçamento, mapa | Previsões validadas e versionadas | Artigos 2 e 3, covariáveis reais |
| v3 | Apoio à decisão com retorno e registro de decisões | Governança institucional e parecer jurídico | Decisão institucional |

## 2. O que o protótipo já mostra de verdade (com os limites)

1. A carteira aberta por campus e sua idade (por exemplo, chamados abertos há mais de 365 dias), referida à data mais recente da base.
2. O efeito da normalização por área sobre a ordem de prioridade (correlações de postos de 0,63 a 0,83 entre contagem bruta e por 1.000 m² nos anos de 2022 a 2025), com postos que mudam seis ou mais posições.
3. A grande amplitude dos intervalos de postos com pesos incertos: poucas alternativas têm posição firme.
4. O teste exploratório: o índice composto não supera a persistência da demanda para antecipar a demanda do ano seguinte (correlações de postos de 0,65 a 0,69 contra 0,84 a 0,97), sem que isso valha como resultado do artigo, porque o índice inclui a demanda e porque os critérios e a normalização são de protótipo.
5. A qualidade dos dados: baixa confiança da classificação de 50% a 80% desde 2022 e proporção de OS muito diferente entre campi.

## 3. Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Leitura do painel como ranking oficial de campi | média | alto | Aviso permanente, nome "prioridade" e não "desempenho", restrição de publicação até validação |
| Interpretar o protótipo como resultado do artigo | média | alto | Aviso de protótipo; artigo só com dado congelado e protocolo pré-registrado |
| Sensibilidade da família técnica ao erro de classificação | alta | médio | Sinalizar baixa confiança; versão por confiança no v1; agrupar famílias se necessário |
| Normalização por mínimo e máximo instável | média | médio | Referência fixa no v1 |
| Área por campus equivocada (utilização contra construída) | média | médio | Confirmação com o setor de patrimônio; origem declarada em cada ponto |
| Dados defasados | média | médio | Aviso de idade; regeneração semanal automatizada |
| Privacidade por contagem muito pequena | baixa | alto | Limiar de supressão a definir |
| Manutenção do painel sem dono | média | médio | Documentação, testes e pacote de replicação |

## 4. Estrutura do repositório

Já criada nesta entrega: `gemeo_digital/` (painel e dados), `docs/gemeo_digital/` (desenho), `scripts/replicacao/gerar_dados_gemeo.py` (gerador) e `tests/test_gemeo.py` (testes). A estrutura-alvo completa do repositório está em `docs/auditoria/06_PLANO_DE_EXECUCAO.md` (seção "Estrutura-alvo do repositório"): raiz enxuta, `docs/` com manuscrito, auditoria, literatura e desenho do painel, `dados/` com snapshots e dado congelado, `scripts/replicacao/`, `protocolo/`, `tests/` e `.github/workflows/`. As ações de higiene (remover o modelo de preenchimento obsoleto, mover as referências, corrigir `CITATION.cff`, escolher licença, restringir a publicação) dependem de aprovação do autor.

## 5. Decisões que cabem ao autor

1. Publicação: o `pages.yml` atual publica a raiz inteira, portanto o painel ficará público após o merge. Decidir se aceita a publicação do protótipo com o aviso, se restringe a publicação (por exemplo, publicando só `index.html`, `dashboard.html` e `dados/`, sem `gemeo_digital/`), ou se mantém o painel apenas local até a validação. Recomendação: restringir a publicação até haver validação e autorização institucional.
2. Nome: manter "gêmeo digital" no repositório e "sombra digital" no texto científico.
3. Critérios e normalização do painel: confirmar se o conjunto C1, C5, C7 e C2 representa o que se quer mostrar, ou ajustar para o conjunto mínimo do desenho.
4. Níveis de agregação: manter campus por sistema (24 alternativas) ou reduzir a campus (4 alternativas), que perde a utilidade para priorização, mas ganha robustez à classificação.
5. Área: confirmar `Area_Utilizacao_m2` como área construída e a projeção de +5% para 2026.
6. Próxima iteração: priorizar entre detalhe por alternativa, exportação para estudo técnico preliminar e mapa.
