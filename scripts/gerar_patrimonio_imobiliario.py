#!/usr/bin/env python3
"""Gera snapshots ODS/ESG a partir da aba Patrimonio Imobiliario1."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import tempfile
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from statistics import mean


SPREADSHEET_ID = "1sUk9jEEOWxmtoQHcd0LAY0UXhU76c_7PIV7eQ7JfsMA"
SHEET_GID = "0"
SHEET_NAME = "Patrimônio Imobiliário1"
CSV_EXPORT_URL = (
    f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export"
    f"?format=csv&gid={SHEET_GID}"
)

COLUNAS_ESPERADAS = [
    "Item",
    "Cód.",
    "Descrição",
    "Endereço",
    "Cidade",
    "RIP (Terreno)",
    "RIP (Utilização)",
    "Área (m²) - Terreno",
    "Área (m²) - Utilização",
    "Valores (R$) - Terreno",
    "Valores (R$) - Utilização",
    "Valor Final (Imóvel R$)",
    "Latitude x Longitude",
    "Campus",
]


def numero_br(valor: str | None) -> float | None:
    if valor is None:
        return None
    texto = str(valor).strip()
    if not texto:
        return None
    texto = texto.replace("R$", "").replace("\xa0", " ").strip()
    texto = re.sub(r"[^0-9,\.-]", "", texto)
    if not texto:
        return None
    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")
    try:
        return float(texto)
    except ValueError:
        return None


def dividir_lat_lon(valor: str | None) -> tuple[float | None, float | None]:
    if not valor:
        return None, None
    partes = [p.strip() for p in str(valor).split(",")]
    if len(partes) != 2:
        return None, None
    return numero_br(partes[0]), numero_br(partes[1])


def texto(valor: object) -> str:
    if valor is None:
        return ""
    return str(valor).strip()


def ler_csv_local(caminho: Path) -> list[dict[str, str]]:
    with caminho.open("r", encoding="utf-8-sig", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def baixar_csv(url: str) -> list[dict[str, str]]:
    try:
        with urllib.request.urlopen(url, timeout=30) as resposta:
            texto = resposta.read().decode("utf-8-sig")
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403}:
            raise SystemExit(
                "A planilha nao esta acessivel por export CSV publico. "
                "Exporte a aba Patrimônio Imobiliário1 como CSV e rode "
                "com --csv caminho\\arquivo.csv, ou publique/libere a planilha "
                "para leitura por link."
            ) from exc
        raise
    return list(csv.DictReader(texto.splitlines()))


def ler_google_sheets_autenticado() -> list[dict[str, str]]:
    credencial = os.environ.get("PATRIMONIO_GOOGLE_SERVICE_ACCOUNT_JSON") or os.environ.get("GCP_SA_KEY")
    credencial_arquivo = os.environ.get("PATRIMONIO_GOOGLE_SERVICE_ACCOUNT_FILE") or os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not credencial and not credencial_arquivo:
        raise SystemExit(
            "Credencial Google ausente. Configure o secret GCP_SA_KEY ou "
            "PATRIMONIO_GOOGLE_SERVICE_ACCOUNT_JSON e compartilhe a planilha "
            "com o e-mail da conta de servico."
        )

    try:
        import gspread
    except ImportError as exc:
        raise SystemExit("Dependencia ausente: instale gspread e google-auth.") from exc

    temp_path = None
    try:
        if credencial:
            dados_credencial = json.loads(credencial)
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as tmp:
                json.dump(dados_credencial, tmp)
                temp_path = tmp.name
            credencial_arquivo = temp_path

        cliente = gspread.service_account(filename=credencial_arquivo)
        planilha = cliente.open_by_key(SPREADSHEET_ID)
        aba = planilha.worksheet(SHEET_NAME)
        valores = aba.get_all_values()
        if not valores:
            return []
        headers = valores[0]
        return [dict(zip(headers, linha)) for linha in valores[1:] if any(linha)]
    finally:
        if temp_path:
            try:
                os.unlink(temp_path)
            except OSError:
                pass


def validar_colunas(rows: list[dict[str, str]]) -> None:
    if not rows:
        raise SystemExit("CSV sem linhas de dados.")
    headers = list(rows[0].keys())
    faltantes = [col for col in COLUNAS_ESPERADAS if col not in headers]
    if faltantes:
        raise SystemExit(f"Colunas ausentes no CSV: {', '.join(faltantes)}")


def normalizar_linha(row: dict[str, str]) -> dict[str, object]:
    lat, lon = dividir_lat_lon(row.get("Latitude x Longitude"))
    return {
        "Ano": int(numero_br(row.get("Item")) or 0),
        "Codigo": texto(row.get("Cód.")),
        "Descricao": texto(row.get("Descrição")),
        "Endereco": texto(row.get("Endereço")),
        "Cidade": texto(row.get("Cidade")),
        "RIP_Terreno": texto(row.get("RIP (Terreno)")),
        "RIP_Utilizacao": texto(row.get("RIP (Utilização)")),
        "Area_Terreno_m2": numero_br(row.get("Área (m²) - Terreno")),
        "Area_Utilizacao_m2": numero_br(row.get("Área (m²) - Utilização")),
        "Valor_Terreno_R$": numero_br(row.get("Valores (R$) - Terreno")),
        "Valor_Benfeitoria_R$": numero_br(row.get("Valores (R$) - Utilização")),
        "Valor_Final_R$": numero_br(row.get("Valor Final (Imóvel R$)")),
        "Latitude": lat,
        "Longitude": lon,
        "Campus": texto(row.get("Campus")),
        "Fonte": f"Google Sheets {SPREADSHEET_ID}; aba {SHEET_NAME}",
    }


def soma_valores(rows: list[dict[str, object]], campo: str) -> float:
    return round(sum(float(r[campo]) for r in rows if r.get(campo) is not None), 2)


def agregar_campus_ano(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grupos: dict[tuple[int, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        ano = row.get("Ano")
        campus = row.get("Campus")
        if ano and campus:
            grupos[(int(ano), str(campus))].append(row)

    saida = []
    for (ano, campus), itens in sorted(grupos.items()):
        lats = [float(r["Latitude"]) for r in itens if r.get("Latitude") is not None]
        lons = [float(r["Longitude"]) for r in itens if r.get("Longitude") is not None]
        cidades = sorted({str(r["Cidade"]) for r in itens if r.get("Cidade")})
        saida.append(
            {
                "Ano": ano,
                "Campus": campus,
                "N_Imoveis_Itens": len(itens),
                "Cidades": "; ".join(cidades),
                "Area_Terreno_m2": soma_valores(itens, "Area_Terreno_m2"),
                "Area_Utilizacao_m2": soma_valores(itens, "Area_Utilizacao_m2"),
                "Valor_Terreno_R$": soma_valores(itens, "Valor_Terreno_R$"),
                "Valor_Benfeitoria_R$": soma_valores(itens, "Valor_Benfeitoria_R$"),
                "Valor_Final_R$": soma_valores(itens, "Valor_Final_R$"),
                "Latitude_Media": round(mean(lats), 8) if lats else None,
                "Longitude_Media": round(mean(lons), 8) if lons else None,
                "Fonte": f"Google Sheets {SPREADSHEET_ID}; aba {SHEET_NAME}",
            }
        )
    return saida


def selecionar_mapa(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    anos = [int(r["Ano"]) for r in rows if r.get("Ano")]
    if not anos:
        return []
    ano_final = max(anos)
    return [
        {
            "Ano": r["Ano"],
            "Campus": r["Campus"],
            "Codigo": r["Codigo"],
            "Descricao": r["Descricao"],
            "Cidade": r["Cidade"],
            "Endereco": r["Endereco"],
            "Latitude": r["Latitude"],
            "Longitude": r["Longitude"],
            "Area_Terreno_m2": r["Area_Terreno_m2"],
            "Area_Utilizacao_m2": r["Area_Utilizacao_m2"],
            "Valor_Final_R$": r["Valor_Final_R$"],
        }
        for r in rows
        if r.get("Ano") == ano_final and r.get("Latitude") is not None and r.get("Longitude") is not None
    ]


def tabela_json(headers: list[str], rows: list[dict[str, object]]) -> list[list[object]]:
    return [headers] + [[row.get(h, "") for h in headers] for row in rows]


def escrever_json(caminho: Path, payload: object) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera dados patrimoniais por campus/ano.")
    parser.add_argument("--csv", help="CSV exportado da aba Patrimônio Imobiliário1.")
    parser.add_argument("--google-auth", action="store_true", help="Ler a planilha via conta de servico.")
    parser.add_argument("--url", default=CSV_EXPORT_URL, help="URL CSV da aba.")
    parser.add_argument("--saida", default="dados")
    args = parser.parse_args()

    if args.google_auth:
        rows = ler_google_sheets_autenticado()
    elif args.csv:
        rows = ler_csv_local(Path(args.csv))
    else:
        rows = baixar_csv(args.url)
    validar_colunas(rows)
    normalizados = [normalizar_linha(row) for row in rows if row.get("Item") and row.get("Campus")]
    por_campus_ano = agregar_campus_ano(normalizados)
    mapa = selecionar_mapa(normalizados)

    saida = Path(args.saida)
    headers_raw = list(normalizados[0].keys()) if normalizados else []
    headers_agregado = list(por_campus_ano[0].keys()) if por_campus_ano else []
    headers_mapa = list(mapa[0].keys()) if mapa else []

    escrever_json(saida / "patrimonio_imobiliario.json", tabela_json(headers_raw, normalizados))
    escrever_json(saida / "patrimonio_imobiliario_campus_ano.json", tabela_json(headers_agregado, por_campus_ano))
    escrever_json(saida / "patrimonio_imobiliario_mapa.json", tabela_json(headers_mapa, mapa))

    print(f"Linhas patrimoniais: {len(normalizados)}")
    print(f"Linhas campus/ano: {len(por_campus_ano)}")
    print(f"Pontos no mapa: {len(mapa)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
