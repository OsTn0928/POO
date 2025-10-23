# Tarea libro de clases
# Arreglar codigo para que al ingresar algo que no sea un número float o un numero normal tire error y coloque ingrese not

def main():
    # Imprimir mensaje de bienvenida
    print("=====================")
    print("LIBRO DE CLASES VATE.")
    print("=====================")

    # Función para estandarizar texto
    def estandarizar_texto(texto):
        return texto.title()  # Convertir la primera letra de cada palabra a mayúscula y el resto a minúscula

    estudiantes = []  # Lista para almacenar los datos de los estudiantes

    while True:  # Bucle para ingresar estudiantes
        nombre_apellidos = input("Ingrese el nombre y apellidos del estudiante: ")
        nombre_apellidos = estandarizar_texto(nombre_apellidos)  # Estandarizar el nombre y apellidos

        asignaturas = {}  # Diccionario para almacenar las asignaturas y sus notas

        while True:  # Bucle para ingresar asignaturas
            asignatura = input("Ingrese el nombre de la asignatura: ")
            asignatura = estandarizar_texto(asignatura)  # Estandarizar el nombre de la asignatura

            notas = []  # Lista para almacenar las notas de la asignatura
            while True:  # Bucle para ingresar notas
                try:
                    nota = float(input(f"Ingrese una nota para {asignatura} (o -1 para terminar): "))
                    if nota == -1:
                        break  # Salir del bucle si se ingresa -1
                    notas.append(nota)  # Agregar la nota a la lista
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                
                

            asignaturas[asignatura] = notas  # Almacenar las notas en el diccionario de asignaturas

            otra_asignatura = input("¿Desea ingresar otra asignatura? (s/n): ").lower()
            if otra_asignatura != 's':
                break  # Salir del bucle si no se desea ingresar otra asignatura

        estudiantes.append({'nombre': nombre_apellidos, 'asignaturas': asignaturas})  # Almacenar los datos del estudiante

        otro_estudiante = input("¿Desea ingresar otro estudiante? (s/n): ").lower()
        if otro_estudiante != 's':
            break  # Salir del bucle si no se desea ingresar otro estudiante

    # Calcular y mostrar promedios
    for estudiante in estudiantes:
        print(f"\nEstudiante: {estudiante['nombre']}")
        total_general = 0  # Variable para el total general de notas
        total_asignaturas = 0  # Contador de asignaturas
        for asignatura, notas in estudiante['asignaturas'].items():
            if notas:  # Verificar que haya notas ingresadas
                promedio_asignatura = sum(notas) / len(notas)  # Calcular el promedio de la asignatura
                print(f"Promedio de {asignatura}: {promedio_asignatura:.2f}")
                total_general += promedio_asignatura  # Sumar al total general
                total_asignaturas += 1  # Incrementar el contador de asignaturas
        if total_asignaturas > 0:
            promedio_general = total_general / total_asignaturas  # Calcular el promedio general
            print(f"Promedio general del estudiante: {promedio_general:.2f}")
    # Imprimir información final del programa
    print("\nPrograma desarrollado por: Vicente Rojas Huenchumil  Curso: 4°C, Fecha: 22/10/2025 hoy miercole.")
    
    main()  # Llamar a la función principal