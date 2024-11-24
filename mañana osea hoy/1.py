print("")
print("Emmanuel Castruita Soto 3w 1176")
print("")
def max_in_list(numbers):
    # Retorna el número más grande de la lista
    return max(numbers)

# Función para pedir números al usuario
def obtener_numeros():
    lista_numeros = []
    while True:
        try:
            # Pedimos al usuario que ingrese un número
            num = input("Ingresa un número (o 'fin' para terminar): ")
            if num.lower() == 'fin':
                break
            else:
                lista_numeros.append(float(num))
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    return lista_numeros

# Llamada a las funciones
numeros = obtener_numeros()

if numeros:
    print(f"El número más grande es: {max_in_list(numeros)}")
else:
    print("No se ingresaron números.")
