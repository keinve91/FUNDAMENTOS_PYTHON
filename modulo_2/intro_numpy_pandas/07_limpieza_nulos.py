import pandas as pd
import numpy as np

# Cargar el DataFrame (Asegúrate de tener el archivo 'Data Source.csv' en la carpeta correcta)
# Usamos r'' para rutas absolutas si es necesario, como vimos antes.
dataframe_3 = pd.read_csv('Data Source.csv')

# --- 1. INSPECCIÓN INICIAL ---
# .info() es el primer paso vital. Nos dice:
# - Cuántas filas y columnas hay.
# - Qué tipo de dato tiene cada columna (int, float, object/texto).
# - Cuántos valores NO son nulos.
print("--- Información Inicial ---")
dataframe_3.info()

# --- 2. CORRECCIÓN DE FECHAS ---
# Pandas a menudo carga las fechas como 'object' (texto). Esto es malo para el análisis.
# Convertimos la columna 'Date' a formato datetime real.
dataframe_3['Date'] = pd.to_datetime(dataframe_3['Date'])
# Ahora .info() mostrará 'datetime64[ns]' en lugar de 'object'.


# --- 3. DETECCIÓN DE DATOS FALTANTES (NaN) ---
# isna() nos dice True/False si falta un dato. .sum() los cuenta por columna.
conteo_nulos = dataframe_3.isna().sum()
print("\n--- Conteo de Nulos por Columna ---")
print(conteo_nulos)


# --- 4. ESTRATEGIA A: ELIMINAR (DROP) ---
# A veces preferimos borrar lo que está incompleto.

# Eliminar FILAS que tengan al menos un valor nulo:
df_sin_filas_nulas = dataframe_3.dropna()

# Eliminar COLUMNAS que tengan al menos un valor nulo (axis=1):
df_sin_cols_nulas = dataframe_3.dropna(axis=1)


# --- 5. ESTRATEGIA B: RELLENAR (FILL) ---
# Borrar datos puede ser peligroso (pierdes información). A veces es mejor rellenar.

# Opción 1: Rellenar con un valor fijo (ej. 0)
# Útil si un nulo significa "cantidad cero".
df_relleno_cero = dataframe_3.fillna(0)

# Opción 2: Rellenar con el valor ANTERIOR (Forward Fill - ffill)
# Copia el dato de la fila de arriba. Útil en series de tiempo.
df_relleno_ffill = dataframe_3.fillna(method="ffill")

# Opción 3: Rellenar con el valor SIGUIENTE (Back Fill - bfill)
# Copia el dato de la fila de abajo.
df_relleno_bfill = dataframe_3.fillna(method="bfill")

print("\nEjemplo de relleno con 0:")
print(df_relleno_cero.head())