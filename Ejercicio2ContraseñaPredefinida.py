# Contraseña predefinida
contrasena_correcta = "EzequielUGR2025"
intentos_maximos = 3
intentos_realizados = 0

print("Bienvenido al sistema de acceso.")

while intentos_realizados < intentos_maximos:
    contrasena_ingresada = input(f"Intento {intentos_realizados + 1}: Ingrese la contraseña: ")

    if contrasena_ingresada == contrasena_correcta:
        print("Acceso concedido.")
        break  # Sale del bucle while porque la contraseña es correcta
    else:
        intentos_realizados += 1
        print("Contraseña incorrecta.")

if intentos_realizados == intentos_maximos:
    print("Acceso bloqueado. Ha excedido el número máximo de intentos.")