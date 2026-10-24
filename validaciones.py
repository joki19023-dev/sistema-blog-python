"""Reglas de validación para las publicaciones del blog."""

from blog.datos import estados_post


CLAVES_REQUERIDAS = ("id", "titulo", "contenido", "estado", "etiquetas", "autor")


def validar_post(post):
    """Retorna True si el post es válido o un texto con los errores detectados."""
    if not isinstance(post, dict):
        return "El registro no es un diccionario."

    errores = []

    # Comprueba las claves antes de acceder a sus valores.
    for clave in CLAVES_REQUERIDAS:
        if clave not in post:
            errores.append(f"falta la clave obligatoria '{clave}'")

    # Los campos de texto requeridos deben existir y no estar vacíos.
    for campo in ("titulo", "contenido", "estado"):
        if campo not in post:
            continue
        valor = post.get(campo)
        if not isinstance(valor, str) or not valor.strip():
            errores.append(f"el campo '{campo}' está vacío o no es texto")

    estado = post.get("estado")
    if isinstance(estado, str) and estado.strip():
        estados_permitidos = {item.lower() for item in estados_post}
        if estado.strip().lower() not in estados_permitidos:
            errores.append(f"el estado '{estado}' no es válido")

    etiquetas = post.get("etiquetas")
    if "etiquetas" in post:
        if not isinstance(etiquetas, list):
            errores.append("el campo 'etiquetas' debe ser una lista")
        elif not etiquetas or not any(
            isinstance(etiqueta, str) and etiqueta.strip() for etiqueta in etiquetas
        ):
            errores.append("el campo 'etiquetas' debe contener al menos una etiqueta no vacía")
        elif any(not isinstance(etiqueta, str) or not etiqueta.strip() for etiqueta in etiquetas):
            errores.append("todas las etiquetas deben ser textos no vacíos")

    autor = post.get("autor")
    if "autor" in post:
        if not isinstance(autor, dict):
            errores.append("el campo 'autor' debe ser un diccionario")
        else:
            for campo_autor in ("nombre", "correo"):
                valor_autor = autor.get(campo_autor)
                if not isinstance(valor_autor, str) or not valor_autor.strip():
                    errores.append(f"el autor debe tener el campo '{campo_autor}' no vacío")

    return True if not errores else "; ".join(errores) + "."
