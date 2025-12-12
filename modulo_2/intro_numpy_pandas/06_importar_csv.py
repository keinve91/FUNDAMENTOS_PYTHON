import pandas as pd
# --- CARGAR CSV ---
# Usamos pd.read_csv().
# Si el archivo está en la misma carpeta, solo pones el nombre:
dataframe_3 = pd.read_csv('Data Source.csv')

# Si estuviera en una subcarpeta llamada 'data', sería:
# pd.read_csv('data/Data Source.csv')

print(dataframe_3)