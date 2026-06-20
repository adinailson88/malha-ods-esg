# Dicionário de indicadores ODS/ESG

Documento de rastreabilidade do eixo `malha-ods-esg`. Consolida, para cada indicador
multicritério, a sua definição operacional, sentido de otimização, fonte, associação a
ODS e a pilares ESG, e o **status no snapshot atual** (ativo no score ou lacuna de
qualidade). Serve como Quadro Q1 do artigo e como contrato de auditoria do painel.

Fontes deste dicionário (todas versionadas):

- `dados/indicadores_ods.json` — valores brutos por campus (snapshot).
- `dados/metadados_indicadores.json` — dimensão, sentido, condição de uso, limite atual,
  melhoria esperada da fonte.
- `dados/pesos_ods.json` — pesos por ODS (9, 11, 12).
- `dados/classificacao_ods_esg.json` — pesos ESG (E/S/G), classe principal e justificativa.

> Regra de leitura: os pesos abaixo são **pesos operacionais editáveis**, com leitura
> compatível com AHP, mas **não** constituem AHP formal — não houve matriz pareada de
> especialistas nem cálculo de razão de consistência (CR). Ver
> [`METODOLOGIA_MCDM_ODS_ESG.md`](METODOLOGIA_MCDM_ODS_ESG.md), seção 4.

## 1. Estado do snapshot (revalidar a cada execução)

Unidades de análise (alternativas) no snapshot atual: `Campus Jorge Amado`,
`Campus Maria Felipa - Jequié`, `Campus Paulo Freire`, `Campus Sosígenes Costa`,
`Reitoria` (5 unidades).

> **Cautela de fronteira do corpus:** o número de unidades e os valores brutos mudam a
> cada sincronização com o hub `malha-ia`. Reconferir antes de citar qualquer número no
> artigo. O `Campus Maria Felipa - Jequié` aparece com volume muito baixo de chamados no
> snapshot atual; por ser quase-vazio, distorce a normalização min–max e o TOPSIS, e deve
> ser tratado explicitamente (ver seção 4 deste documento).

## 2. Convenções

- **Sentido** — `maximizar` (maior é melhor), `minimizar` (menor é melhor),
  `contextual` (valor intermediário é favorecido; o indicador representa exposição/uso,
  não "quanto maior melhor").
- **Status no score** — `ativo` (entra no score composto e no TOPSIS) ou
  `lacuna` (exibido na auditoria, mas **não** entra no cálculo por estar vazio ou sem
  variação no snapshot). O status é derivado do snapshot e **não é permanente**: passa a
  `ativo` assim que a fonte fornecer dado válido e variável.
- **Pesos ODS** — colunas ODS 9 / ODS 11 / ODS 12 de `pesos_ods.json`.
- **Pesos ESG** — colunas E / S / G de `classificacao_ods_esg.json`;
  `Classe` é a dimensão ESG predominante (`Classe_Principal`).

## 3. Indicadores

### 3.1 N_chamados_total
- **Definição:** volume total de chamados de manutenção registrados por campus.
- **Sentido:** minimizar.
- **Dimensão principal (metadados):** Governança.
- **Pesos ODS** — 9: 0,10 · 11: 0,10 · 12: 0,05.
- **Pesos ESG** — E: 0,15 · S: 0,25 · G: 0,60 · **Classe: G**.
- **Status no snapshot:** **ativo** (há variação entre campi).
- **Limite atual:** proxy de pressão operacional; favorece campi menores se usado
  isoladamente (campus maior tende a registrar mais demandas).
- **Melhoria da fonte:** normalizar por área de campus, população usuária ou período.

### 3.2 N_infra_critica
- **Definição:** número de chamados em infraestrutura crítica por campus.
- **Sentido:** minimizar.
- **Dimensão principal (metadados):** ODS 9 / Governança.
- **Pesos ODS** — 9: 0,30 · 11: 0,10 · 12: 0,00.
- **Pesos ESG** — E: 0,10 · S: 0,25 · G: 0,65 · **Classe: G**.
- **Status no snapshot:** **ativo** (há variação entre campi).
- **Limite atual:** calculado por heurística textual/categoria; depende da qualidade da
  classificação dos chamados.
- **Melhoria da fonte:** revisar dicionário de infraestrutura crítica por família técnica.

### 3.3 Tempo_medio_resolucao_dias
- **Definição:** tempo médio, em dias, entre abertura e conclusão do chamado.
- **Sentido:** minimizar.
- **Dimensão principal (metadados):** Governança / Social.
- **Pesos ODS** — 9: 0,20 · 11: 0,05 · 12: 0,10.
- **Pesos ESG** — E: 0,00 · S: 0,35 · G: 0,65 · **Classe: G**.
- **Status no snapshot:** **lacuna** (vazio no snapshot atual).
- **Limite atual:** depende de data de conclusão padronizada, ausente no snapshot.
- **Melhoria da fonte:** adicionar data de conclusão padronizada ao snapshot ODS.

