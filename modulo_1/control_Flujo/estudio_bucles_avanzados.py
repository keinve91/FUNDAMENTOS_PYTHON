
# Definimos un diccionario de productos electrónicos
electronics_dict = {
  "brand": ["Apple", "Microsoft", "Lenova"],
  "product": ["phone", "laptop", 'tablet'],
  "year": [2022, 2020, 2010]
}

# 1. Iterar solo las Claves (Keys)
# Por defecto, un bucle sobre un diccionario devuelve las claves.
print("--- Claves del diccionario ---")
for i_key in electronics_dict:
    print(i_key)

# 2. Acceder a los Valores usando las Claves
print("\n--- Valores del diccionario (accedidos por clave) ---")
for i_key in electronics_dict:
    # Usamos la clave actual para obtener el valor: dict[clave]
    valores = electronics_dict[i_key]
    print(valores)

# 3. Iterar Clave y Valor simultáneamente (.items())
# La función .items() devuelve pares, permitiendo usar dos variables en el bucle.
print("\n--- Pares Clave-Valor usando .items() ---")
for i_key, j_value in electronics_dict.items():
    print(f"La clave es '{i_key}' y sus valores son: {j_value}")

# 4. Bucles Anidados (Nested Loops)
# Un bucle dentro de otro. Útil para recorrer listas que están dentro de un diccionario.
print("\n--- Bucle Anidado (Desglosando todo) ---")
for i_key in electronics_dict:                 # Bucle Externo: Recorre las claves ('brand', 'product', etc.)
    print(f"--> Entrando a la categoría: {i_key}")
    
    # Bucle Interno: Recorre la LISTA que hay dentro de cada clave
    for j_value in electronics_dict[i_key]:    
        print(f"    Elemento individual: {j_value}")