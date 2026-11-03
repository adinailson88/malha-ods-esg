# Gêmeo digital (sombra digital) da manutenção predial: protótipo v0

Página única `index.html`, sem servidor e sem dependências externas. Os dados agregados ficam em `dados/gemeo.json` (contrato) e `dados/dados.js` (mesmo conteúdo em `window.GEMEO`, para funcionar em `file://`).

Natureza: protótipo metodológico. Não é resultado de artigo. Usa apenas agregados reais de chamados (hub `malha-ia`) e de patrimônio; não há dado simulado.

1. Abrir: abrir `gemeo_digital/index.html` no navegador.
2. Regenerar os dados: `python scripts/replicacao/gerar_dados_gemeo.py <caminho>/malha-ia/dados/chamados.json`. A saída é determinística (semente fixa) e registra o SHA-256 do arquivo de entrada.
3. Testar: `python -m unittest tests.test_gemeo -v`.
4. Documentação de desenho: `docs/gemeo_digital/README.md`.

Publicação: o `pages.yml` publica a raiz do repositório, então esta pasta ficará pública após o merge na `main`. Como o painel mostra prioridades por campus e sistema, a decisão de publicar fica com o autor e a instituição (`docs/gemeo_digital/05_ROADMAP_E_RISCOS.md`, seção 5).
