print("")
print("Castruita soto emmanuel ")
print("")
def contar_mayusculas(cadena):
    # Cuenta cuántas letras mayúsculas hay en la cadena
    return sum(1 for caracter in cadena if caracter.isupper())

# Solicitar la entrada del usuario
cadena_usuario = input("Ingresa una cadena: ")

# Llamar a la función para contar las mayúsculas
numero_mayusculas = contar_mayusculas(cadena_usuario)

# Mostrar el resultado
print(f"La cadena tiene {numero_mayusculas} letras mayúsculas.")