### 3.4 Taxa_resolucao_no_prazo
- **Definição:** proporção de chamados resolvidos dentro do SLA aplicável.
- **Sentido:** maximizar.
- **Dimensão principal (metadados):** Governança.
- **Pesos ODS** — 9: 0,20 · 11: 0,10 · 12: 0,10.
- **Pesos ESG** — E: 0,00 · S: 0,25 · G: 0,75 · **Classe: G**.
- **Status no snapshot:** **lacuna** (vazio no snapshot atual).
- **Limite atual:** depende de SLA definido e de data de conclusão válida.
- **Melhoria da fonte:** definir SLA por criticidade e categoria.

### 3.5 N_criticos_alta
- **Definição:** número de chamados com criticidade alta por campus.
- **Sentido:** minimizar.
- **Dimensão principal (metadados):** Social.
- **Pesos ODS** — 9: 0,10 · 11: 0,30 · 12: 0,05.
- **Pesos ESG** — E: 0,05 · S: 0,65 · G: 0,30 · **Classe: S**.
- **Status no snapshot:** **lacuna** (zerado/constante no snapshot atual — sem variância).
- **Limite atual:** depende de criticidade preenchida e confiável na fonte.
- **Melhoria da fonte:** validar criticidade da fonte.

### 3.6 N_em_espaco_coletivo
- **Definição:** número de chamados em espaços de uso coletivo por campus.
- **Sentido:** contextual.
- **Dimensão principal (metadados):** Social.
- **Pesos ODS** — 9: 0,05 · 11: 0,25 · 12: 0,05.
- **Pesos ESG** — E: 0,05 · S: 0,75 · G: 0,20 · **Classe: S**.
- **Status no snapshot:** **ativo** (há variação entre campi).
- **Limite atual:** heurística por título pode subcontar espaços coletivos.
- **Melhoria da fonte:** usar descrição, local e categoria quando disponíveis.

### 3.7 Densidade_chamados_por_1000m2
- **Definição:** chamados por 1.000 m² de área construída do campus.
- **Sentido:** minimizar.
- **Dimensão principal (metadados):** Ambiental / ODS 11.
- **Pesos ODS** — 9: 0,00 · 11: 0,05 · 12: 0,05.
- **Pesos ESG** — E: 0,45 · S: 0,25 · G: 0,30 · **Classe: E**.
- **Status no snapshot:** **lacuna** (zerado por falta de área por campus).
- **Limite atual:** depende de área construída por campus (ver
  `dados/modelo_area_campus.json`, hoje pendente).
- **Melhoria da fonte:** materializar área construída por campus em `modelo_area_campus`.

### 3.8 Razao_preventiva_corretiva
- **Definição:** relação entre manutenção preventiva e corretiva por campus.
- **Sentido:** maximizar.
- **Dimensão principal (metadados):** Ambiental / Governança.
- **Pesos ODS** — 9: 0,05 · 11: 0,05 · 12: 0,30.
- **Pesos ESG** — E: 0,50 · S: 0,10 · G: 0,40 · **Classe: E**.
- **Status no snapshot:** **ativo** (há variação entre campi).
- **Cálculo (corrigido em 2026-06-20):** em `motor_ods.py`, passou a ser a **proporção
  de preventiva** `n_prev/(n_prev+n_corr)`, limitada a [0,1] — 1,0 quando só há
  preventiva, 0,0 quando só há corretiva, 0,5 no equilíbrio. A versão anterior devolvia
  `float(n_prev)` (contagem absoluta) quando `n_corr == 0`, gerando valores na casa das
  centenas/milhar (ex.: ~998, ~1214, ~1366) em escala incompatível, que distorciam a
  normalização min–max deste indicador (sentido `maximizar`). **Os snapshots gerados
  antes da correção ainda contêm os valores antigos — reexecutar o motor para
  regenerar.** O nome histórico da coluna foi preservado.
- **Estado intermediário (1ª regeneração 2026-06-20):** com o cálculo corrigido mas a
  heurística antiga, os valores ficaram `1, 0, 1, 1, 1` — quase constantes, porque a
  heurística procurava a substring `corretiv`, **inexistente na taxonomia de `COL_CAT_IA`**,
  fixando `n_corr ≡ 0`. A proporção colapsava em 1,0 (o único `0` era o campus quase-vazio
  Maria Felipa). Pela regra de Zuur, isso configura **quase-lacuna**, e o indicador foi
  temporariamente excluído do score pelo guard de "valor dominante" do dashboard.
