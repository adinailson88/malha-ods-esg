# Continuidade — Artigo / Eixo ODS-ESG

> Nota de estado para retomada de sessão. **Atualizar este arquivo** ao avançar; não criar
> dossiês novos. Fonte canônica do manuscrito: [`ARTIGO_MALHA_ODS_ESG.md`](ARTIGO_MALHA_ODS_ESG.md).

## Última atualização: 2026-06-20

### O que está PRONTO
- **Artigo canônico** ([`ARTIGO_MALHA_ODS_ESG.md`](ARTIGO_MALHA_ODS_ESG.md)) com Introdução,
  Materiais e Métodos (detalhe em [`ARTIGO_SECAO_3_MATERIAIS_METODOS.md`](ARTIGO_SECAO_3_MATERIAIS_METODOS.md)),
  **Resultados (4.1–4.5)**, Discussão, Limitações e Conclusão em prosa final (estilo do autor).
- **Indicador `Razao_preventiva_corretiva` — corrigido em dois níveis** (motor do eixo e do hub
  `malha-ia`):
  1. *Cálculo:* proporção `n_prev/(n_prev+n_corr)` em [0,1] (antes devolvia `float(n_prev)` quando
     `n_corr==0`).
  2. *Heurística/fonte:* a taxonomia de `COL_CAT_IA` (col. Z) **não tem rótulo "corretiva"** — só o
     ramo `Manutenção Preventiva > …` é nomeado. Definição ratificada pelo usuário:
     **corretiva = todo chamado classificado que não seja preventiva** (exclusão simples, sem
     remover não-categorias). Resultado por campus: **~0,26–0,34** (Jorge Amado 0,268; Paulo Freire
     0,330; Sosígenes 0,336; Reitoria 0,261; Maria Felipa 0,000). Indicador **voltou a ser ativo**.
- **Guard de quase-lacuna** no `dashboard.html` (`avaliarIndicadores`): exclui do score indicador
  cujo valor dominante cobre ≥ N−1 das N unidades (regra de Zuur).
- **Snapshots regenerados na nuvem** (sem execução manual), cadeia de Actions:
  hub `ods_indicadores.yml` → hub `atualizar-dados-json.yml` → eixo `atualizar-dados-hub.yml`.
- **Republicação no Drive:** `artigo_1` é o doc **vigente**
  (id `1vw5vrrSJauf1tsBlgrnE0xtsak238H5i8D_GhNnrHP8`, pasta `1sxcVJLMUz-uAram9f6eBvVEzRgyufdX7`).

### Resultados do snapshot 2026-06-20 (reconferir a cada execução)
- **Indicadores ativos (5/10):** N_chamados_total, N_infra_critica, N_em_espaco_coletivo,
  Razao_preventiva_corretiva, Valor_total_gasto_R$. Lacunas (5): tempo médio e taxa no prazo
  (vazios), N_criticos_alta (constante 0), densidade (falta área/campus), repetidos (falta chave).
- **Soma ponderada (geral):** Maria Felipa 53,9 · Reitoria 48,4 · Jorge Amado 36,8 ·
  Paulo Freire 34,3 · Sosígenes 23,3.
- **TOPSIS:** Jorge Amado 56,7 · Reitoria 52,6 · Maria Felipa 44,0 · Paulo Freire 39,3 ·
  Sosígenes 33,8.
- **Leitura:** a divergência no topo confirma que a liderança de Maria Felipa na soma ponderada é
  artefato de escala (campus com ~5 chamados); reportar ranking com e sem essa unidade.

### PENDENTE (retomar aqui)
1. **Apagar no Drive** (o conector não deleta; o usuário apaga): docs obsoletos pré-numeração
   `1JvSzuBnao5gs-0QeV6p6pEfWIkQQcltgpelGyPR6rOg` (ARTIGO_..._RASCUNHO) e
   `1COTp43PM_AmIE6GIYxcn_7Zi2aiNgjf6F3SCWgjuO-M`.
2. **Referencial teórico (seção 2)** ainda em tópicos → passar para prosa (skill meu-estilo-textual).
3. **Análise de sensibilidade dos pesos** e **coeficiente de correlação de postos** (soma ponderada
   × TOPSIS): recomendados no texto, ainda não executados.
4. **Melhoria futura do indicador:** se a classificação de origem passar a marcar "corretiva"
   explicitamente, trocar a definição por exclusão pelo rótulo direto.

### Convenções fixas (não reabrir)
- Ranking é **comparativo intra-snapshot**, não certificação ODS/ESG.
- Pesos são **operacionais/editáveis**, leitura compatível com AHP, **não AHP formal** (sem matriz
  pareada nem razão de consistência).
- Drive: cada republicação é um **novo Google Doc numerado** (`artigo_N`); **próxima = `artigo_2`**.
  Sempre informar ao usuário qual é o vigente e quais apagar.
- Push direto na `main` dos dois repos autorizado; `gh` logado como `adinailson88-jpg` tem push em
  ambos os repos de `adinailson88`.
