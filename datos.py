"""Datos iniciales usados por el sistema del blog.

Este módulo solo define datos. No importa funciones de otros módulos,
lo que ayuda a evitar dependencias circulares.
"""

perfil_autor = {
    "nombre": "Ana Pérez",
    "correo": "ana.perez@example.com",
    "bio": "Escritora sobre tecnología y aprendizaje.",
}

estados_post = ["borrador", "publicado", "archivado"]

etiquetas_blog = ["Python", "Tecnología", "Educación", "Programación"]

posts = [
    {
        "id": 1,
        "titulo": "Introducción a Python",
        "contenido": "Python es un lenguaje de programación claro y versátil.",
        "estado": "publicado",
        "etiquetas": ["Python", "Programación"],
        "autor": perfil_autor.copy(),
    },
    {
        "id": 2,
        "titulo": "La tecnología en el aula",
        "contenido": "Las herramientas digitales pueden apoyar el aprendizaje.",
        "estado": "borrador",
        "etiquetas": ["Tecnología", "Educación"],
        "autor": perfil_autor.copy(),
    },
    {
        # Post intencionalmente incompleto: sirve para probar las validaciones.
        "id": 3,
        "titulo": "Publicación incompleta",
        "contenido": "   ",
        "etiquetas": [],
        "autor": "Ana Pérez",  # Debe ser un diccionario, no texto.
        # Falta la clave obligatoria "estado".
    },
]
