def multiplicacion_rusa(x, y):
    """
    Calcula la multiplicación de dos enteros utilizando el método ruso.

    Args:
        x: El primer entero (multiplicando).
        y: El segundo entero (multiplicador).

    Returns:
        El resultado de la multiplicación (entero).
    """
    acumulador = 0
    print("x\ty\tacumulador")
    print(f"{x}\t{y}\t{acumulador}")

    while x > 0:
        if x % 2 == 1:
            acumulador += y
            print(f"{x}\t{y}\t{acumulador}")
        else:
            print(f"{x}\t{y}\t{acumulador}")
        x //= 2  # División entera de x por 2
        y *= 2   # Multiplicación de y por 2

    return acumulador

# Solicitar los dos enteros al usuario
try:
    num1 = int(input("Ingrese el primer entero (x): "))
    num2 = int(input("Ingrese el segundo entero (y): "))

    resultado = multiplicacion_rusa(num1, num2)
    print("\nEl resultado de la multiplicación rusa es:", resultado)

except ValueError:
    print("Error: Por favor, ingrese números enteros válidos.")