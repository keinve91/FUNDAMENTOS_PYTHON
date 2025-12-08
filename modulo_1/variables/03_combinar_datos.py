number = 10

# --- EL ERROR ---
# Si intentamos esto, Python dará un TypeError:
# print(number + " es mi número favorito")

# --- LA SOLUCIÓN ---
# Usamos str() para "disfrazar" el número de texto temporalmente.
# Ahora ambos son strings y se pueden unir (+).
mensaje = str(number) + " es mi número favorito"

print(mensaje) 
# Salida: 10 es mi número favorito