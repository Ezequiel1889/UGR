def es_contrasena_segura(contrasena):
    """
    Verifica si una contraseña cumple con los requisitos de seguridad.

    Args:
        contrasena: La contraseña ingresada por el usuario (string).

    Returns:
        True si la contraseña es segura, False en caso contrario.
    """
    tiene_longitud_minima = len(contrasena) >= 8
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)

    if tiene_longitud_minima and tiene_mayuscula and tiene_numero:
        return True
    else:
        return False

# Solicitar la contraseña al usuario
contrasena_ingresada = input("Ingrese una contraseña: ")

# Verificar si la contraseña es segura
if es_contrasena_segura(contrasena_ingresada):
    print("La contraseña es segura.")
else:
    print("La contraseña no cumple con los requisitos de seguridad.")
    if not len(contrasena_ingresada) >= 8:
        print("- Debe tener al menos 8 caracteres.")
    if not any(c.isupper() for c in contrasena_ingresada):
        print("- Debe incluir al menos una letra mayúscula.")
    if not any(c.isdigit() for c in contrasena_ingresada):
        print("- Debe incluir al menos un número.")