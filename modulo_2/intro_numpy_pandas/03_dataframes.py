import pandas as pd
import numpy as np
# --- CREACIÓN DESDE UN ARRAY NUMPY ---
# 1. Definimos los datos crudos
Frames = np.array([[1,2,3], [4,5,6], [4,5,6], [4,5,6], [4,5,6]])
# 2. Definimos etiquetas
Rows = ['A', 'B', 'C', 'D', 'E']     # Índices
Columns = ['X', 'Y', 'Z']            # Cabeceras de columna
# 3. Construimos el DataFrame
dataframe_1 = pd.DataFrame(Frames, Rows, Columns)
print(dataframe_1)

# --- CREACIÓN DESDE UN DICCIONARIO ---
# Las claves del diccionario ('Grade', 'Price', 'State') se convierten en columnas.
# Las listas de valores son las filas.

dictionary_2 = {
    'Grade': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Price': [125, 236, 300, 300, 472, 600],
    'State': ['NY', 'CA', 'IL', 'IL', 'WI', 'NV']
}

dataframe_2 = pd.DataFrame(data=dictionary_2)
print(dataframe_2)