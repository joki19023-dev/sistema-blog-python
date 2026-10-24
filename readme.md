# Sistema de Gestión de Blog con POO y Persistencia JSON

Aplicación de consola en Python que modela un blog utilizando Programación Orientada a Objetos (POO), estructura de paquetes y persistencia de datos en formato JSON.

## Estructura del Repositorio

- `blog/__init__.py`: Inicializador del paquete `blog` que expone las clases y funciones principales.
- `blog/modelos.py`: Define las clases `Autor` (`nombre`, `bio`, `redes_sociales`), `Post` (que reciba una instancia de `Autor` y los datos de la publicación) y `Blog` (que centraliza la lista de objetos `Post` y los métodos para listar, agregar, buscar por título y filtrar por tag).
- `blog/datos.py`: Gestiona la lectura y escritura del archivo `posts.json` mediante el módulo nativo `json`.
- `main.py`: Punto de entrada que instancia la clase `Blog` y ejecuta el menú interactivo en consola.
- `posts.json`: Archivo de almacenamiento persistente con las publicaciones del blog.

## Interacción entre las Clases y el Archivo JSON

1. **Carga inicial (`cargar_posts`)**: Al ejecutar `main.py`, la función `cargar_posts()` de `blog/datos.py` lee el archivo `posts.json` usando `json.load()`. Cada diccionario leído se transforma en una instancia de `Post` (y su correspondiente instancia anidada de `Autor`) mediante los métodos de clase `Post.from_dict()` y `Autor.from_dict()`. Con esa lista de objetos se instancia `Blog`.
2. **Guardado de nuevos posts (`guardar_posts`)**: Cuando el usuario crea una publicación desde el menú, se instancian los objetos `Autor` y `Post` y se agregan a `mi_blog.posts`. Luego, `guardar_posts()` invoca el método `to_dict()` de cada `Post` (el cual a su vez llama a `autor.to_dict()`) para convertir los objetos en diccionarios compatibles con JSON y los guarda en `posts.json` mediante `json.dump()`.

## Cómo Ejecutar el Proyecto

1. Cloná el repositorio y ubicáte en la carpeta raíz del proyecto:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```
2. Ejecutá el archivo principal con Python 3:
   ```bash
   python main.py
   ```
3. Utilizá las opciones del menú numérico (1 al 5) para listar publicaciones, buscar por título, filtrar por etiqueta, crear nuevos posts persistentes en `posts.json` o salir del programa.
