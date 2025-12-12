import pandas as pd
import numpy as np
import seaborn as sns # Esta librería se usa al final para gráficos
import matplotlib.pyplot as plt
# Cargar el DataFrame (Ajusta la ruta si es necesario)
df_grades = pd.read_csv(r'C:\Users\kevin\OneDrive\Documentos\CURSO DE PYTHON\modulo_3\StudentGrades.csv')

# Mostrar los datos
print(df_grades)

# Calcular el promedio (media) de la Matrícula (Tuition)
print("Promedio de Matrícula:", df_grades['Tuition'].mean())

# Calcular la mediana de las Horas de Oficina Participadas
print("Mediana de Horas de Oficina:", df_grades['OfficeHoursParticipated'].median())

# Calcular la moda de Clases Saltadas (el número más común)
print("Moda de Clases Saltadas:\n", df_grades['ClassesSkipped'].mode())

# Calcular la media de múltiples columnas a la vez
print("\nMedia de Matrícula y Clases Saltadas:\n", df_grades[['Tuition','ClassesSkipped']].mean())

# Varianza de todo el DataFrame (solo columnas numéricas)
print("Varianza del DataFrame:\n", df_grades.var(numeric_only=True))

# Desviación Estándar de todo el DataFrame
print("\nDesviación Estándar del DataFrame:\n", df_grades.std(numeric_only=True))

# Varianza de una columna específica (Matrícula)
print("\nVarianza de Matrícula:", df_grades['Tuition'].var())

# Desviación Estándar de una columna específica (Matrícula)
print("Desviación Estándar de Matrícula:", df_grades['Tuition'].std())

# Ver un resumen estadístico de todas las columnas numéricas
print(df_grades.describe())

# 1. Calcular la media y la desviación estándar de las horas de oficina
mean = df_grades['OfficeHoursParticipated'].mean()
std = df_grades['OfficeHoursParticipated'].std()

# 2. Calcular el Z-score para cada estudiante: (Valor - Media) / Desviación Estándar
df_grades['z-score'] = (df_grades['OfficeHoursParticipated'] - mean) / std

# Mostrar los datos con la nueva columna z-score
print(df_grades.head())

# --- PASO 1: Crear columna numérica GPA basada en la nota (A, B, C...) ---
# np.select toma condiciones y valores a asignar si se cumplen esas condiciones
df_grades['GPA'] = np.select(
    [
        df_grades['GradeAverage'] == 'A',
        df_grades['GradeAverage'] == 'B',
        df_grades['GradeAverage'] == 'C',
        df_grades['GradeAverage'] == 'D',
        df_grades['GradeAverage'] == 'F'
    ],
    [4, 3, 2, 1, 0] # Valores correspondientes: A=4, B=3, etc.
)

# --- PASO 2: Calcular el Rango Intercuartil (IQR) ---
# Q3 = Percentil 75, Q1 = Percentil 25
q3 = np.percentile(df_grades['GPA'], 75)
q1 = np.percentile(df_grades['GPA'], 25)
IQR = q3 - q1

print(f"IQR calculado: {IQR}")

# --- PASO 3: Definir la regla del Outlier ---
# Un dato es outlier si es: Mayor que (Q3 + 1.5*IQR)  O  Menor que (Q1 - 1.5*IQR)
IQR_rule = (df_grades['GPA'] > q3 + 1.5 * IQR) | (df_grades['GPA'] < q1 - 1.5 * IQR)

# --- PASO 4: Crear columna 'Outlier' ---
# np.where(condición, valor_si_verdad, valor_si_falso)
df_grades['Outlier'] = np.where(IQR_rule, 'yes', 'no')

# Ver resultados (fíjate en los que dicen 'yes')
print(df_grades)

# --- 6. CORRELACIÓN Y GRÁFICO ---
print("--- MATRIZ DE CORRELACIÓN ---")
# Solo usamos columnas numéricas para evitar errores
corr_matrix = df_grades.corr(numeric_only=True)
print(corr_matrix)

# Gráfico de calor (Heatmap)
print("\nGenerando gráfico de calor... (Revisa la ventana emergente)")
plt.figure(figsize=(8, 6)) # Tamaño de la ventana
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True) # annot=True pone los números en los cuadros
plt.title("Mapa de Calor de Correlación")

# ESTA LÍNEA ES CLAVE EN VS CODE PARA VER EL GRÁFICO
plt.show()