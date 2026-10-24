"""Pruebas unitarias para las funciones principales del paquete blog."""

import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

from blog.datos import posts
from blog.menu import menu
from blog.operaciones import buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


class OperacionesTests(unittest.TestCase):
    def test_busqueda_titulo_ignora_mayusculas(self):
        encontrados = buscar_por_titulo(posts, "pYtHoN")
        self.assertEqual([post["id"] for post in encontrados], [1])

    def test_filtro_tag_ignora_mayusculas(self):
        encontrados = filtrar_por_tag(posts, "eDuCaCiÓn")
        self.assertEqual([post["id"] for post in encontrados], [2])

    def test_busqueda_vacia_no_devuelve_resultados(self):
        self.assertEqual(buscar_por_titulo(posts, "  "), [])


class ValidacionesTests(unittest.TestCase):
    def test_post_completo_es_valido(self):
        resultado = validar_post(posts[0])
        self.assertIs(resultado, True)

    def test_post_incompleto_reporta_errores(self):
        resultado = validar_post(posts[2])
        self.assertIsInstance(resultado, str)
        self.assertIn("falta la clave obligatoria 'estado'", resultado)
        self.assertIn("el campo 'autor' debe ser un diccionario", resultado)
        self.assertIn("el campo 'contenido' está vacío", resultado)

    def test_detecta_clave_faltante(self):
        post = {
            "id": 10,
            "titulo": "Prueba",
            "contenido": "Contenido",
            "estado": "borrador",
            "etiquetas": ["Python"],
            # Se omite la clave autor.
        }
        resultado = validar_post(post)
        self.assertIsInstance(resultado, str)
        self.assertIn("falta la clave obligatoria 'autor'", resultado)


class MenuTests(unittest.TestCase):
    def test_menu_no_se_cierra_con_entrada_no_numerica(self):
        salida = StringIO()
        with patch("builtins.input", return_value="texto"):
            with redirect_stdout(salida):
                opcion = menu()
        self.assertEqual(opcion, 0)
        self.assertIn("Entrada inválida", salida.getvalue())


if __name__ == "__main__":
    unittest.main()
