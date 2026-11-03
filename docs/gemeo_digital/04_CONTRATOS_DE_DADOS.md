# Contratos de dados

O painel lê um único objeto, `window.GEMEO`, definido em `gemeo_digital/dados/dados.js` e espelhado em `gemeo.json`. Esta é a versão 0 do contrato (protótipo). Alterações de estrutura incrementam a versão e atualizam os testes em `tests/test_gemeo.py`.

## 1. Estrutura

1. `meta`: `titulo`, `natureza` (aviso de protótipo), `gerado_em_utc`, `chamados_sha256`, `chamados_bytes`, `chamados_preenchidos`, `data_mais_recente`, `criterios` (id e nome), `familias`, `campi` (id e nome curto), `n_sorteios_smaa`, `semente`, `avisos` (lista de textos fixos).
2. `painel`: lista de registros por campus e ano com `n`, `os`, `os_pct`, `valor_corrente`, `valor_posto`, `prev`, `baixa_conf_pct`, `crit_alta`, `area_m2`, `area_origem` (`PATRIMONIO` ou `PROJETADO_5PCT`), `n_por_1000m2`, `valor_corrente_por_1000m2` e `parcial` (2026).
3. `mensal`: por campus, lista de pares (mês, contagem).
4. `carteira_aberta`: por campus, contagens por faixa de idade (`ate30`, `d31a90`, `d91a365`, `mais365`) e `total`, referidas à data mais recente da base.
5. `prioridade`: por ano de índice (2022 a 2025), duas variantes (`exposicao` e `bruto`) com `alternativas` (campus, família, `n`, `valor_corrente`, `tendencia`, `severidade`, `area_m2`, `c` (critérios brutos), `r` (critérios normalizados), `escore_igual`, `posto_igual`, `aceitabilidade` (vetor por posto), `posto_medio`, `p5` e `p95`) e `spearman_bruto_exposicao`.
6. `validacao_exploratoria`: por ano, correlação de postos do índice e da persistência da demanda com a demanda do ano seguinte, com `n_alternativas`.

## 2. Regras

1. Nenhum campo de texto livre de chamados, nenhum identificador de chamado, nenhum dado pessoal.
2. Valores monetários nominais, em reais; áreas em m2; datas em ISO.
3. Todo valor derivado de projeção deve declarar a origem (`area_origem`); nenhum dado simulado entra no painel.
4. O hash do arquivo de chamados identifica a versão do dado; quando o painel for usado no artigo, a versão congelada e o hash devem coincidir com o release arquivado.
5. A semente do SMAA é fixa: duas execuções com o mesmo dado produzem o mesmo resultado (exceto `gerado_em_utc`).

## 3. Testes de contrato

`tests/test_gemeo.py` verifica: funções de posto, correlação de postos e normalização; propriedades do SMAA (aceitabilidade soma 1 por alternativa e por posto, alternativa dominante tem aceitabilidade 1); mapeamento e projeção de área; presença e formato dos campos de `gemeo.json`; 24 alternativas por ano e variante; ausência de campos não previstos nos registros (proteção contra vazamento de texto).

## 4. Evolução

1. v1: acrescentar pesos elicitados com intervalo, critério de tempo de resolução e prioridade nativa do GLPI, usuários por campus e versão congelada.
2. v2: critérios previstos dos Artigos 2 e 3 e cenários.
3. Cada versão mantém compatibilidade ou declara a quebra no `meta`.
