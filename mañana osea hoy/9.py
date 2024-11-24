print("")
print("Castruita soto emmanuel ")
print("")
def contar_vocales(palabra):
    # Diccionario para contar las vocales
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Recorrer cada caracter de la palabra
    for letra in palabra.lower():  # Usamos .lower() para hacer la búsqueda insensible a mayúsculas
        if letra in vocales:
            vocales[letra] += 1  # Incrementar el contador de la vocal encontrada
    
    return vocales

# Solicitar la palabra al usuario
palabra_usuario = input("Ingresa una palabra: ")

# Llamar a la función para contar las vocales
resultado = contar_vocales(palabra_usuario)

# Imprimir el resultado
print("Conteo de vocales en la palabra:")
for vocal, cantidad in resultado.items():
    print(f"{vocal.upper()}: {cantidad}")
