print("")
print("Castruita soto emmanuel ")
print("")
def contar_nombres_con_letra(nombres, letra):
    # Cuenta cuántos nombres comienzan con la letra especificada
    return sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))

# Lista de nombres (puedes agregar más nombres si lo deseas)
nombres = ["Ana", "Pedro", "Alba", "Luis", "Andrés", "Carlos", "Antonio", "Martín", "Alfonso"]

# Solicitar la letra al usuario
letra_buscar = input("Ingresa la letra para buscar los nombres que comienzan con ella: ")

# Contar cuántos nombres comienzan con la letra proporcionada
cantidad_nombres = contar_nombres_con_letra(nombres, letra_buscar)

# Imprimir el resultado
print(f"Cantidad de nombres que comienzan con la letra '{letra_buscar.upper()}': {cantidad_nombres}")
