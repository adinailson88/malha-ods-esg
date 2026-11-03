#!/usr/bin/env python3
"""Reproduz em Python a soma ponderada e o TOPSIS do dashboard e mede estabilidade (somente leitura).

Uso (na raiz do repositorio):
    python scripts/diagnostico/mcdm_sensibilidade.py [caminho/para/malha-ia/dados/chamados.json]

Sem o caminho de chamados.json, os cenarios que recalculam indicadores sao pulados.
Dependencia: numpy. Replica as funcoes avaliarIndicadores, calcularScores e calcularTOPSIS de dashboard.html.
"""

import json
import sys
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "dados"
DIMS = ["ODS_9_Infraestrutura", "ODS_11_Cidades_Sustentaveis", "ODS_12_Consumo_Responsavel"]
MAPA_PATRIMONIO = {"CJA": "Campus Jorge Amado", "CPF": "Campus Paulo Freire",
                   "CSC": "Campus Sosígenes Costa", "Reitoria": "Reitoria"}


def ler(nome):
    return json.loads((DADOS / nome).read_text(encoding="utf-8"))


def num(v):
    try:
        return None if v in ("", None) else float(v)
    except (TypeError, ValueError):
        return None


def carregar():
    ind = ler("indicadores_ods.json")
    cab = ind[0]
    linhas = [dict(zip(cab, r)) for r in ind[1:]]
    pesos = {r[0]: {"sentido": r[1].lower(), "w": np.array([float(x) for x in r[2:5]])} for r in ler("pesos_ods.json")[1:]}
    return linhas, pesos


def ativos(linhas, pesos):
    usar = []
    for ind in pesos:
        v = [num(r.get(ind)) for r in linhas]
        v = [x for x in v if x is not None]
        if not v or max(v) == min(v):
            continue
        freq = max(v.count(x) for x in set(v))
        if len(v) >= 3 and freq >= len(v) - 1:
            continue
        usar.append(ind)
    return usar


def norm(v, lo, hi, sentido):
    if v is None or hi == lo:
        return 0.0
    n = (v - lo) / (hi - lo)
    if sentido == "minimizar":
        n = 1 - n
    if sentido == "contextual":
        n = 1 - abs(n - 0.5) * 2
    return max(0.0, min(1.0, n))


def pontuar(linhas, pesos, w_override=None):
    """Devolve (geral, topsis) como dicts campus -> valor (0-100)."""
    W = w_override or {k: p["w"] for k, p in pesos.items()}
    uso = [i for i in ativos(linhas, pesos)]
    lim = {i: (min(num(r[i]) for r in linhas if num(r.get(i)) is not None),
               max(num(r[i]) for r in linhas if num(r.get(i)) is not None)) for i in uso}
    geral = {}
    for r in linhas:
        dims = []
        for d in range(3):
            s = tot = 0.0
            for i in uso:
                p = W[i][d]
                s += norm(num(r.get(i)), *lim[i], pesos[i]["sentido"]) * p
                tot += p
            dims.append(s / tot * 100 if tot else 0.0)
        geral[r["Campus"]] = float(np.mean(dims))
    pw = {i: W[i].sum() for i in uso}
    tw = sum(pw.values())
    if tw <= 0:
        return geral, {}
    def val(r, i):
        v = num(r.get(i)) or 0.0
        return norm(v, *lim[i], "contextual") * 100 if pesos[i]["sentido"] == "contextual" else v
    nrm = {i: (np.sqrt(sum(val(r, i) ** 2 for r in linhas)) or 1.0) for i in uso}
    M = {r["Campus"]: {i: val(r, i) / nrm[i] * pw[i] / tw for i in uso} for r in linhas}
    pos, neg = {}, {}
    for i in uso:
        col = [M[c][i] for c in M]
        pos[i], neg[i] = (min(col), max(col)) if pesos[i]["sentido"] == "minimizar" else (max(col), min(col))
    top = {}
    for c, vals in M.items():
        dp = np.sqrt(sum((vals[i] - pos[i]) ** 2 for i in uso))
        dn = np.sqrt(sum((vals[i] - neg[i]) ** 2 for i in uso))
        top[c] = float(dn / (dp + dn) * 100) if dp + dn else 0.0
    return geral, top


def ordem(d):
    return [c for c, _ in sorted(d.items(), key=lambda kv: -kv[1])]


