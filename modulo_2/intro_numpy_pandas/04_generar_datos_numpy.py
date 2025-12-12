import numpy as np

# --- 1. RANGOS DE NÚMEROS (ARANGE y LINSPACE) ---

# np.arange(fin): Crea enteros desde 0 hasta el fin (NO INCLUIDO).
# Salida: 0, 1, ..., 29
array_simple = np.arange(30)
print(array_simple)

# np.arange(inicio, fin): Desde inicio hasta fin (NO INCLUIDO).
# Salida: 3, 4, 5, 6
array_intervalo = np.arange(3, 7)
print (array_intervalo)
# np.arange(inicio, fin, paso): Salta de 2 en 2.
# Salida: 1, 3, 5, 7, 9
array_pasos = np.arange(1, 10, 2)
print(array_pasos)
# np.linspace(inicio, fin, cantidad):
# Genera 'cantidad' de números DECIMALES (floats) distribuidos equitativamente.
# Salida: 20 números exactos entre 0 y 5.
array_floats = np.linspace(0, 5, 20)
print(array_floats)


# --- 2. DATOS ALEATORIOS (RANDOM) ---

# np.random.rand(n): Genera 'n' decimales aleatorios entre 0 y 1.
random_floats = np.random.rand(10)
print (random_floats)
# np.random.randint(inicio, fin): Entero aleatorio entre inicio y fin (NO INCLUIDO).
# Ejemplo: Un número entre 10 y 19.
random_int = np.random.randint(10, 20)
print(random_int)
# Crear una matriz aleatoria:
# np.random.randint(inicio, fin, (filas, columnas))
matriz_random = np.random.randint(1, 101, (2, 4))
print(matriz_random)


# --- 3. SEMILLA (SEED) PARA REPRODUCIBILIDAD ---
# Si quieres que tus números "aleatorios" sean siempre los mismos (para que
# otra persona obtenga tus mismos resultados), usa seed.
np.random.seed(11)
print(np.random.rand(3)) 
# Si corres esto 100 veces, siempre dará los mismos 3 números.