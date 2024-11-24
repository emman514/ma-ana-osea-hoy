print("")
print("Castruita soto emmanuel ")
print("")
def contar_mayores_de_20(edades):
    # Cuenta cuántas edades son mayores a 20
    return sum(1 for edad in edades if edad > 20)

# Crear una lista para almacenar las edades ingresadas por el usuario
edades = []

# Solicitar las edades de 10 personas al usuario
for i in range(10):
    while True:
        try:
            edad = int(input(f"Ingresa la edad de la persona {i+1}: "))
            edades.append(edad)
            break
        except ValueError:
            print("Por favor, ingresa una edad válida (número entero).")

# Convertir la lista de edades a una tupla
tupla_edades = tuple(edades)

# Contar cuántas personas tienen edades superiores a 20
cantidad_mayores_de_20 = contar_mayores_de_20(tupla_edades)

# Imprimir el resultado
print(f"Cantidad de personas con edades superiores a 20: {cantidad_mayores_de_20}")
