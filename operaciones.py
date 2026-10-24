"""Operaciones para listar, buscar y filtrar publicaciones."""


def listar_posts(lista):
    """Imprime una lista de publicaciones con un formato legible."""
    if not lista:
        print("No se encontraron publicaciones.")
        return

    print(f"\nPublicaciones encontradas: {len(lista)}")
    print("-" * 54)
    for post in lista:
        if not isinstance(post, dict):
            print("Registro inválido: se esperaba un diccionario.")
            print("-" * 54)
            continue

        titulo = post.get("titulo", "[Sin título]")
        contenido = post.get("contenido", "[Sin contenido]")
        estado = post.get("estado", "[Sin estado]")
        etiquetas = post.get("etiquetas", [])
        autor = post.get("autor", {})

        if isinstance(etiquetas, list):
            etiquetas_texto = ", ".join(str(item) for item in etiquetas) or "Sin etiquetas"
        else:
            etiquetas_texto = "Formato de etiquetas inválido"

        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "[Autor sin nombre]")
        else:
            nombre_autor = "[Autor inválido: debe ser un diccionario]"

        print(f"ID: {post.get('id', 'N/D')}")
        print(f"Título: {titulo}")
        print(f"Contenido: {contenido}")
        print(f"Estado: {estado}")
        print(f"Etiquetas: {etiquetas_texto}")
        print(f"Autor: {nombre_autor}")
        print("-" * 54)


def buscar_por_titulo(lista, termino):
    """Devuelve los posts cuyo título contiene el término, sin distinguir caso."""
    if not isinstance(termino, str):
        return []
    termino = termino.strip().lower()
    if not termino:
        return []

    resultados = []
    for post in lista:
        if not isinstance(post, dict):
            continue
        titulo = post.get("titulo", "")
        if isinstance(titulo, str) and termino in titulo.lower():
            resultados.append(post)
    return resultados


def filtrar_por_tag(lista, tag):
    """Devuelve los posts con la etiqueta indicada, ignorando mayúsculas."""
    if not isinstance(tag, str):
        return []
    tag = tag.strip().lower()
    if not tag:
        return []

    resultados = []
    for post in lista:
        if not isinstance(post, dict):
            continue
        etiquetas = post.get("etiquetas", [])
        if not isinstance(etiquetas, list):
            continue
        if any(isinstance(item, str) and item.lower() == tag for item in etiquetas):
            resultados.append(post)
    return resultados
