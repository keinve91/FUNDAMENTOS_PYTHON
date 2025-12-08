# Un paquete (o librería) es una colección de funciones externas.

# 1. Importación básica
# Importamos todo el paquete 'math'. Para usarlo debemos poner 'math.' antes de la función.
import math
raiz_100 = math.sqrt(100)
print("Raíz cuadrada de 100 (usando math.sqrt):", raiz_100)

# 2. Importación con Alias (Renombrar)
# Importamos 'math' pero le llamamos 'mth' para escribir menos.
import math as mth
raiz_81 = mth.sqrt(81)
print("Raíz cuadrada de 81 (usando mth.sqrt):", raiz_81)

# 3. Importar una función específica
# Usamos 'from ... import ...'. Ya no hace falta escribir 'math.' antes de la función.
from math import sqrt
raiz_25 = sqrt(25)
print("Raíz cuadrada de 25 (importando solo sqrt):", raiz_25)

# 4. Importar TODO de un paquete
# El asterisco (*) importa todas las funciones. 
# NOTA: No se recomienda en scripts grandes para evitar conflictos de nombres.
from math import *
print("Raíz de 9:", sqrt(9))
print("Potencia de 3^2:", pow(3, 2))

# 5. Obtener Ayuda
# La función help() muestra la documentación de una función o librería.
print("\n--- Ayuda sobre la función sqrt ---")
help(math.sqrt)