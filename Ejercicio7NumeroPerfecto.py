def es_perfecto(numero):
    """
    Determina si un número entero positivo es un número perfecto.

    Un número perfecto es aquel que es igual a la suma de sus divisores propios
    (excluyéndose a sí mismo).

    Args:
        numero: El número entero positivo a verificar.

    Returns:
        True si el número es perfecto, False en caso contrario.
    """
    if numero <= 1:
        return False  # 1 no es un número perfecto

    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    return suma_divisores == numero

def contar_perfectos(lista_numeros):
    """
    Cuenta cuántos números perfectos hay en una lista de enteros positivos.

    Args:
        lista_numeros: Una lista de números enteros positivos.

    Returns:
        La cantidad de números perfectos encontrados en la lista.
    """
    contador = 0
    for numero in lista_numeros:
        if numero > 0 and es_perfecto(numero):
            contador += 1
    return contador

# Ejemplo de uso
try:
    entrada = input("Ingrese una lista de números enteros positivos separados por espacios: ")
    numeros_str = entrada.split()
    lista_numeros = [int(num) for num in numeros_str]

    cantidad_perfectos = contar_perfectos(lista_numeros)
    print(f"En la lista ingresada, hay {cantidad_perfectos} número(s) perfecto(s).")

except ValueError:
    print("Error: Por favor, ingrese números enteros positivos válidos separados por espacios.")