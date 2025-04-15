# Inicializar una lista vacía para guardar los números
numeros = []

print("Ingrese números para la lista (para terminar, ingrese 'fin'):")

while True:
    entrada = input("> ")
    if entrada.lower() == 'fin':
        break  # Salir del bucle si el usuario ingresa 'fin'
    try:
        numero = float(entrada)  # Convertir la entrada a un número decimal
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número o 'fin'.")

if numeros:  # Verificar si la lista no está vacía
    # Calcular el promedio
    suma = sum(numeros)
    promedio = suma / len(numeros)

    # Encontrar el valor máximo
    maximo = max(numeros)

    # Encontrar el valor mínimo
    minimo = min(numeros)

    # Mostrar los resultados
    print("\nResultados:")
    print(f"Promedio: {promedio}")
    print(f"Valor máximo: {maximo}")
    print(f"Valor mínimo: {minimo}")
else:
    print("\nNo se ingresaron números en la lista.")