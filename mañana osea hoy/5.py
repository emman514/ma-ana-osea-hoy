print("")
print("Castruita soto emmanuel ")
print("")
def convertir_binario_a_entero(binario):
    try:
        # Convertir el número binario (cadena) a entero
        entero = int(binario, 2)
        return entero
    except ValueError:
        # Si no se ingresa un número binario válido
        return "Error: No es un número binario válido."

# Solicitar la entrada del usuario
numero_binario = input("Ingresa un número binario: ")

# Llamar a la función para convertir el binario a entero
resultado = convertir_binario_a_entero(numero_binario)

# Mostrar el resultado
print(f"El número binario {numero_binario} es {resultado} en decimal.")
