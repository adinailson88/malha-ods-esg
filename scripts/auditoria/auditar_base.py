#!/usr/bin/env python3
"""Auditoria agregada e reproduzivel da base de chamados e do patrimonio (somente leitura).

Uso (na raiz do repositorio):
    python scripts/auditoria/auditar_base.py <caminho>/malha-ia/dados/chamados.json [saida.json]

Nao grava texto de chamados: apenas contagens, proporcoes e distribuicoes. Python padrao (sem pandas).
Datas lidas como AAAA-MM-DD, sem inversao de dia e mes. Colunas pelo indice do cabecalho do chamados.json.
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "../malha-ia/dados/chamados.json"
SAIDA = Path(sys.argv[2]) if len(sys.argv) > 2 else RAIZ / "docs" / "auditoria" / "dados" / "auditoria_base.json"
I = dict(ID=0, TITULO=1, DATA=2, STATUS=3, CAMPUS=7, CAT_HIST=12, VALOR=16, GLPI=22, OSM_T=23, OSM_D=24,
         CAT_IA=25, AVAL=27, EXEC=28, CRIT=29)


def val(r, k):
    return str(r[I[k]]).strip() if len(r) > I[k] else ""


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def main():
    bruto = json.loads(Path(CAMINHO).read_text(encoding="utf-8"))
    cab, linhas = bruto[0], bruto[1:]
    cheias = [r for r in linhas if val(r, "DATA")]
    out = {"linhas_total": len(linhas), "linhas_preenchidas": len(cheias), "linhas_vazias": len(linhas) - len(cheias),
           "colunas": len(cab), "colunas_sem_nome": sum(1 for c in cab if not str(c).strip())}
    ids = Counter(val(r, "ID") for r in cheias)
    out["ids_duplicados"] = sum(1 for v in ids.values() if v > 1)
    out["datas_fora_do_padrao_iso"] = sum(1 for r in cheias if not (len(val(r, "DATA")) >= 10 and val(r, "DATA")[4] == "-" and val(r, "DATA")[7] == "-"))
    por = defaultdict(lambda: defaultdict(lambda: Counter()))
    for r in cheias:
        ano = val(r, "DATA")[:4]
        c = val(r, "CAMPUS")
        p = por[c][ano]
        p["n"] += 1
        osv = num(val(r, "VALOR"))
        if osv > 0:
            p["os_valor"] += 1
            p["valor_rs"] += osv
        if val(r, "OSM_T") or val(r, "OSM_D"):
            p["os"] += 1
        if "preventiv" in val(r, "CAT_IA").lower():
            p["prev_ia"] += 1
        if val(r, "CRIT").lower() == "alta":
            p["crit_alta"] += 1
        if val(r, "EXEC").upper().startswith("LSTM_BAIXA") or "BAIXA_CONF" in val(r, "EXEC").upper():
            p["baixa_conf"] += 1
    out["painel_campus_ano"] = {c: {a: {k: (round(v, 2) if isinstance(v, float) else v) for k, v in cnt.items()}
                                    for a, cnt in sorted(anos.items())} for c, anos in por.items()}
    out["status"] = Counter(val(r, "STATUS") for r in cheias).most_common()
    out["criticidade"] = Counter(val(r, "CRIT") for r in cheias).most_common()
    out["executor_classificacao"] = Counter(val(r, "EXEC") for r in cheias).most_common()
    out["categorias_ia_distintas"] = len({val(r, "CAT_IA") for r in cheias})
    out["concordancia_categoria_historica_x_ia"] = round(sum(1 for r in cheias if val(r, "CAT_HIST") == val(r, "CAT_IA")) / len(cheias), 3)
    out["preenchimento_por_coluna"] = {str(cab[j]) or f"coluna_{j}": sum(1 for r in cheias if len(r) > j and str(r[j]).strip() != "") for j in range(len(cab))}
    conf = [num(val(r, "AVAL")) for r in cheias if val(r, "AVAL")]
    conf.sort()
    out["confianca_ia_quantis"] = {q: conf[int(q / 100 * (len(conf) - 1))] for q in (5, 25, 50, 75, 95)} if conf else {}
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    SAIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k not in ("painel_campus_ano", "preenchimento_por_coluna")}, ensure_ascii=False, indent=1))
    print("\nPainel campus x ano (n, OS com valor, % OS, valor R$, preventivos IA, criticidade alta):")
    for c, anos in sorted(out["painel_campus_ano"].items()):
        print(f"\n{c}")
        for a, d in anos.items():
            n = d.get("n", 0)
            print(f"  {a}: n={n:5d} OS={d.get('os_valor',0):4d} ({100*d.get('os_valor',0)/n:4.1f}%) R$={d.get('valor_rs',0):>12,.0f} prev={d.get('prev_ia',0):4d} alta={d.get('crit_alta',0):3d} baixaconf={d.get('baixa_conf',0)}")


if __name__ == "__main__":
    main()
