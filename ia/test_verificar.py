#!/usr/bin/env python3
"""Pruebas de ia/verificar.py. Correr: python3 -m unittest discover -s ia -p 'test_*.py'"""
import re
import unittest

import verificar as v


class Secretos(unittest.TestCase):
    def detecta(self, texto: str) -> bool:
        return any(re.search(p, texto) for p in v.SECRETOS)

    def test_detecta(self):
        # Las muestras se arman al vuelo para que este archivo no dispare el propio escaneo.
        for texto in ("-----BEGIN RSA " + "PRIVATE KEY-----", "sk" + "-" + "a" * 30, "gh" + "p_" + "A1" * 18,
                      "session" + "id=" + "ab12" * 6, "IG" + "Q" + "x" * 45, "EA" + "A" + "b" * 45,
                      "GAME" + "900101" + "HDFRRL09"):
            self.assertTrue(self.detecta(texto), texto)

    def test_no_marca_texto_normal(self):
        for texto in ("La contraseña se la pide Instagram a Emi en su teléfono.", "https://www.instagram.com/reel/C86WDnEuBjB/",
                      "huella 3f2a9c0e1d7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0", "password: nunca se guarda aquí"):
            self.assertFalse(self.detecta(texto), texto)

    def test_edad_de_fuentes(self):
        texto, dias = v.edad_fuentes()
        self.assertIsInstance(dias, int)
        self.assertIn("revisadas el", texto)


if __name__ == "__main__":
    unittest.main()
