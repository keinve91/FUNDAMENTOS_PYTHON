import pandas as pd

# Cargamos de nuevo para este ejemplo
dataframe_3 = pd.read_csv('Data Source.csv')

# --- 1. MANEJO DE DUPLICADOS ---

# Ver valores únicos en una columna específica (ej. 'Store'):
tiendas_unicas = pd.unique(dataframe_3['Store'])

# Contar cuántos valores únicos hay en CADA columna:
conteo_unicos = dataframe_3.nunique()

# Eliminar filas duplicadas:
# drop_duplicates() busca filas donde TODOS los valores sean idénticos.
df_sin_duplicados = dataframe_3.drop_duplicates()

# Eliminar duplicados basándose solo en una columna (ej. 'Store'):
# Esto dejará solo la primera aparición de cada tienda y borrará las demás.
df_tiendas_unicas = dataframe_3.drop_duplicates(subset=['Store'])


# --- 2. CORRECCIÓN DE DATOS (TEXTO) ---
# Supongamos que la columna 'ProductID' tiene valores como "11XXRP-P".
# Queremos separar el ID ("11XXRP") del código especial ("P").

# Usamos .str.split()
# - '-': Es el separador.
# - expand=True: Convierte el resultado en columnas separadas de DataFrame, no en una lista.
division = dataframe_3['ProductID'].str.split('-', expand=True)

# Asignamos esas nuevas columnas al DataFrame original
# Columna 0 va a 'ProductID' (sobrescribe), Columna 1 va a una nueva 'SpecialID'
dataframe_3[['ProductID', 'SpecialID']] = division

print("\n--- DataFrame con columnas separadas ---")
print(dataframe_3.head())


# --- 3. EXPORTAR DATOS LIMPIOS ---
# Una vez limpio, guardamos el resultado para no tener que limpiarlo cada vez.
# index=False evita que se guarde la columna de números de fila (0, 1, 2...) en el CSV.
dataframe_3.to_csv('export_limpio.csv', index=False)
print("\n¡Archivo exportado con éxito!")