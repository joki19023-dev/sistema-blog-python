"""Módulo de persistencia con JSON: lectura y escritura de posts.json."""

import json
import os
from .modelos import Autor, Post

RUTA_ARCHIVO_JSON = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "posts.json"
)


def obtener_posts_iniciales():
    """Retorna la lista inicial de objetos Post si posts.json aún no existe."""
    autor_principal = Autor(
        nombre="Guido van Rossum",
        bio="Creador del lenguaje de programación Python en el CWI de Ámsterdam.",
        redes_sociales=[
            "https://github.com/gvanrossum",
            "https://gist.github.com/gvanrossum",
            "https://gvanrossum.github.io/"
        ]
    )
    return [
        Post(
            id_post=1,
            titulo="Introducción a Python",
            autor=autor_principal,
            categoria="Programación",
            tags=["python", "desarrollo web"],
            estado="publicado"
        ),
        Post(
            id_post=2,
            titulo="Estructuras de datos en memoria",
            autor=autor_principal,
            categoria="Bases de Datos",
            tags=["python", "bases de datos"],
            estado="publicado"
        ),
        Post(
            id_post=3,
            titulo="El futuro de la inteligencia artificial con Python",
            autor=autor_principal,
            categoria="Tecnología",
            tags=["python", "inteligencia artificial"],
            estado="borrador"
        )
    ]


def guardar_posts(lista_posts, ruta_archivo=RUTA_ARCHIVO_JSON):
    """Convierte los objetos Post a diccionarios y los guarda en el archivo posts.json."""
    datos_json = [post.to_dict() for post in lista_posts]
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos_json, archivo, indent=4, ensure_ascii=False)


def cargar_posts(ruta_archivo=RUTA_ARCHIVO_JSON):
    """Lee el archivo posts.json al iniciar el programa y devuelve una lista de objetos Post."""
    if not os.path.exists(ruta_archivo):
        posts_iniciales = obtener_posts_iniciales()
        guardar_posts(posts_iniciales, ruta_archivo)
        return posts_iniciales

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
            return [Post.from_dict(item) for item in contenido]
    except (json.JSONDecodeError, OSError):
        posts_iniciales = obtener_posts_iniciales()
        guardar_posts(posts_iniciales, ruta_archivo)
        return posts_iniciales