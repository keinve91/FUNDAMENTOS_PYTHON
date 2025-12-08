# Permiten ejecutar acciones diferentes dependiendo de si una condición es True o False.

# 1. Sentencia 'if' (Si...)
# Ejecuta el código indentado solo si la condición es Verdadera.
a = 6
b = 5

print(f"Comparando a={a} y b={b}...")
if a > b:
    # Es importante indentar (sangrar) el código dentro del if
    print('Resultado: a es mayor que b')

# Si la condición no se cumple, Python simplemente salta este bloque.
a_menor = 3
if a_menor > b:
    print('Este mensaje NO se imprimirá porque 3 no es mayor que 5')

# 2. Sentencia 'else' (Si no...)
# Define una acción alternativa cuando el 'if' no se cumple.
# Ejemplo: Clasificar clientes por ingresos.
customer_a = 20

print(f"\nClasificando cliente con valor {customer_a}:")
if customer_a > 15:
    print("Clasificación: high (alto)")
else:
    print("Clasificación: low (bajo)")

# 3. Sentencia 'elif' (Si no, si...)
# Permite agregar múltiples condiciones intermedias.
# Lógica: >15 es 'high', <10 es 'low', el resto es 'med'.

customer_list = [20, 5, 10] # Vamos a probar con varios valores manualmente
val = 10 # Probamos con el valor 10 (customer_c del ejemplo original)

print(f"\nClasificando cliente con valor {val} usando lógica compleja:")
if val > 15:
    print("high")
elif val < 10:
    print("low")
else:
    # Si no es mayor a 15 ni menor a 10, cae aquí (entre 10 y 15)
    print("med")