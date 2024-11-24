print("")
print("Castruita soto emmanuel ")
print("")
def calcular_edad(año_nacimiento, año_actual):
    # Calcula la edad de una persona durante el año actual
    return año_actual - año_nacimiento

# Solicitar el año actual
año_actual = int(input("Ingresa el año en curso: "))

# Lista para almacenar los datos de las personas
personas = []

# Pedir el nombre y año de nacimiento de tres personas
for i in range(3):
    nombre = input(f"Ingresa el nombre de la persona {i+1}: ")
    año_nacimiento = int(input(f"Ingresa el año de nacimiento de {nombre}: "))
    edad = calcular_edad(año_nacimiento, año_actual)
    personas.append((nombre, edad))

# Imprimir los resultados
print("\nAños que cumplirán las personas durante el año en curso:")
for persona in personas:
    print(f"{persona[0]} cumplirá {persona[1]} años.")
