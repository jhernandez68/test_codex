"""Calculadora básica en consola con 4 operaciones y dos números."""


def mostrar_menu() -> None:
    """Muestra el menú principal de operaciones."""
    print("\n=== Calculadora Básica ===")
    print("Esta calculadora solo opera con dos números.")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")


def solicitar_numero(mensaje: str) -> float:
    """Solicita un número al usuario y valida la entrada."""
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")


def ejecutar_calculadora() -> None:
    """Ejecuta el flujo principal de la calculadora."""
    mostrar_menu()
    opcion = input("Selecciona la operación (1, 2, 3 o 4): ")

    if opcion not in {"1", "2", "3", "4"}:
        print("Opción inválida. Debes elegir 1, 2, 3 o 4.")
        return

    numero_1 = solicitar_numero("Ingresa el primer número (solo se usan dos números): ")
    numero_2 = solicitar_numero("Ingresa el segundo número (solo se usan dos números): ")

    if opcion == "1":
        resultado = numero_1 + numero_2
        operacion = "suma"
    elif opcion == "2":
        resultado = numero_1 - numero_2
        operacion = "resta"
    elif opcion == "3":
        resultado = numero_1 * numero_2
        operacion = "multiplicación"
    else:
        if numero_2 == 0:
            print("No se puede dividir entre cero.")
            return
        resultado = numero_1 / numero_2
        operacion = "división"

    print(f"El resultado de la {operacion} es: {resultado}")


if __name__ == "__main__":
    ejecutar_calculadora()
