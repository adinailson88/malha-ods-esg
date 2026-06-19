#!/usr/bin/env python3
"""Gera diagnostico de exploracao de dados segundo Zuur et al. (2010)."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DADOS = RAIZ / "dados"
CSV_DIR = RAIZ / "dados_csv"
SAIDA_JSON = DADOS / "protocolo_zuur.json"
SAIDA_CSV = CSV_DIR / "protocolo_zuur.csv"

REFERENCIA = (
    "Zuur, A.F., Ieno, E.N. & Elphick, C.S. (2010). A protocol for data "
    "exploration to avoid common statistical problems. Methods in Ecology and "
    "Evolution, 1(1), 3-14. doi:10.1111/j.2041-210X.2009.00001.x"
)


def carregar(nome: str) -> list:
    caminho = DADOS / nome
    if not caminho.exists():
        return []
    return json.loads(caminho.read_text(encoding="utf-8"))


def numero(valor) -> float | None:
    if isinstance(valor, (int, float)) and not isinstance(valor, bool):
        return float(valor)
    if isinstance(valor, str):
        texto = valor.strip().replace("R$", "").replace("%", "").replace(".", "").replace(",", ".")
        if not texto:
            return None
        try:
            return float(texto)
        except ValueError:
            return None
    return None


def linhas_tabela(tabela: list) -> tuple[list[str], list[list]]:
    if not tabela or not isinstance(tabela[0], list):
        return [], []
    return [str(c) for c in tabela[0]], [r for r in tabela[1:] if any(str(c).strip() for c in r)]


def resumo_colunas(cab: list[str], linhas: list[list]) -> list[dict]:
    out = []
    for i, nome in enumerate(cab[1:], start=1):
        vals = [numero(r[i]) for r in linhas if len(r) > i]
        vals = sorted(v for v in vals if v is not None)
        if not vals:
            out.append({"indicador": nome, "status": "Informação insuficiente para verificar."})
            continue
        media = sum(vals) / len(vals)
        out.append({
            "indicador": nome,
            "n": len(vals),
            "min": round(vals[0], 4),
            "max": round(vals[-1], 4),
            "media": round(media, 4),
            "zeros": sum(1 for v in vals if v == 0),
        })
    return out


def main() -> int:
    indicadores = carregar("indicadores_ods.json")
    pesos = carregar("pesos_ods.json")
    classificacao = carregar("classificacao_ods_esg.json")
    area = carregar("area_manutencao.json")

    cab, linhas = linhas_tabela(indicadores)
    resumo = resumo_colunas(cab, linhas)
    n_campi = len(linhas)
    n_indicadores = max(0, len(cab) - 1)
    n_pesos = max(0, len(pesos) - 1) if isinstance(pesos, list) else 0
    n_class = max(0, len(classificacao) - 1) if isinstance(classificacao, list) else 0

    passos = [
        {"passo": 1, "titulo": "Outliers em indicadores brutos", "status": "verificado", "evidencia": "dados/indicadores_ods.json", "resultado": resumo, "mudanca_minima": "Exibir amplitude e zeros por indicador antes dos scores normalizados."},
        {"passo": 2, "titulo": "Homogeneidade de variancia", "status": "precisa calcular", "evidencia": "dados/indicadores_ods.json", "resultado": {"status": "Informação insuficiente para verificar."}, "mudanca_minima": "Adicionar variancia/escala por indicador para evitar dominancia de indicadores monetarios ou de contagem."},
        {"passo": 3, "titulo": "Normalidade", "status": "nao aplicavel como pressuposto principal", "evidencia": "dados/indicadores_ods.json", "resultado": {"n_campi": n_campi, "observacao": "Painel multicriterio usa normalizacao min-max, nao inferencia gaussiana."}, "mudanca_minima": "Registrar normalidade apenas como diagnostico descritivo se a amostra de campi crescer."},
        {"passo": 4, "titulo": "Zeros ou ausencia estrutural", "status": "verificado", "evidencia": "dados/indicadores_ods.json", "resultado": {"indicadores": [{"indicador": r["indicador"], "zeros": r.get("zeros")} for r in resumo]}, "mudanca_minima": "Separar zero operacional real de campo vazio antes da normalizacao."},
        {"passo": 5, "titulo": "Colinearidade entre indicadores", "status": "precisa calcular", "evidencia": "dados/indicadores_ods.json", "resultado": {"status": "Informação insuficiente para verificar."}, "mudanca_minima": "Adicionar matriz de correlacao/VIF entre indicadores quando houver amostra suficiente."},
        {"passo": 6, "titulo": "Relacoes entre resposta e covariaveis", "status": "adaptado", "evidencia": "dados/pesos_ods.json", "resultado": {"n_indicadores": n_indicadores, "n_pesos": n_pesos}, "mudanca_minima": "Documentar que a relacao Y-X e substituida por pesos multicriterio ODS."},
        {"passo": 7, "titulo": "Interacoes", "status": "adaptado", "evidencia": "dados/classificacao_ods_esg.json", "resultado": {"n_classificacoes": n_class}, "mudanca_minima": "Tratar interacao como leitura indicador x ODS x pilar ESG."},
        {"passo": 8, "titulo": "Independencia espacial/temporal", "status": "precisa calcular", "evidencia": "dados/area_manutencao.json", "resultado": {"linhas_area": max(0, len(area) - 1) if isinstance(area, list) else 0}, "mudanca_minima": "Adicionar verificacao de dependencia por campus/area quando houver coordenadas ou serie temporal por campus."},
    ]

    out = {
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "repositorio": "malha-ods-esg",
        "eixo": "indicadores ODS/ESG multicriterio",
        "referencia": REFERENCIA,
        "escopo": "Exploracao dos indicadores brutos e pesos publicados; sem certificacao oficial ODS/ESG.",
        "diagnostico_do_que_falta": [
            "Falta matriz de correlacao/VIF entre indicadores.",
            "Falta regra explicita para zeros estruturais versus dados ausentes.",
            "Falta diagnostico de dependencia por campus ou area institucional.",
        ],
        "passos": passos,
        "metodo_artigo": (
            "No eixo ODS/ESG, o protocolo de Zuur et al. (2010) foi adaptado a indicadores "
            "multicriterio por campus. Antes da composicao dos scores, os indicadores brutos "
            "devem ser inspecionados quanto a outliers, zeros estruturais, escalas discrepantes, "
            "colinearidade e dependencia por unidade institucional. Os passos de relacao Y-X e "
            "interacao sao reinterpretados como pesos indicador-ODS e leitura indicador-ODS-ESG."
        ),
    }

    SAIDA_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    CSV_DIR.mkdir(exist_ok=True)
    with SAIDA_CSV.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        writer.writerow(["passo", "titulo", "status", "evidencia", "mudanca_minima"])
        for p in passos:
            writer.writerow([p["passo"], p["titulo"], p["status"], p["evidencia"], p["mudanca_minima"]])
    print(f"OK {SAIDA_JSON}")
    print(f"OK {SAIDA_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
