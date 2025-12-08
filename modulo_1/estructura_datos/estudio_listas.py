# Una lista es una secuencia mutable de datos.

# 1. Creación de listas
# Lista de textos (Strings)
list_a = ['Yuting', 'John', 'Karina', 'Rahul']
print("Lista inicial (list_a):", list_a)

# Lista numérica
list_b = [12, 11, 13]
print("Lista numérica (list_b):", list_b)

# Lista con tipos de datos mixtos (enteros, letras, booleanos, decimales)
list_c = [1, 'a', True, 2.56]
print("Lista mixta (list_c):", list_c)

# 2. Acceso a elementos (Indexación)
# Los índices empiezan en 0. 'Karina' es el índice 2.
print("Elemento en índice 2:", list_a[2])

# Índices negativos: -1 es el último, -3 es el tercero desde el final.
print("Tercer elemento desde el final (-3):", list_a[-3])

# 3. Listas Anidadas (Listas dentro de listas)
# Aquí list_d contiene a list_a como un elemento
list_d = [list_a, 'Pavel']
print("Lista anidada (list_d):", list_d)

# 4. Concatenación (Unir listas)
# Sumar listas crea una nueva lista combinada
list_f = list_a + list_b
print("Listas unidas (list_f):", list_f)

# 5. Ordenamiento (Sort)
# Ordenar alfabéticamente
list_a.sort()
print("Lista ordenada alfabéticamente:", list_a)

# Ordenar numéricamente en orden inverso (descendente)
list_b.sort(reverse=True)
print("Lista numérica ordenada descendente:", list_b)

# NOTA: No se puede ordenar 'list_c' porque mezcla números y letras.

# 6. Mutabilidad (Modificar la lista)
# Agregar un elemento al final
list_a.append('Rosie')
print("Después de append('Rosie'):", list_a)

# Reemplazar un valor específico (cambiamos el índice 1)
list_a[1] = 'Oscar'
print("Después de reemplazar índice 1 con 'Oscar':", list_a)

# Eliminar un elemento (borramos el índice 3)
del list_a[3]
print("Después de eliminar índice 3:", list_a)