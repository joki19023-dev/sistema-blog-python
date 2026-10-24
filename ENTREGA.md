# Entrega del proyecto: sistema de administración de publicaciones

## Objetivo

Reorganizar el programa original en módulos y un paquete de Python llamado `blog`, separando los datos, las operaciones, la interfaz de menú y las validaciones.

## Archivos que integran la entrega

El código entregado está dividido por responsabilidades dentro del mismo repositorio:

- `main.py`: punto de entrada e integración de las funciones.
- `blog/__init__.py`: marca la carpeta `blog` como paquete.
- `blog/datos.py`: perfil de autor, estados permitidos, etiquetas y publicaciones de ejemplo.
- `blog/operaciones.py`: listar, buscar por título y filtrar por etiqueta.
- `blog/menu.py`: lectura y manejo de entradas del usuario.
- `blog/validaciones.py`: reglas de negocio para validar una publicación.
- `tests/test_blog.py`: pruebas automatizadas de las funciones principales.
- `README.md`: instrucciones para ejecutar, probar y publicar el proyecto.
- `.gitignore`: evita incluir archivos generados localmente.

## Criterios de aceptación

1. Existe el paquete `blog` y contiene `__init__.py`.
2. `main.py` importa funciones con `from blog.modulo import funcion`.
3. La validación comprueba claves requeridas, campos vacíos y que el autor sea un diccionario.
4. La búsqueda y el filtrado ignoran mayúsculas y minúsculas mediante `.lower()`.
5. Una entrada no numérica en el menú se controla con `try-except`.
6. La lógica de inicio está protegida por `if __name__ == "__main__":`.
7. Existe un `README.md` con instrucciones de ejecución, pruebas y publicación en GitHub.

## Comandos de ejecución y comprobación

Desde la carpeta raíz:

```bash
python main.py
python -m unittest discover -s tests -v
```

## Nota de publicación

La carpeta está preparada para subir a un repositorio público de GitHub. La publicación real requiere crear o seleccionar el repositorio dentro de una cuenta de GitHub y completar el envío de los archivos según las instrucciones del README.
