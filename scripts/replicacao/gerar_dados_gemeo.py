#!/usr/bin/env python3
"""Gera os dados agregados do prototipo de gemeo digital (somente agregados, sem texto de chamados).

Uso (na raiz do repositorio):
    python scripts/replicacao/gerar_dados_gemeo.py <caminho>/malha-ia/dados/chamados.json

Saidas em gemeo_digital/dados/: gemeo.json e dados.js (window.GEMEO), que o painel gemeo_digital/index.html le.
Biblioteca padrao apenas. Datas lidas como AAAA-MM-DD. Semente fixa: a execucao e deterministica.

PROTOTIPO METODOLOGICO. Os criterios, a normalizacao (minimo e maximo na janela) e a incerteza de pesos (SMAA com
pesos uniformes no simplex) ilustram o desenho de docs/auditoria/03_DESENHO_DO_ESTUDO_A1.md; nao sao resultados do artigo.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SAIDA = RAIZ / "gemeo_digital" / "dados"
CAMINHO = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ.parent / "malha-ia" / "dados" / "chamados.json"

CAMPI = ["Campus Jorge Amado", "Campus Paulo Freire", "Campus Sosígenes Costa", "Reitoria"]
CURTO = {"Campus Jorge Amado": "Jorge Amado", "Campus Paulo Freire": "Paulo Freire",
         "Campus Sosígenes Costa": "Sosígenes Costa", "Reitoria": "Reitoria"}
PATRIMONIO = {"CJA": "Campus Jorge Amado", "CPF": "Campus Paulo Freire", "CSC": "Campus Sosígenes Costa", "Reitoria": "Reitoria"}
FAMILIAS = ["Estrutura Predial", "Climatização", "Elétrica", "Hidrossanitária", "TI / Dados / Rede",
            "Instalação de Acessórios e Mobiliário"]
ANOS = list(range(2018, 2027))
ANOS_INDICE = [2022, 2023, 2024, 2025]
CRITERIOS = [("C1", "Demanda"), ("C5", "Custo de OS corrente"), ("C7", "Tendência"), ("C2", "Severidade")]
ABERTOS = {"Processando (atribuído)", "Processando (planejado)", "Novo", "Pendente"}
N_SORTEIOS = 4000
SEMENTE = 20261103
IDX = dict(ID=0, DATA=2, STATUS=3, CAMPUS=7, VALOR=16, OSM_T=23, OSM_D=24, CAT_IA=25, EXEC=28, CRIT=29)


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def familia(cat: str) -> str:
    return str(cat).split(">")[0].strip()


def baixa_confianca(exec_: str) -> bool:
    return "BAIXA_CONF" in str(exec_).upper()


def carregar_area(caminho: Path) -> dict:
    """Devolve {campus: {ano: (area_m2, origem)}}; 2026 projetado com +5% sobre 2025."""
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    h = dados[0]
    out: dict = defaultdict(dict)
    for r in dados[1:]:
        reg = dict(zip(h, r))
        c = PATRIMONIO.get(reg["Campus"])
        if c:
            out[c][int(reg["Ano"])] = (float(reg["Area_Utilizacao_m2"]), "PATRIMONIO")
    for c, serie in out.items():
        ultimo = max(serie)
        if ultimo < 2026:
            serie[ultimo + 1] = (round(serie[ultimo][0] * 1.05, 2), "PROJETADO_5PCT")
    return out


def ranks_medios(valores: list[float]) -> list[float]:
    ordem = sorted(range(len(valores)), key=lambda i: -valores[i])
    r = [0.0] * len(valores)
    i = 0
    while i < len(ordem):
        j = i
        while j + 1 < len(ordem) and valores[ordem[j + 1]] == valores[ordem[i]]:
            j += 1
        medio = (i + j) / 2 + 1
        for k in range(i, j + 1):
            r[ordem[k]] = medio
        i = j + 1
    return r


def spearman(a: list[float], b: list[float]) -> float | None:
    ra, rb = ranks_medios(a), ranks_medios(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    num_ = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))
    return None if den == 0 else num_ / den


def minmax(col: list[float]) -> list[float]:
    lo, hi = min(col), max(col)
    return [0.0 if hi == lo else (v - lo) / (hi - lo) for v in col]


def smaa(matriz: list[list[float]], n_sorteios: int = N_SORTEIOS, semente: int = SEMENTE) -> dict:
    """SMAA-2 sem informacao de preferencia: pesos uniformes no simplex (Dirichlet(1,...,1)).
    matriz: alternativas x criterios (normalizados, maior e melhor prioridade).
    Devolve aceitabilidade de postos (alternativas x postos), posto medio e intervalo p5 a p95."""
    rng = random.Random(semente)
    n, m = len(matriz), len(matriz[0])
    acc = [[0] * n for _ in range(n)]
    historico = [[] for _ in range(n)]
    for _ in range(n_sorteios):
        g = [rng.gammavariate(1.0, 1.0) for _ in range(m)]
        s = sum(g)
        w = [x / s for x in g]
        pont = [sum(wi * v for wi, v in zip(w, linha)) for linha in matriz]
        ordem = sorted(range(n), key=lambda i: -pont[i])
        for posto, i in enumerate(ordem):
            acc[i][posto] += 1
            historico[i].append(posto + 1)
    saida = {"aceitabilidade": [[round(c / n_sorteios, 4) for c in linha] for linha in acc], "posto_medio": [], "p5": [], "p95": []}
    for h in historico:
        h.sort()
        saida["posto_medio"].append(round(sum(h) / len(h), 2))
        saida["p5"].append(h[int(0.05 * (len(h) - 1))])
        saida["p95"].append(h[int(0.95 * (len(h) - 1))])
    return saida


def main():
    bruto = json.loads(CAMINHO.read_text(encoding="utf-8"))
    linhas = [r for r in bruto[1:] if len(r) > IDX["CRIT"] and str(r[IDX["DATA"]]).strip()]
    sha = hashlib.sha256(CAMINHO.read_bytes()).hexdigest()
    area = carregar_area(RAIZ / "dados" / "patrimonio_imobiliario_campus_ano.json")

    painel = defaultdict(lambda: Counter())
    fam = defaultdict(lambda: Counter())
    mensal = defaultdict(Counter)
    aberta = defaultdict(lambda: Counter())
    ultima = max(str(r[IDX["DATA"]])[:10] for r in linhas)
    ref = datetime.strptime(ultima, "%Y-%m-%d")
    for r in linhas:
        c = r[IDX["CAMPUS"]]
        if c not in CAMPI:
            continue
        data = str(r[IDX["DATA"]])
        ano = int(data[:4])
        f = familia(r[IDX["CAT_IA"]])
        valor = num(r[IDX["VALOR"]])
        posto = f == "Posto de trabalho"
        crit = str(r[IDX["CRIT"]]).strip().lower()
        p = painel[(c, ano)]
        p["n"] += 1
        if str(r[IDX["OSM_T"]]).strip() or str(r[IDX["OSM_D"]]).strip():
            p["os"] += 1
        if valor > 0:
            p["valor"] += valor
            if not posto:
                p["valor_corrente"] += valor
            else:
                p["valor_posto"] += valor
        if "preventiv" in str(r[IDX["CAT_IA"]]).lower():
            p["prev"] += 1
        if baixa_confianca(r[IDX["EXEC"]]):
            p["baixa_conf"] += 1
        if crit in ("média", "media", "alta"):
            p["crit_ma"] += 1
        if crit == "alta":
            p["crit_alta"] += 1
        q = fam[(c, f, ano)]
        q["n"] += 1
        if valor > 0 and not posto:
            q["valor_corrente"] += valor
        if crit in ("média", "media", "alta"):
            q["crit_ma"] += 1
        mensal[c][data[:7]] += 1
        if r[IDX["STATUS"]] in ABERTOS:
            idade = (ref - datetime.strptime(data[:10], "%Y-%m-%d")).days
            faixa = "ate30" if idade <= 30 else "d31a90" if idade <= 90 else "d91a365" if idade <= 365 else "mais365"
            aberta[c][faixa] += 1
            aberta[c]["total"] += 1

    def area_de(c, ano):
        return area.get(c, {}).get(ano, (None, None))

    # painel campus e ano
    out_painel = []
    for c in CAMPI:
        for ano in ANOS:
            p = painel.get((c, ano))
            if not p:
                continue
            a, orig = area_de(c, ano)
            n = p["n"]
            out_painel.append({
                "campus": c, "ano": ano, "n": n, "os": p["os"], "os_pct": round(100 * p["os"] / n, 1),
                "valor_corrente": round(p["valor_corrente"], 2), "valor_posto": round(p["valor_posto"], 2),
                "prev": p["prev"], "baixa_conf_pct": round(100 * p["baixa_conf"] / n, 1), "crit_alta": p["crit_alta"],
                "area_m2": a, "area_origem": orig,
                "n_por_1000m2": round(n / a * 1000, 2) if a else None,
                "valor_corrente_por_1000m2": round(p["valor_corrente"] / a * 1000, 2) if a else None,
                "parcial": ano == 2026})

    # indice de prioridade por ano e variante
    def criterios(ano):
        alts = []
        for c in CAMPI:
            a, _ = area_de(c, ano)
            for f in FAMILIAS:
                q = fam.get((c, f, ano), Counter())
                n = q["n"]
                anos_j = [ano - 3 + k for k in range(4)]
                ys = [fam.get((c, f, y), Counter())["n"] for y in anos_j]
                media = sum(ys) / 4
                xs = [0, 1, 2, 3]
                mx = 1.5
                sxx = sum((x - mx) ** 2 for x in xs)
                inc = sum((x - mx) * (y - media) for x, y in zip(xs, ys)) / sxx
                tend = inc / media if media > 0 else 0.0
                sev = q["crit_ma"] / n if n else 0.0
                alts.append({"campus": c, "familia": f, "n": n, "valor_corrente": round(q["valor_corrente"], 2),
                             "tendencia": round(tend, 4), "severidade": round(sev, 4), "area_m2": a})
        return alts

    prioridade = {}
    for ano in ANOS_INDICE:
        alts = criterios(ano)
        prioridade[str(ano)] = {}
        for variante in ("exposicao", "bruto"):
            def c1(a): return a["n"] / a["area_m2"] * 1000 if variante == "exposicao" else a["n"]
            def c5(a): return a["valor_corrente"] / a["area_m2"] * 1000 if variante == "exposicao" else a["valor_corrente"]
            cols = [[c1(a) for a in alts], [c5(a) for a in alts], [a["tendencia"] for a in alts], [a["severidade"] for a in alts]]
            norm = [minmax(col) for col in cols]
            matriz = [[norm[j][i] for j in range(4)] for i in range(len(alts))]
            igual = [sum(linha) / 4 for linha in matriz]
            res = smaa(matriz)
            rk = ranks_medios(igual)
            prioridade[str(ano)][variante] = {
                "alternativas": [{**a, "c": [round(cols[j][i], 4) for j in range(4)], "r": [round(norm[j][i], 4) for j in range(4)],
                                   "escore_igual": round(igual[i], 4), "posto_igual": rk[i],
                                   "aceitabilidade": res["aceitabilidade"][i], "posto_medio": res["posto_medio"][i],
                                   "p5": res["p5"][i], "p95": res["p95"][i]} for i, a in enumerate(alts)]}
        e = prioridade[str(ano)]["exposicao"]["alternativas"]
        b = prioridade[str(ano)]["bruto"]["alternativas"]
        prioridade[str(ano)]["spearman_bruto_exposicao"] = round(spearman([x["escore_igual"] for x in e], [x["escore_igual"] for x in b]), 3)

    # teste exploratorio de validade preditiva (ilustrativo; o indice contem o criterio C1)
    validacao = []
    for ano in ANOS_INDICE[:-1]:
        e_t = prioridade[str(ano)]["exposicao"]["alternativas"]
        e_n = prioridade[str(ano + 1)]["exposicao"]["alternativas"]
        c1_n = [x["c"][0] for x in e_n]
        validacao.append({"ano_indice": ano, "ano_resultado": ano + 1, "n_alternativas": len(e_t),
                          "spearman_indice_vs_demanda_seguinte": round(spearman([x["escore_igual"] for x in e_t], c1_n), 3),
                          "spearman_persistencia_demanda": round(spearman([x["c"][0] for x in e_t], c1_n), 3)})

    gem = {
        "meta": {
            "titulo": "Gêmeo digital de manutenção predial: protótipo metodológico",
            "natureza": "PROTOTIPO. Não são resultados do artigo; ilustra o desenho em docs/auditoria/03_DESENHO_DO_ESTUDO_A1.md.",
            "gerado_em_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "chamados_sha256": sha, "chamados_bytes": CAMINHO.stat().st_size,
            "chamados_preenchidos": len(linhas), "data_mais_recente": ultima,
            "criterios": [{"id": i, "nome": n} for i, n in CRITERIOS],
            "familias": FAMILIAS, "campi": [{"id": c, "curto": CURTO[c]} for c in CAMPI],
            "n_sorteios_smaa": N_SORTEIOS, "semente": SEMENTE,
            "avisos": [
                "Normalização por mínimo e máximo dentro do ano e do conjunto de alternativas: sensível à composição; o desenho final usa referência fixa.",
                "Família técnica vem da classificação por IA (40,6% dos chamados com baixa confiança, concentrada de 2021 em diante).",
                "Severidade usa a criticidade por IA (instável em 2026) e foi calculada sobre 2022 a 2025.",
                "Área por campus: Area_Utilizacao_m2 do patrimônio (equivalência com área construída a confirmar); 2026 projetado em +5%.",
                "Custo é valor de ordens de serviço (16,5% dos chamados), nominal, sem contratação ('Posto de trabalho').",
                "Pesos incertos: SMAA com pesos uniformes no simplex; nenhum painel de especialistas foi consultado.",
                "Maria Felipa (11 chamados em 2026) e a família 'Manutenção Preventiva' ficam fora das alternativas.",
            ]},
        "painel": out_painel,
        "mensal": {c: sorted(mensal[c].items()) for c in CAMPI},
        "carteira_aberta": {c: dict(aberta[c]) for c in CAMPI},
        "prioridade": prioridade,
        "validacao_exploratoria": validacao,
    }
    SAIDA.mkdir(parents=True, exist_ok=True)
    (SAIDA / "gemeo.json").write_text(json.dumps(gem, ensure_ascii=False, indent=1), encoding="utf-8")
    (SAIDA / "dados.js").write_text("window.GEMEO = " + json.dumps(gem, ensure_ascii=False) + ";\n", encoding="utf-8")
    print("gerado:", SAIDA / "gemeo.json", f"({(SAIDA / 'gemeo.json').stat().st_size/1024:.0f} KB)")
    print("spearman bruto x exposicao:", {a: prioridade[a]["spearman_bruto_exposicao"] for a in prioridade})
    print("validacao exploratoria:", validacao)


if __name__ == "__main__":
    main()
