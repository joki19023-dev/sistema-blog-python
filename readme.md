# Sistema de Blog en Python - POO y Persistencia con JSON

Proyecto de consola en Python estructurado con Programación Orientada a Objetos (`Autor`, `Post` y `Blog`) y persistencia de datos mediante el archivo `posts.json`.

## Estructura Actualizada del Repositorio

```text
.
├── blog/
│   ├── __init__.py       # Inicializador del paquete blog
│   ├── modelos.py        # Clases Autor, Post y Blog
│   └── datos.py          # Funciones cargar_posts() y guardar_posts() con el módulo json
├── main.py               # Punto de entrada que instancia la clase Blog y gestiona el menú
├── posts.json            # Base de datos persistente en formato JSON
└── README.md             # Documentación del proyecto
```

## Cómo Interactúan las Clases con el Archivo JSON

1. **Lectura al iniciar (`cargar_posts` en `blog/datos.py`)**:
   Al ejecutar `main.py`, la función `cargar_posts()` abre `posts.json` utilizando `json.load()`. Cada diccionario almacenado en el archivo JSON se convierte en un objeto `Post` (y su correspondiente objeto `Autor` anidado) mediante los métodos `Post.from_dict()` y `Autor.from_dict()`. Con esa lista de instancias `Post` se inicializa el objeto principal `Blog`.

2. **Operaciones en memoria (`Blog` en `blog/modelos.py`)**:
   La clase `Blog` mantiene la lista de objetos `Post` en su atributo `self.posts` y centraliza los métodos `listar_posts()`, `buscar_por_titulo()`, `filtrar_por_tag()` y `agregar_post()`.

3. **Escritura al crear un nuevo post (`guardar_posts` en `blog/datos.py`)**:
   Cuando el usuario crea una publicación desde el menú, se crea una instancia de `Autor` y una instancia de `Post`, y se agrega a `mi_blog.posts`. Inmediatamente, `guardar_posts()` transforma cada objeto `Post` en un diccionario serializable llamando a `post.to_dict()` (que a su vez convierte al objeto `Autor` con `autor.to_dict()`) y guarda la lista completa en `posts.json` mediante `json.dump()`.

## Cómo Ejecutar el Proyecto

1. Cloná el repositorio y entrá a la carpeta raíz del proyecto:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Ejecutá el archivo principal con Python 3:
   ```bash
   python main.py
   ```

3. Elegí una opción del menú interactivo (1 al 5) para listar las publicaciones cargadas desde `posts.json`, buscar por título, filtrar por tag, crear un nuevo post (que se guardará automáticamente en `posts.json`) o salir.
