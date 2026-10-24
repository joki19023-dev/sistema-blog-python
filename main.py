"""Punto de entrada del sistema de administración de publicaciones."""

from blog.datos import posts
from blog.menu import menu, pedir_texto
from blog.operaciones import buscar_por_titulo, filtrar_por_tag, listar_posts
from blog.validaciones import validar_post


def ejecutar_programa():
    """Coordina el menú y las operaciones disponibles en el paquete blog."""
    while True:
        opcion = menu()

        if opcion == 1:
            listar_posts(posts)
        elif opcion == 2:
            termino = pedir_texto("Ingresá el título o una parte del título: ")
            listar_posts(buscar_por_titulo(posts, termino))
        elif opcion == 3:
            tag = pedir_texto("Ingresá la etiqueta que querés buscar: ")
            listar_posts(filtrar_por_tag(posts, tag))
        elif opcion == 4:
            print("\n========== VALIDACIÓN DE PUBLICACIONES ==========")
            for indice, post in enumerate(posts, start=1):
                resultado = validar_post(post)
                titulo = post.get("titulo", "[Sin título]") if isinstance(post, dict) else "[Registro inválido]"
                if resultado is True:
                    print(f"Post {indice} - '{titulo}': VÁLIDO")
                else:
                    print(f"Post {indice} - '{titulo}': INVÁLIDO. {resultado}")
        elif opcion == 5:
            print("Programa finalizado. ¡Hasta luego!")
            break
        elif opcion == 0:
            # menu() ya explicó que la entrada no era numérica.
            continue
        else:
            print("Opción fuera de rango. Elegí un número del 1 al 5.")


if __name__ == "__main__":
    ejecutar_programa()
