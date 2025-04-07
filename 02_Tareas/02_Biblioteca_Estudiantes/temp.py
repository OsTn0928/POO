# Variables de la biblioteca
nombre_biblioteca = "Biblioteca Escolar Vate"
capacidad_maxima = 1500
libros_disponibles = 1223

# Información del libro destacado
libro_destacado = {
    "Titulo": "La Conspiración",
    "Autor": "Dan Brown",
    "año": 2001,
    "género": "Novela",
    "disponible": True,
}

# Lista de categorías de libros
categorias = ["Ficción", "Historia", "Ciencia Ficción", "Biografía", "Fantasía"]

# Tupla con horarios (hora de apertura, hora de cierre)
horarios = (9, 17)

# Lista de estudiantes con préstamo
estudiantes_con_prestamo = [123456789, 234567890, 345678901]  # Se parte con algunos RUT de ejemplo

# 1. Imprimir el nombre de la biblioteca
print("Nombre de la biblioteca:", nombre_biblioteca)

# 2. Calcular y mostrar cuántos libros faltan para alcanzar la capacidad máxima
faltan = capacidad_maxima - libros_disponibles
print("Libros que faltan para llegar a la capacidad máxima:", faltan)

# 3. Agregar una nueva categoría "Programación"
categorias.append("Programación")
print("Categorías actualizadas:", categorias)

# 4. Mostrar la hora de apertura y cierre
print("Horario de atención:")
print("Abre a las", horarios[0], "hrs")
print("Cierra a las", horarios[1], "hrs")

# 5. Agregar un nuevo estudiante con RUT 12280919
estudiantes_con_prestamo.append(12280919)
print("Estudiantes con préstamo actualizados:", estudiantes_con_prestamo)

# 6. Cambiar el estado de disponibilidad del libro destacado a False
libro_destacado["disponible"] = False

# 7. Mostrar toda la información actualizada del libro destacado
print("Libro destacado actualizado:")
for clave, valor in libro_destacado.items():
    print(f"{clave}: {valor}")
 
