# Una tupla es una colección ordenada e INMUTABLE (no se puede cambiar).

# 1. Creación de Tuplas
# Tupla de strings
tuple_a = ('a', 'b', 'c')
print("Tupla de strings (tuple_a):", tuple_a)

# Tupla numérica
tuple_b = (1, 2, 3)
print("Tupla numérica (tuple_b):", tuple_b)

# Tupla mixta
tuple_c = (1, 'a', True, 2.56)
print("Tupla mixta (tuple_c):", tuple_c)

# 2. Tuplas Anidadas
# Una tupla que contiene otras tuplas y listas dentro
# Supongamos que list_a viene del módulo anterior (la definimos aquí para el ejemplo)
list_a = ['Yuting', 'Oscar', 'Karina', 'Rosie'] 
tuple_d = (tuple_b, list_a, tuple_c)
print("Tupla de tuplas (tuple_d):", tuple_d)

# 3. Concatenación
# Se pueden sumar tuplas para crear una nueva, aunque las originales no cambien
tuple_e = tuple_a + tuple_b
print("Tuplas concatenadas (tuple_e):", tuple_e)

# 4. Demostración de Inmutabilidad
# Las siguientes líneas darían ERROR si se ejecutan, porque las tuplas son fijas.
# Están comentadas para que el código corra sin detenerse.

# INTENTO DE APPEND (Error: 'tuple' object has no attribute 'append')
# tuple_a.append('a') 

# INTENTO DE REEMPLAZO (Error: 'tuple' object does not support item assignment)
# tuple_a[1] = 'e'

# INTENTO DE BORRADO (Error: 'tuple' object doesn't support item deletion)
# del tuple_a[3]

print("Nota: Las operaciones de modificación (append, asignación, del) darán error en tuplas.")