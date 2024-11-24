print("")
print("Castruita soto emmanuel ")
print("")
def filtrar_palabras(palabras, n):
    # Filtra y devuelve las palabras que tienen más de 'n' caracteres
    return [palabra for palabra in palabras if len(palabra) > n]

# Función para pedir palabras al usuario
def obtener_palabras():
    lista_palabras = []
    while True:
        palabra = input("Ingresa una palabra (o 'fin' para terminar): ")
        if palabra.lower() == 'fin':
            break
        lista_palabras.append(palabra)
    
    return lista_palabras

# Función para pedir el número 'n'
def obtener_n():
    while True:
        try:
            n = int(input("Ingresa el valor de n (número entero): "))
            return n
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

# Llamada a las funciones
palabras = obtener_palabras()

if palabras:
    n = obtener_n()
    resultado = filtrar_palabras(palabras, n)
    print(f"Las palabras con más de {n} caracteres son: {resultado}")
else:
    print("No se ingresaron palabras.")
