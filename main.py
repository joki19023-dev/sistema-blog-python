"""Punto de entrada principal del sistema de Blog."""

from blog.modelos import Autor, Post, Blog
from blog.datos import cargar_posts, guardar_posts


def mostrar_menu():
    """Muestra las opciones del menú principal y retorna la selección del usuario."""
    print("\n--- MENÚ DEL BLOG ---")
    print("1. Listar todos los posts")
    print("2. Buscar posts por título")
    print("3. Filtrar posts por tag")
    print("4. Crear un nuevo post")
    print("5. Salir")
    try:
        return int(input("Seleccioná una opción (1-5): "))
    except ValueError:
        print("Error: Debés ingresar un número válido.")
        return -1


def crear_post_interactivo(mi_blog):
    """Solicita los datos por consola, instancia Autor y Post, y guarda en posts.json."""
    titulo = input("Título del post: ").strip()
    categoria = input("Categoría: ").strip()
    tags_entrada = input("Tags (separados por coma): ").strip()
    nombre_autor = input("Nombre del autor: ").strip()
    bio_autor = input("Biografía del autor: ").strip()

    if not titulo or not categoria or not nombre_autor:
        print("Error: El título, la categoría y el nombre del autor son obligatorios.")
        return

    lista_tags = [t.strip().lower() for t in tags_entrada.split(",") if t.strip()]
    if not lista_tags:
        lista_tags = ["general"]

    autor_obj = Autor(nombre=nombre_autor, bio=bio_autor)
    nuevo_post = Post(
        id_post=mi_blog.obtener_siguiente_id(),
        titulo=titulo,
        autor=autor_obj,
        categoria=categoria,
        tags=lista_tags,
        estado="publicado"
    )

    mi_blog.agregar_post(nuevo_post)
    guardar_posts(mi_blog.posts)
    print(f"Post '{nuevo_post.titulo}' creado y guardado en posts.json con éxito.")


if __name__ == "__main__":
    # Instancia la clase Blog cargando los datos desde posts.json
    mi_blog = Blog(cargar_posts())

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            mi_blog.listar_posts()

        elif opcion == 2:
            termino = input("Ingresá el término de búsqueda: ")
            mi_blog.buscar_por_titulo(termino)

        elif opcion == 3:
            tag = input("Ingresá el tag a filtrar: ")
            mi_blog.filtrar_por_tag(tag)

        elif opcion == 4:
            crear_post_interactivo(mi_blog)

        elif opcion == 5:
            print("¡Gracias por usar el sistema del blog! ¡Hasta pronto!")
            break

        elif opcion != -1:
            print("Opción fuera de rango. Elegí un número entre 1 y 5.")