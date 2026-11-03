# Gêmeo digital da manutenção predial: desenho e protótipo

Desenho do "gêmeo digital" do eixo ODS/ESG e protótipo funcional (v0) em [`../../gemeo_digital/`](../../gemeo_digital/index.html). Criado em 03/11/2026, com autorização do autor, sobre os dados agregados reais já existentes (chamados do hub e patrimônio) e sem qualquer dado simulado.

| Arquivo | Conteúdo |
|---|---|
| `01_CONCEITO_E_ESCOPO.md` | O que é (sombra digital), níveis de maturidade, usuários e decisões, o que não é |
| `02_ARQUITETURA.md` | Camadas, fluxo de dados, congelamento, privacidade, automação futura |
| `03_DESIGN_DO_DASHBOARD.md` | Arquitetura de informação, telas, interações, sistema visual, acessibilidade e evolução |
| `04_CONTRATOS_DE_DADOS.md` | Estrutura de `gemeo.json`, regras de versionamento e testes de contrato |
| `05_ROADMAP_E_RISCOS.md` | Roadmap por versão, critérios de aceite, riscos e decisões que cabem ao autor |

Como abrir o protótipo: abrir `gemeo_digital/index.html` no navegador (funciona sem servidor, porque os dados vão em `dados/dados.js`); após o merge, o `pages.yml` atual publica a raiz do repositório e o painel ficará em `https://adinailson88.github.io/malha-ods-esg/gemeo_digital/`. Como regenerar os dados: `python scripts/replicacao/gerar_dados_gemeo.py <caminho>/malha-ia/dados/chamados.json`. Como testar: `python -m unittest tests.test_gemeo -v`.

Atenção à publicação: o painel mostra prioridades por campus e sistema com os nomes dos campi. Ele traz aviso de protótipo, mas a publicação pública de qualquer ranking de unidades institucionais é uma decisão do autor e da instituição (seção 5 de `05_ROADMAP_E_RISCOS.md`).
