"""Funciones de interfaz de consola y captura de entradas del usuario."""


def menu():
    """Muestra el menú y devuelve una opción entera.

    Si se escribe una entrada no numérica, devuelve 0 para volver al menú.
    """
    print("\n========== MENÚ DEL BLOG ==========")
    print("1. Listar publicaciones")
    print("2. Buscar por título")
    print("3. Filtrar por etiqueta")
    print("4. Validar publicaciones")
    print("5. Salir")

    try:
        return int(input("Elegí una opción (1-5): ").strip())
    except ValueError:
        print("Entrada inválida: ingresá un número del 1 al 5.")
        return 0


def pedir_texto(mensaje):
    """Solicita un texto al usuario; centraliza el uso de input() en este módulo."""
    return input(mensaje).strip()
