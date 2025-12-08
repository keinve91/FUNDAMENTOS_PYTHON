# Un diccionario es una colección de pares Clave-Valor desordenados.

# 1. Creación de un Diccionario
# Se usan llaves {}. Formato -> 'clave': valor
dict_a = {
    'first_name': 'Frank', 
    'last_name': 'Park', 
    'age': 20
}
print("Diccionario inicial (dict_a):", dict_a)

# 2. Acceder a valores
# Se usa la clave (key) en lugar de un número de índice
nombre = dict_a['first_name']
print("Valor de la clave 'first_name':", nombre)

# 3. Regla de Unicidad (No duplicados en claves)
# Si repites una clave, Python se queda con el ÚLTIMO valor asignado.
dict_c = {
    'first_name': 'Frank', 
    'first_name': 'Frank1',  # Esta sobrescribe a la anterior
    'last_name': 'Park', 
    'age': 20
}
print("Diccionario con clave duplicada (se queda con el último valor):", dict_c)

# 4. Crear diccionarios usando Listas
# Es común tener listas de datos y unirlas en un diccionario
sales_list = [100, 200, 240, 400, 100, 500]
stores_list = ['Store A', 'Store B', 'Store A', 'Store C', 'Store D', 'Store B']

dict_sales = {'Sales': sales_list, 'Stores': stores_list}
print("Diccionario creado desde listas (dict_sales):", dict_sales)

# 5. Inspeccionar ítems
# El método .items() devuelve los pares clave-valor (útil para bucles)
print("Ítems del diccionario:", dict_sales.items())