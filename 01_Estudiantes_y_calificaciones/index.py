# Lista de estudiantes con nombres y notas
estudiantes = [
    {"nombre": "Martin", "nota": 50},
    {"nombre": "Carlos", "nota": 62},
    {"nombre": "Juan", "nota": 70},
    {"nombre": "Roberto", "nota": 38},
    {"nombre": "David", "nota": 40},
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Elena", "nota": 90}
]

# Variables para cálculos
suma_notas = 0
mejor_nota = 0
peor_nota = 100
mejor_estudiante = ""
peor_estudiante = ""
arriba_promedio = 0
abajo_promedio = 0

# Recorrer lista de estudiantes
for estudiante in estudiantes:
    nota = estudiante["nota"]
    suma_notas += nota
    
    if nota > mejor_nota:
        mejor_nota = nota
        mejor_estudiante = estudiante["nombre"]
    
    if nota < peor_nota:
        peor_nota = nota
        peor_estudiante = estudiante["nombre"]

# Calcular promedio
promedio = suma_notas / len(estudiantes)

# Contar estudiantes por encima y por debajo del promedio
for estudiante in estudiantes:
    if estudiante["nota"] > promedio:
        arriba_promedio += 1
    elif estudiante["nota"] < promedio:
        abajo_promedio += 1

# Imprimir resultados
print(f"Promedio de notas: {promedio:.2f}")
print(f"Mejor estudiante: {mejor_estudiante} con {mejor_nota}")
print(f"Peor estudiante: {peor_estudiante} con {peor_nota}")
print(f"Estudiantes por encima del promedio: {arriba_promedio}")
print(f"Estudiantes por debajo del promedio: {abajo_promedio}")

# Listar estudiantes según el promedio
print("\nEstudiantes por encima del promedio:")
for estudiante in estudiantes:
    if estudiante["nota"] > promedio:
        print(f"- {estudiante['nombre']} ({estudiante['nota']})")

print("\nEstudiantes por debajo del promedio:")
for estudiante in estudiantes:
    if estudiante["nota"] < promedio:
        print(f"- {estudiante['nombre']} ({estudiante['nota']})")
