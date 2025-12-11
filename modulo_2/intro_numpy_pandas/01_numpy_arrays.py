import numpy as np

# --- CREACIÓN BÁSICA DE ARRAYS ---
# Crear un array simple (similar a una lista pero optimizado)
# Salida esperada: array([0, 1, 2])
array_simple = np.array([0, 1, 2])
print("Array:", array_simple)
print("Tipo:", type(array_simple))
print("-" * 20)


# --- CREACIÓN DE MATRICES (2 DIMENSIONES) ---
# Se usan listas anidadas para crear filas y columnas
# Array_1 es una matriz de 2 filas y 3 columnas
Array_1 = np.array([[1, 2, 3], 
                    [4, 5, 6]])
print("Matriz:\n", Array_1)
print("Dimensiones (filas, cols):", Array_1.shape)
print("-" * 20)


# --- TIPOS DE DATOS ---
# Nota importante: NumPy homogeneíza los datos. 
# Si hay un string ('hello world'), TODOS los números se convierten a strings.
Array_2 = np.array([[1, 2, 3, 4], 
                    ["hello world", 5, 6, 7]])
print("Matriz mezclada:\n", Array_2)
print("Tipo de dato interno:", Array_2.dtype)

# --- INSPECCIÓN DE DATOS ---
# .shape nos dice las dimensiones (filas, columnas)
# Para Array_1, el resultado es (2, 3) -> 2 filas, 3 columnas
forma = Array_1.shape
print(forma)
# --- INDEXACIÓN (ACCEDER A DATOS) ---
# Sintaxis: variable[fila, columna]
# Acceder a la fila 1 (segunda fila), columna 0 (primera columna)
valor_seleccionado = Array_1[1, 0] # Devuelve: 4
print(valor_seleccionado)
# --- FUNCIONES MATEMÁTICAS RÁPIDAS ---
# Encontrar el valor mínimo y máximo de todo el array
minimo = Array_1.min() # 1
maximo = Array_1.max() # 6