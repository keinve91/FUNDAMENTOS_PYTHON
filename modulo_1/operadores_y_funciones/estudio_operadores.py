# --- MÓDULO 1: OPERADORES ---
# Los operadores se usan para realizar operaciones sobre variables y valores.

# 1. Operadores Matemáticos
# Suma
print("3 + 2 =", 3 + 2)

# Resta
print("3 - 2 =", 3 - 2)

# Multiplicación
print("3 * 5 =", 3 * 5)

# División (siempre devuelve un flotante)
print("10 / 2 =", 10 / 2)

# Módulo (%): Devuelve el resto de la división
print("4 % 3 =", 4 % 3)  # El 3 cabe una vez en el 4, sobra 1

# Potencia (**): Eleva el número de la izquierda a la potencia de la derecha
print("2 ** 4 =", 2 ** 4) # 2 * 2 * 2 * 2 = 16

# Orden de operaciones (BEDMAS/PEMDAS)
# Python respeta paréntesis y exponentes antes que sumas y restas
resultado = 18 / (2 + 1) ** 2
print("18 / (2 + 1) ** 2 =", resultado)

# 2. Operadores de Comparación
# Devuelven un valor booleano: True (Verdadero) o False (Falso)

print("15 > 10 (Mayor que):", 15 > 10)
print("15 < 10 (Menor que):", 15 < 10)
print("15 >= 10 (Mayor o igual):", 15 >= 10)
print("15 <= 10 (Menor o igual):", 15 <= 10)

# Igualdad (==) y Desigualdad (!=)
print("20 == 20 (Es igual):", 20 == 20)
print("'John' == 'disagreeable':", 'John' == 'disagreeable')
print("21 != 21 (No es igual):", 21 != 21)

# 3. Operadores Lógicos (and, or)
# Permiten combinar condiciones

x = 2
# 'and': Ambas condiciones deben ser True
condicion_and = (x < 1) and (x < 3)
print("x=2, ¿es menor que 1 Y menor que 3?:", condicion_and)

# 'or': Al menos una condición debe ser True
condicion_or = (x < 1) or (x < 3)
print("x=2, ¿es menor que 1 O menor que 3?:", condicion_or)

# Combinación compleja
a, b, c = 10, 5, 20
compleja = (a + b > b + c) or (b + c < a + c)
print("Resultado de condición compleja:", compleja)