- **Correção da heurística (2ª correção 2026-06-20, ratificada):** a inspeção da fonte
  (13.872 chamados classificados) mostrou que `COL_CAT_IA` **não tem rótulo "corretiva"**:
  `Manutenção Preventiva > …` é o único ramo nomeado e 4.207 chamados o contêm; todos os
  demais chamados classificados são reativos, isto é, corretivos por definição. O motor
  (`malha-ods-esg` **e** hub `malha-ia`) passou a definir `n_corr` **por exclusão**:
  qualquer chamado classificado (não vazio) que não seja preventiva. Resultado por campus:
  **≈ 0,26–0,34** (Jorge Amado 0,268; Paulo Freire 0,330; Sosígenes 0,336; Reitoria 0,261;
  Maria Felipa 0,000). O indicador **volta a ser ativo**, com variação real entre campi.
- **Melhoria futura:** se a classificação de origem passar a marcar "corretiva" de forma
  explícita, usar o rótulo direto em vez da definição por exclusão.

### 3.9 Valor_total_gasto_R$
- **Definição:** valor total registrado, em reais, gasto com chamados por campus.
- **Sentido:** minimizar.
- **Dimensão principal (metadados):** Governança / ODS 12.
- **Pesos ODS** — 9: 0,00 · 11: 0,00 · 12: 0,20.
- **Pesos ESG** — E: 0,20 · S: 0,05 · G: 0,75 · **Classe: G**.
- **Status no snapshot:** **ativo** (há variação entre campi).
- **Limite atual:** não representa custo total se há chamados sem valor; cobertura de
  valor é parcial.
- **Melhoria da fonte:** separar gasto registrado, gasto médio, custo por m² e cobertura
  de valor.

### 3.10 N_chamados_repetidos
- **Definição:** número de chamados recorrentes (mesmo local/ativo) por campus.
- **Sentido:** minimizar.
- **Dimensão principal (metadados):** Governança / ODS 12.
- **Pesos ODS** — 9: 0,00 · 11: 0,00 · 12: 0,10.
- **Pesos ESG** — E: 0,30 · S: 0,20 · G: 0,50 · **Classe: G**.
- **Status no snapshot:** **lacuna** (zerado por falta de chave de recorrência).
- **Limite atual:** depende de chave de local/ativo/categoria.
- **Melhoria da fonte:** criar chave de local/ativo/categoria para recorrência.

## 4. Quadro-síntese de status (snapshot atual)

| Indicador | Sentido | Classe ESG | Status | Motivo do status |
|---|---|---|---|---|
| N_chamados_total | minimizar | G | ativo | há variação entre campi |
| N_infra_critica | minimizar | G | ativo | há variação entre campi |
| N_em_espaco_coletivo | contextual | S | ativo | há variação entre campi |
| Razao_preventiva_corretiva | maximizar | E | ativo | há variação entre campi |
| Valor_total_gasto_R$ | minimizar | G | ativo | há variação entre campi |
| Tempo_medio_resolucao_dias | minimizar | G | lacuna | vazio no snapshot |
| Taxa_resolucao_no_prazo | maximizar | G | lacuna | vazio no snapshot |
| N_criticos_alta | minimizar | S | lacuna | constante (sem variância) |
| Densidade_chamados_por_1000m2 | minimizar | E | lacuna | zerado (falta área por campus) |
| N_chamados_repetidos | minimizar | G | lacuna | zerado (falta chave de recorrência) |

**Leitura para o artigo:** no snapshot atual, **5 de 10** indicadores entram no score
composto e no TOPSIS; os demais 5 são lacunas de qualidade da fonte, não resultados.
Esta proporção deve ser reconferida e atualizada a cada execução, pois é determinante
para a robustez do ranking.

**Observação de unidade quase-vazia:** o `Campus Maria Felipa - Jequié`, com volume muito
baixo de chamados no snapshot, comprime o intervalo min–max e pode dominar artificialmente
a normalização. Recomenda-se: (a) reportar o ranking com e sem essa unidade como teste de
sensibilidade; ou (b) definir um critério mínimo de elegibilidade (volume mínimo de
registros) para a unidade entrar no ranking, registrado em metodologia.

## 5. Regra de exclusão (passo de Zuur)

Antes de compor scores, aplicar o passo de homogeneidade/variância do protocolo de
exploração de dados (Zuur, Ieno & Elphick, 2010, DOI 10.1111/j.2041-210X.2009.00001.x):

1. indicador **vazio** no snapshot → `lacuna` (não entra no score);
2. indicador com **variância nula ou quase nula** entre unidades → `lacuna` (não
   discrimina alternativas; inflaria o score artificialmente);
3. distinguir **zero verdadeiro** de **dado ausente** — não tratar ausência como 0, pois
   distorce min–max e TOPSIS;
4. todo indicador excluído permanece visível na auditoria do painel, com o motivo.

Artefatos relacionados: `scripts/gerar_protocolo_zuur.py`, `dados/protocolo_zuur.json`,
[`METODOLOGIA_PROTOCOLO_ZUUR.md`](METODOLOGIA_PROTOCOLO_ZUUR.md).