def spearman(a, b):
    cs = list(a)
    ra = {c: i for i, c in enumerate(ordem(a))}
    rb = {c: i for i, c in enumerate(ordem(b))}
    x = np.array([ra[c] for c in cs], float)
    y = np.array([rb[c] for c in cs], float)
    return float(np.corrcoef(x, y)[0, 1]) if len(cs) > 2 else float("nan")


def monte_carlo(linhas, pesos, n=5000, seed=7):
    rng = np.random.default_rng(seed)
    base = {k: p["w"] for k, p in pesos.items()}
    campi = [r["Campus"] for r in linhas]
    topo = {m: {c: 0 for c in campi} for m in ("soma", "topsis")}
    pos = {m: {c: [] for c in campi} for m in ("soma", "topsis")}
    for _ in range(n):
        W = {k: w * rng.uniform(0.5, 1.5, 3) for k, w in base.items()}
        g, t = pontuar(linhas, pesos, W)
        for m, d in (("soma", g), ("topsis", t)):
            o = ordem(d)
            topo[m][o[0]] += 1
            for i, c in enumerate(o):
                pos[m][c].append(i + 1)
    return {m: {c: {"prob_1o": topo[m][c] / n, "posto_medio": float(np.mean(pos[m][c]))} for c in campi} for m in topo}


def razao_corrigida(caminho):
    rows = [r for r in json.loads(Path(caminho).read_text(encoding="utf-8"))[1:] if r[2]]
    cont = {}
    for r in rows:
        c = r[7]
        z = str(r[25]).strip().lower()
        a = cont.setdefault(c, [0, 0])
        if "preventiv" in z:
            a[0] += 1
        elif z:
            a[1] += 1
    return {c: v[0] / (v[0] + v[1]) for c, v in cont.items() if sum(v)}


def area_2025():
    d = ler("patrimonio_imobiliario_campus_ano.json")
    h = d[0]
    out = {}
    for r in d[1:]:
        reg = dict(zip(h, r))
        if reg["Ano"] == 2025:
            out[MAPA_PATRIMONIO[reg["Campus"]]] = float(reg["Area_Utilizacao_m2"])
    return out


def relatar(titulo, linhas, pesos):
    g, t = pontuar(linhas, pesos)
    print(f"\n== {titulo}")
    print("indicadores ativos:", ativos(linhas, pesos))
    print("soma ponderada:", [(c, round(v, 1)) for c, v in sorted(g.items(), key=lambda kv: -kv[1])])
    print("TOPSIS:        ", [(c, round(v, 1)) for c, v in sorted(t.items(), key=lambda kv: -kv[1])])
    print("Spearman entre metodos:", round(spearman(g, t), 2))
    mc = monte_carlo(linhas, pesos)
    for m in mc:
        print(f"Monte Carlo {m} (pesos x U[0,5;1,5], 5000 sorteios):",
              {c.replace('Campus ', ''): (round(v['prob_1o'], 2), round(v['posto_medio'], 2)) for c, v in mc[m].items()})


def main():
    linhas, pesos = carregar()
    relatar("S0 snapshot como publicado (5 unidades)", linhas, pesos)
    sem = [r for r in linhas if "Jequi" not in r["Campus"]]
    relatar("S1 sem Maria Felipa - Jequie (11 chamados)", sem, pesos)
    if len(sys.argv) > 1:
        rz = razao_corrigida(sys.argv[1])
        print("\nRazao preventiva/(preventiva+corretiva) recalculada de chamados.json:", {c: round(v, 3) for c, v in rz.items()})
        s2 = [dict(r, Razao_preventiva_corretiva=rz.get(r["Campus"], 0.0)) for r in sem]
        relatar("S2 S1 com razao preventiva corrigida (proporcao)", s2, pesos)
        ar = area_2025()
        s3 = []
        for r in s2:
            a = ar.get(r["Campus"])
            if not a:
                continue
            q = dict(r)
            for k in ("N_chamados_total", "N_infra_critica", "N_em_espaco_coletivo", "Valor_total_gasto_R$"):
                q[k] = float(r[k]) / a * 1000
            q["Densidade_chamados_por_1000m2"] = float(r["N_chamados_total"]) / a * 1000
            s3.append(q)
        print("\nArea de utilizacao 2025 (patrimonio, m2):", ar)
        relatar("S3 S2 com contagens e gasto por 1000 m2 (area 2025 do patrimonio)", s3, pesos)


if __name__ == "__main__":
    main()
