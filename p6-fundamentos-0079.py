#Iram Jimenez NC = 0079
print("==========================================")
print(" 1. VARIABLES EN PYTHON ")
print("==========================================")

# Ejemplo 1: Creación de variables
edad = 28
nombre_usuario = "Mariana"
print("Ejemplo 1 (Creación):", edad, nombre_usuario)

print("------------------------------------------")

# Ejemplo 2: Cambio de tipo mediante casting
a = str(100)    # 'a' se convierte a texto "100"
b = int(45.8)   # 'b' se convierte a entero 45
c = float(12)   # 'c' se convierte a decimal 12.0
print("Ejemplo 2 (Casting):", a, b, c)

print("------------------------------------------")

# Ejemplo 3: Obtener el tipo de dato
temperatura = 36.6
activo = True
print("Ejemplo 3 (Tipos):", type(temperatura), type(activo))


print("==========================================")
print(" 2. VARIABLES MÚLTIPLES ")
print("==========================================")

# Ejemplo 1: Asignar valores a múltiples variables
pais1, pais2, pais3 = "México", "Colombia", "España"
print("Ejemplo 1 (Múltiples países):", pais1, pais2, pais3)

print("------------------------------------------")

# Ejemplo 2: Un mismo valor asignado a varias variables
estado1 = estado2 = estado3 = "Pendiente"
print("Ejemplo 2 (Un solo valor):", estado1, estado2, estado3)

print("------------------------------------------")

# Ejemplo 3: Desempaquetar una lista de países
paises_latam = ["Argentina", "Chile", "Perú"]
p1, p2, p3 = paises_latam
print("Ejemplo 3 (Desempaquetar lista):", p1, p2, p3)


print("==========================================")
print(" 3. TIPOS DE DATOS ")
print("==========================================")

# Ejemplo 1: Texto (str), entero (int) y flotante (float)
producto = "Computadora Laptop"
precio = 12500
descuento = 0.15
print("Ejemplo 1 (Texto y Números):", producto, precio, descuento)

print("------------------------------------------")

# Ejemplo 2: Tipos de secuencia (list, tuple, range)
ciudades = ["Madrid", "Bogotá", "Lima"]
coordenadas_gps = (19.4326, -99.1332)
secuencia_pasos = range(1, 5)
print("Ejemplo 2 (Secuencias):", ciudades, coordenadas_gps, list(secuencia_pasos))

print("------------------------------------------")

# Ejemplo 3: Tipo mapeo (dict) y booleano (bool)
capitales = {"México": "CDMX", "Francia": "París"}
es_socio = False
print("Ejemplo 3 (Diccionario y Booleano):", capitales, es_socio)


print("==========================================")
print(" 4. OPERADORES ARITMÉTICOS ")
print("==========================================")

# Ejemplo 1: Suma, Resta y Multiplicación
total_suma = 250 + 75
diferencia = 500 - 120
producto_mult = 12 * 8
print("Ejemplo 1 (Básicos):", total_suma, diferencia, producto_mult)

print("------------------------------------------")

# Ejemplo 2: División exacta y división entera
div_real = 25 / 4
div_entera = 25 // 4
print("Ejemplo 2 (Divisiones):", div_real, div_entera)

print("------------------------------------------")

# Ejemplo 3: Módulo (residuo) y Potencia
residuo = 17 % 5
potencia_cubo = 4 ** 3
print("Ejemplo 3 (Módulo y Potencia):", residuo, potencia_cubo)


print("==========================================")
print(" 5. OPERADORES DE COMPARACIÓN ")
print("==========================================")

# Ejemplo 1: Igualdad (==) y Desigualdad (!=)
iguales = (100 == 100)
diferentes = ("México" != "Canadá")
print("Ejemplo 1 (Igualdad):", iguales, diferentes)

print("------------------------------------------")

# Ejemplo 2: Mayor que (>) y Menor que (<)
es_mayor = (85 > 90)
es_menor = (12 < 30)
print("Ejemplo 2 (Mayor/Menor):", es_mayor, es_menor)

print("------------------------------------------")

# Ejemplo 3: Mayor o igual (>=) y Menor o igual (<=)
puntuacion_minima = (70 >= 70)
limite_alcanzado = (15 <= 10)
print("Ejemplo 3 (Límites):", puntuacion_minima, limite_alcanzado)


print("==========================================")
print(" 6. OPERADORES LÓGICOS ")
print("==========================================")

# Ejemplo 1: Operador AND (ambas condiciones verdaderas)
nota = 88
aprobo = (nota >= 70 and nota <= 100)
print("Ejemplo 1 (AND):", aprobo)

print("------------------------------------------")

# Ejemplo 2: Operador OR (al menos una condición verdadera)
nivel = "intermedio"
tiene_acceso = (nivel == "administrador" or nivel == "intermedio")
print("Ejemplo 2 (OR):", tiene_acceso)

print("------------------------------------------")

# Ejemplo 3: Operador NOT (invierte el valor lógico)
suscripto = False
mostrar_publicidad = not suscripto
print("Ejemplo 3 (NOT):", mostrar_publicidad)

print("Iram Jimenez NC = 0079")