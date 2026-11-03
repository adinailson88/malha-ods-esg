"""Testes do prototipo de gemeo digital (biblioteca padrao). Executar: python -m unittest tests.test_gemeo -v"""

import importlib.util
import json
import re
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
GEM = RAIZ / "gemeo_digital"
spec = importlib.util.spec_from_file_location("gerar_dados_gemeo", RAIZ / "scripts" / "replicacao" / "gerar_dados_gemeo.py")
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


class TestFuncoes(unittest.TestCase):
    def test_spearman_monotonico(self):
        self.assertAlmostEqual(g.spearman([1, 2, 3, 4], [10, 20, 30, 40]), 1.0)
        self.assertAlmostEqual(g.spearman([1, 2, 3, 4], [4, 3, 2, 1]), -1.0)

    def test_spearman_constante_nao_definido(self):
        self.assertIsNone(g.spearman([1, 1, 1], [1, 2, 3]))

    def test_ranks_medios_empate(self):
        self.assertEqual(g.ranks_medios([5, 5, 1]), [1.5, 1.5, 3.0])

    def test_minmax(self):
        self.assertEqual(g.minmax([2, 4, 6]), [0.0, 0.5, 1.0])
        self.assertEqual(g.minmax([3, 3]), [0.0, 0.0])

    def test_smaa_deterministico_e_normalizado(self):
        m = [[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]]
        a = g.smaa(m, 500, 7)
        b = g.smaa(m, 500, 7)
        self.assertEqual(a, b)
        for linha in a["aceitabilidade"]:
            self.assertAlmostEqual(sum(linha), 1.0, places=2)
        for j in range(3):
            self.assertAlmostEqual(sum(l[j] for l in a["aceitabilidade"]), 1.0, places=2)

    def test_smaa_dominante_fica_em_primeiro(self):
        m = [[1.0, 1.0], [0.2, 0.1], [0.0, 0.0]]
        a = g.smaa(m, 300, 1)
        self.assertEqual(a["p5"][0], 1)
        self.assertEqual(a["p95"][2], 3)


class TestContratoDeDados(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads((GEM / "dados" / "gemeo.json").read_text(encoding="utf-8"))

    def test_chaves_de_topo(self):
        for k in ["meta", "painel", "mensal", "carteira_aberta", "prioridade", "validacao_exploratoria"]:
            self.assertIn(k, self.d)

    def test_meta_declara_prototipo_e_hash(self):
        m = self.d["meta"]
        self.assertRegex(m["chamados_sha256"], r"^[0-9a-f]{64}$")
        self.assertIn("PROTOTIPO", m["natureza"])
        self.assertEqual(m["n_sorteios_smaa"], g.N_SORTEIOS)
        self.assertEqual(len(m["campi"]), 4)

    def test_prioridade_tem_24_alternativas_por_ano_e_variante(self):
        for ano in map(str, g.ANOS_INDICE):
            for var in ["exposicao", "bruto"]:
                alts = self.d["prioridade"][ano][var]["alternativas"]
                self.assertEqual(len(alts), len(g.CAMPI) * len(g.FAMILIAS))
                for a in alts:
                    self.assertLessEqual(a["p5"], a["p95"])
                    self.assertTrue(1 <= a["p5"] and a["p95"] <= len(alts))
                    self.assertTrue(1 <= a["posto_medio"] <= len(alts))
                    self.assertAlmostEqual(sum(a["aceitabilidade"]), 1.0, places=2)
                    self.assertTrue(all(0.0 <= x <= 1.0 for x in a["r"]))

    def test_painel_cobre_campi_e_anos(self):
        pares = {(p["campus"], p["ano"]) for p in self.d["painel"]}
        for c in g.CAMPI:
            for a in g.ANOS:
                self.assertIn((c, a), pares)

    def test_sem_dado_simulado_nem_texto_de_chamado(self):
        txt = (GEM / "dados" / "gemeo.json").read_text(encoding="utf-8")
        self.assertNotIn("SIMULADO", txt)
        self.assertLess(len(txt), 400_000)  # agregados apenas; texto de chamados inflaria o arquivo

    def test_dados_js_espelha_json(self):
        js = (GEM / "dados" / "dados.js").read_text(encoding="utf-8")
        corpo = js[js.index("=") + 1:].strip().rstrip(";")
        self.assertEqual(json.loads(corpo), self.d)


class TestPagina(unittest.TestCase):
    def test_pagina_sem_recurso_externo_e_com_aviso(self):
        html = (GEM / "index.html").read_text(encoding="utf-8")
        externos = [u for u in re.findall(r"(?:src|href)=\"(https?://[^\"]+)", html)]
        self.assertEqual(externos, [])
        self.assertIn("NÃO É RESULTADO DE ARTIGO", html)
        self.assertIn("dados/dados.js", html)


if __name__ == "__main__":
    unittest.main()
