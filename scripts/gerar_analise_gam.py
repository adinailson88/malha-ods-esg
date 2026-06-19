from __future__ import annotations

import csv
import json
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
DADOS = RAIZ / "dados"
CSV_DIR = RAIZ / "dados_csv"
SAIDA_JSON = DADOS / "analise_gam.json"
SAIDA_CSV = CSV_DIR / "analise_gam.csv"
FONTE = DADOS / "indicadores_ods.json"


def _matriz(caminho: Path):
    return json.loads(caminho.read_text(encoding="utf-8"))


def _objetos(matriz):
    cab = [str(c) for c in matriz[0]]
    return [dict(zip(cab, linha)) for linha in matriz[1:] if linha and linha[0]]


def gerar():
    indicadores = _objetos(_matriz(FONTE))
    n = len(indicadores)
    status = "nao_recomendado_para_ajuste_inferencial" if n < 30 else "parcial"
    resultado = {
        "artefato": "analise_gam",
        "eixo": "ods_esg",
        "fonte": str(FONTE.relative_to(RAIZ)).replace("\\", "/"),
        "status_geral": status,
        "alvo": "scores ODS/ESG derivados de indicadores multicriterio",
        "familia_recomendada": "Nao ajustar GAM inferencial com o snapshot atual; usar como extensao futura se houver serie painel campus-mes.",
        "suporte_amostral": {
            "unidades_observacionais": n,
            "minimo_operacional": 30,
            "nivel_atual": "campus",
        },
        "efeitos_aditivos": [
            {
                "termo": "s(indicadores_operacionais)",
                "status": "somente_conceitual",
                "evidencia": "O snapshot atual tem poucos campi; curvas suaves seriam instaveis.",
            },
            {
                "termo": "efeito_campus",
                "status": "descritivo",
                "evidencia": "Manter leitura multicriterio por campus e nao inferir relacoes nao lineares.",
            },
            {
                "termo": "painel campus-mes",
                "status": "futuro",
                "evidencia": "GAM passa a ser adequado se os indicadores forem materializados por campus e mes.",
            },
        ],
        "recomendacao_dashboard": "Mostrar GAM como ferramenta nao aplicada ao ODS/ESG atual por insuficiencia de unidades, evitando inferencia artificial.",
        "proximas_validacoes": [
            "Criar painel temporal campus-mes antes de ajustar GAM.",
            "Preservar a metodologia MCDM como analise principal do eixo ODS/ESG.",
            "Usar o protocolo de Zuur para documentar a insuficiencia amostral.",
        ],
        "limites": [
            "Com poucos campi, qualquer curva suave seria superajustada.",
            "Sem painel temporal ou mais unidades, usar a frase: Informação insuficiente para verificar.",
        ],
    }
    DADOS.mkdir(exist_ok=True)
    CSV_DIR.mkdir(exist_ok=True)
    SAIDA_JSON.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
    with SAIDA_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["campo", "valor"])
        w.writerow(["status_geral", resultado["status_geral"]])
        w.writerow(["familia_recomendada", resultado["familia_recomendada"]])
        w.writerow(["unidades_observacionais", n])
    print(f"Gerado {SAIDA_JSON.relative_to(RAIZ)} e {SAIDA_CSV.relative_to(RAIZ)}")


if __name__ == "__main__":
    gerar()
