import pandas as pd


# --- CREACIÓN DE SERIES ---
lista_1 = [12,24,36]
marcador =['a','b','c']

# Opción 1: Crear serie automática (índices 0, 1, 2)
serie_basica=pd.Series(data=lista_1)
print(serie_basica)

#Opción 2: Crear serie con índices personalizados
# Ahora 'a' apunta a 12, 'b' a 24, etc.
serie_personaliza=pd.Series(data=lista_1,index=marcador)
print(serie_personaliza)
# Opción 3: Desde un diccionario (las claves se convierten en índices automáticamente)
diccionario={'d':1, 'e':2,'f':3}
serie_dicc=pd.Series(diccionario)
print(serie_dicc)
# --- OPERACIONES CON SERIES (SUMA Y ALINEACIÓN) ---
# Pandas alinea los datos por su ÍNDICE, no por su posición.
# --- OPERACIONES CON SERIES (SUMA Y ALINEACIÓN) ---
# Pandas alinea los datos por su ÍNDICE, no por su posición.

# Datos de ventas Trimestre 1
Gift_shop_salesQ1 = pd.Series([300, 550, 240, 180], 
                              index=['Magnets', 'Coasters', 'Handbags', 'Snacks'])

# Datos de ventas Trimestre 2
Gift_shop_salesQ2 = pd.Series([340, 600, 225, 75], 
                              index=['Magnets', 'Coasters', 'Handbags', 'Snacks'])

# Datos de ventas Trimestre 3 (Nuevos productos: 'Postcards')
Gift_shop_salesQ3 = pd.Series([480, 520, 360, 40], 
                              index=['Magnets', 'Coasters', 'Handbags', 'Postcards'])

# Suma Total:
# Si un índice (ej. 'Snacks' o 'Postcards') no existe en alguna de las series,
# el resultado será NaN (Not a Number) para ese producto.
total_ventas = Gift_shop_salesQ1 + Gift_shop_salesQ2 + Gift_shop_salesQ3
print(total_ventas)