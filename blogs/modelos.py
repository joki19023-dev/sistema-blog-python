"""Módulo de modelos orientados a objetos para el Blog (Autor, Post y Blog)."""


class Autor:
    """Representa al autor de una publicación del blog."""

    def __init__(self, nombre, bio, redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    def to_dict(self):
        """Convierte la instancia de Autor a un diccionario serializable en JSON."""
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "redes_sociales": self.redes_sociales
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea una instancia de Autor a partir de un diccionario."""
        return cls(
            nombre=datos.get("nombre", "Autor desconocido"),
            bio=datos.get("bio", ""),
            redes_sociales=datos.get("redes_sociales", [])
        )


class Post:
    """Representa una publicación dentro del blog."""

    def __init__(self, id_post, titulo, autor, categoria, tags, estado="publicado"):
        self.id = id_post
        self.titulo = titulo
        self.autor = autor  # Instancia de la clase Autor
        self.categoria = categoria
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        """Convierte la instancia de Post (y su Autor) a un diccionario para JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor.to_dict() if isinstance(self.autor, Autor) else self.autor,
            "categoria": self.categoria,
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, datos):
        """Reconstruye una instancia de Post y su Autor desde un diccionario."""
        datos_autor = datos.get("autor", {})
        autor_obj = Autor.from_dict(datos_autor) if isinstance(datos_autor, dict) else Autor(str(datos_autor), "")
        return cls(
            id_post=datos.get("id", 0),
            titulo=datos.get("titulo", "Sin título"),
            autor=autor_obj,
            categoria=datos.get("categoria", "General"),
            tags=datos.get("tags", []),
            estado=datos.get("estado", "borrador")
        )


class Blog:
    """Centraliza la lógica de negocio y administra la lista de objetos Post."""

    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def agregar_post(self, nuevo_post):
        """Agrega un objeto Post a la lista del blog."""
        self.posts.append(nuevo_post)

    def obtener_siguiente_id(self):
        """Calcula el siguiente ID disponible para un nuevo post."""
        if not self.posts:
            return 1
        return max(post.id for post in self.posts) + 1

    def listar_posts(self, lista_a_mostrar=None):
        """Recorre y muestra en consola una lista de objetos Post."""
        objetivo = self.posts if lista_a_mostrar is None else lista_a_mostrar
        if not objetivo:
            print("No se encontraron publicaciones para mostrar.")
            return []

        for post in objetivo:
            tags_str = ", ".join(post.tags)
            print(
                f"[{post.id}] Título: {post.titulo} | "
                f"Autor: {post.autor.nombre} | "
                f"Categoría: {post.categoria} | "
                f"Tags: [{tags_str}] | "
                f"Estado: {post.estado}"
            )
        return objetivo

    def buscar_por_titulo(self, termino):
        """Filtra los posts cuyo título contenga el término buscado (insensible a mayúsculas)."""
        termino_limpio = termino.lower()
        resultados = [
            post for post in self.posts
            if termino_limpio in post.titulo.lower()
        ]
        self.listar_posts(resultados)
        return resultados

    def filtrar_por_tag(self, tag):
        """Filtra los posts que contengan el tag indicado (insensible a mayúsculas)."""
        tag_limpio = tag.lower()
        resultados = [
            post for post in self.posts
            if tag_limpio in [t.lower() for t in post.tags]
        ]
        self.listar_posts(resultados)
        return resultados