# FUNCIONES DE NORMALIZACIÓN DE TEXTO EN PYTHON

# 1. lower(): convierte todo el texto a minúsculas
titulo = "Cuarto Medio de Programación"
print(titulo.lower())  # Resultado: "cuarto medio de programación"

# 2. upper(): convierte todo el texto a mayúsculas
frase = "tercero medio de programación"
print(frase.upper())  # Resultado: "TERCERO MEDIO DE PROGRAMACIÓN"

# 3. capitalize(): solo la primera letra queda en mayúscula, el resto en minúscula
nombre = "vicente HUIDOBRO programador"
print(nombre.capitalize())  # Resultado: "Vicente huidobro programador"

# 4. title(): pone en mayúscula la primera letra de cada palabra
texto = "juan CARLOS boDOque"
print(texto.title())  # Resultado: "Juan Carlos Bodoque"

# 5. swapcase(): cambia las mayúsculas por minúsculas y viceversa
texto2 = "Cuarto Medio de Programación"
print(texto2.swapcase())  # Resultado: "cUARTO mEDIO DE pROGRAMACIÓN"

# BONUS: usar lower() con listas y comprensión de listas
frutas = ["PHYSALIS", "kumquat", "LoganBerry"]
frutas_normalizadas = [f.lower() for f in frutas]  # Convierte cada fruta a minúsculas
print(frutas_normalizadas)  # Resultado: ['physalis', 'kumquat', 'loganberry']