print("")
print("Emmanuel Castruita Soto 3w 1176")
print("")
def mas_larga(palabras):
    # Retorna la palabra más larga de la lista
    return max(palabras, key=len)

# Función para pedir palabras al usuario
def obtener_palabras():
    lista_palabras = []
    while True:
        palabra = input("Ingresa una palabra (o 'fin' para terminar): ")
        if palabra.lower() == 'fin':
            break
        lista_palabras.append(palabra)
    
    return lista_palabras

# Llamada a las funciones
palabras = obtener_palabras()

if palabras:
    print(f"La palabra más larga es: '{mas_larga(palabras)}'")
else:
    print("No se ingresaron palabras.")
