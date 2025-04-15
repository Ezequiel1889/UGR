# Inicializar las dos listas vacías
lista1 = []
lista2 = []

print("Ingrese los números para la primera lista (para terminar, ingrese 'fin'):")
while True:
    entrada = input("> ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = int(entrada)  # Puedes usar float() si quieres permitir decimales
        lista1.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero o 'fin'.")

print("\nIngrese los números para la segunda lista (para terminar, ingrese 'fin'):")
while True:
    entrada = input("> ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = int(entrada)  # Puedes usar float() si quieres permitir decimales
        lista2.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero o 'fin'.")

# Combinar las dos listas
lista_combinada = lista1 + lista2

# Ordenar la lista combinada
lista_combinada.sort()

# Mostrar la lista combinada y ordenada
print("\nLista combinada y ordenada:")
print(lista_combinada)
