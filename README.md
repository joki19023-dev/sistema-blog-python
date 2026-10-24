# Sistema de administración de publicaciones de un blog

Proyecto académico en Python organizado como paquete. Permite listar publicaciones, buscar por título, filtrar por etiqueta y validar los datos registrados.

## Requisitos

- Python 3.9 o superior recomendado.
- No requiere bibliotecas externas.

## Ejecutar el sistema

Desde la carpeta raíz del proyecto, ejecutá:

```bash
python main.py
```

En algunos sistemas puede ser necesario usar `python3 main.py`.

## Ejecutar las pruebas

```bash
python -m unittest discover -s tests -v
```

Las pruebas verifican las búsquedas y filtros sin distinción entre mayúsculas y minúsculas, las claves requeridas, el tipo de dato del autor y el manejo de una entrada no numérica en el menú.

## Organización del proyecto

```text
sistema_blog_github/
├── main.py                  # Punto de entrada; coordina el flujo del programa
├── README.md                # Documentación y pasos de ejecución
├── .gitignore               # Archivos que Git debe ignorar
├── blog/
│   ├── __init__.py           # Declara blog como paquete de Python
│   ├── datos.py              # Perfil, estados, etiquetas y publicaciones de ejemplo
│   ├── menu.py               # Menú y captura de input() del usuario
│   ├── operaciones.py        # Listado, búsqueda y filtrado
│   └── validaciones.py       # Reglas para validar publicaciones
└── tests/
    └── test_blog.py          # Pruebas automatizadas
```

## Responsabilidad de cada módulo

- **`blog/datos.py`:** define `perfil_autor`, `estados_post`, `etiquetas_blog` y `posts`. Incluye dos publicaciones válidas y una incompleta para probar las validaciones.
- **`blog/operaciones.py`:** implementa `listar_posts(lista)`, `buscar_por_titulo(lista, termino)` y `filtrar_por_tag(lista, tag)`. La búsqueda y el filtrado usan `.lower()`.
- **`blog/menu.py`:** contiene `menu()` y `pedir_texto(mensaje)`. La conversión de la opción del menú está protegida con `try-except`, por lo que escribir letras no cierra el programa.
- **`blog/validaciones.py`:** contiene `validar_post(post)`, que comprueba claves obligatorias, campos vacíos, estado, etiquetas y que el autor sea un diccionario con nombre y correo.
- **`main.py`:** conecta los módulos mediante imports del tipo `from blog.modulo import funcion` y ejecuta el bucle principal solo cuando el archivo se inicia directamente.
- **`blog/__init__.py`:** permite reconocer `blog` como paquete.

Los módulos siguen una dependencia simple: `datos.py` no importa otros módulos del proyecto; `validaciones.py` puede leer los estados definidos en datos; `operaciones.py` no depende del menú; y `main.py` coordina las funciones. Así se evitan imports circulares.

## Subir el proyecto a un repositorio público de GitHub

1. Descomprimí el proyecto y abrí la carpeta `sistema_blog_github`.
2. En GitHub, creá un repositorio nuevo con visibilidad **Public**. Podés llamarlo `sistema-blog-python`.
3. Para subir desde una terminal, ejecutá estos comandos dentro de la carpeta del proyecto. Reemplazá `USUARIO` por tu nombre de usuario de GitHub y comprobá que el repositorio remoto esté creado:

   ```bash
   git init
   git add .
   git commit -m "Crear sistema de administración de blog"
   git branch -M main
   git remote add origin https://github.com/USUARIO/sistema-blog-python.git
   git push -u origin main
   ```

4. Abrí la página del repositorio y comprobá que se vean `main.py`, `README.md`, `blog/` y `tests/`.
5. Como comprobación final, ejecutá `python main.py` y después `python -m unittest discover -s tests -v`.

Si preferís usar la web de GitHub, creá el repositorio público y subí **los archivos y carpetas descomprimidos**, no el archivo ZIP como único archivo.

## Funcionalidades incluidas

- Listar publicaciones con sus datos principales.
- Buscar por título sin distinguir entre mayúsculas y minúsculas.
- Filtrar por etiqueta sin distinguir entre mayúsculas y minúsculas.
- Identificar claves faltantes y campos vacíos.
- Comprobar que el autor sea un diccionario.
- Mantener el programa en funcionamiento si se ingresa texto en vez de un número en el menú.
