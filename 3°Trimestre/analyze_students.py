#HOLA PROFE MAURICIO MEDEL SANCHEZ CORTES SALINAS VESPUCIO NORTE NOVENO SEGUNDO
#Y ESTE ES MI PROGRAMA DE ANALISIS DE NOMBRES DE ESTUDIANTES
#OJALA ME PONGA 7 O SI NO, VOY A HACER SHOW EN SU CLASE Y RECLAMO
#PQ APARTE NO SALE QUE ES CON NOTA
#LA COSA FUNCIONA PERFECTAMENTE Y LE PONGO TODO LO QUE PIDIO
#ESPERO QUE LE GUSTE
#lo quiero 

def procesar_nombres(*args, **kwargs): # aqui definimos la funcion
    print("\n=== Resultados del análisis de nombres ===\n") # encabezado

    for nombre in args: # recorremos cada nombre
        print(f"Nombre original: '{nombre}'") # mostramos el nombre original
        print("Minusculas:", nombre.lower()) # mostramos el nombre en minusculas
        print("Mayusculas:", nombre.upper()) # mostramos el nombre en mayusculas
        print("Primera letra mayúscula:", nombre.capitalize()) # mostramos el nombre con la primera letra en mayuscula
        print("Primera letra de cada palabra mayúscula:", nombre.title()) # mostramos el nombre con la primera letra de cada palabra en mayuscula
        print("Invertir mayúsculas y minúsculas:", nombre.swapcase()) # mostramos el nombre con mayusculas y minusculas invertidas
        print("Quitar espacios al inicio y al final:", nombre.strip()) # mostramos el nombre sin espacios al inicio y al final
        print("Quitar espacios a la izquierda:", nombre.lstrip()) # mostramos el nombre sin espacios a la izquierda
        print("Quitar espacios a la derecha:", nombre.rstrip()) # mostramos el nombre sin espacios a la derecha
        print("-" * 40) # linea separadora1

    print("\n=== Datos adicionales ===") # encabezado2
    for clave, valor in kwargs.items(): # recorremos los datos adicionales
        print(f"{clave}: {valor}") # mostramos cada dato adicional

    print("\n=== Autor del programa ===") # encabezado3
    print("Vicente Austin T.H")   # autor del programa osea yo profe y dejeme el 7 o si no reclamo


#El progarama principale
nombres = []  # aqui profe, una lista vacia para guardar los nombres

cantidad = int(input("¿Cuántos nombres de estudiantes desea ingresar? ")) # y AQUI!!! pedimos la cantidad de nombres

for i in range(cantidad):   # y recorremos la cantidad de nombres
    nombre = input(f"Ingrese el nombre y apellido del estudiante {i+1}: ")  # pedimos cada nombre
    nombres.append(nombre) # y lo agregamos a la listaa

curso = input("Ingrese el curso: ") # pedimos el curso
año = input("Ingrese el año: ") # pedimos el año

# usamos args para nombres curso y año como kwargs
procesar_nombres(*nombres, curso=curso, año=año)
