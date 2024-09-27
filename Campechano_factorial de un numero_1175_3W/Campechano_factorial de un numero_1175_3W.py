print(" ")
print("Alvaro Campechano 3W")
print(" ")
def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
    n (int): El número del cual se desea calcular el factorial.

    Retorna:
    int: El factorial del número n.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    """
    Función principal que solicita un número entero al usuario
    y calcula su factorial.
    """
    try:
        # Solicitar al usuario un número entero
        n = int(input("Ingresa un número entero no negativo: "))
        
        # Calcular el factorial
        resultado = calcular_factorial(n)
        
        # Mostrar el resultado
        print(f"El factorial de {n} es: {resultado}")
    
    except ValueError as e:
        print(f"Entrada no válida: {e}")

# Ejecutar la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
