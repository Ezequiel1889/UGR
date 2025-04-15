def cifrar_frase(frase):
    """
    Cifra una frase reemplazando cada letra por la siguiente en el alfabeto.

    Args:
        frase: La frase a cifrar (string).

    Returns:
        La frase cifrada (string).
    """
    frase_cifrada = ""
    for caracter in frase:
        if 'a' <= caracter <= 'z':
            # Cifrar letras minúsculas
            if caracter == 'z':
                frase_cifrada += 'a'
            else:
                frase_cifrada += chr(ord(caracter) + 1)
        elif 'A' <= caracter <= 'Z':
            # Cifrar letras mayúsculas
            if caracter == 'Z':
                frase_cifrada += 'A'
            else:
                frase_cifrada += chr(ord(caracter) + 1)
        else:
            # Mantener otros caracteres sin cambios (espacios, números, símbolos)
            frase_cifrada += caracter
    return frase_cifrada

# Solicitar la frase al usuario
frase_original = input("Ingrese una frase: ")

# Cifrar la frase
frase_cifrada = cifrar_frase(frase_original)

# Mostrar la frase cifrada
print("Frase cifrada:", frase_cifrada)