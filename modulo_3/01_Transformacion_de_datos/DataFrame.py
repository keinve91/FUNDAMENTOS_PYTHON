import pandas as pd
import numpy as np

# Cargar los datos de calificaciones de estudiantes
df_grades = pd.read_csv(r'C:\Users\kevin\OneDrive\Documentos\CURSO DE PYTHON\modulo_3\StudentGrades.csv')

# Mostrar el DataFrame
print(df_grades)

# Seleccionar una columna específica (devuelve una Serie)
print(df_grades['StudentID'])

# Seleccionar múltiples columnas pasando una lista
print(df_grades[['StudentID','FirstName']])

# Mostrar las primeras 5 filas
print(df_grades.head())

# Mostrar las últimas 5 filas
print(df_grades.tail())

# loc: Seleccionar todas las filas (:), pero solo columnas específicas por nombre
print(df_grades.loc[:,['StudentID','GradeAverage']])

# iloc: Seleccionar todas las filas (:), pero solo columnas en posiciones 0 y 3
print(df_grades.iloc[:,[0,1]])

# loc: Todas las filas, columnas desde 'StudentID' hasta 'GradeAverage'
print(df_grades.loc[:,'StudentID':'GradeAverage'])

# iloc: Todas las filas, columnas desde la posición 0 hasta la 3 (la 4 no se incluye)
print(df_grades.iloc[:,0:4])

# loc: Seleccionar filas específicas por nombre de índice (aquí son números) y todas las columnas
print(df_grades.loc[[0,3],:])

# iloc: Seleccionar filas en posiciones 0 y 3, todas las columnas
print(df_grades.iloc[[0,3],:])

# loc: Rango de filas (incluye el final en loc)
print(df_grades.loc[0:3,:])

# iloc: Rango de filas (NO incluye el final en iloc)
print(df_grades.iloc[0:3,:])

# Crear una condición booleana: Matrícula mayor o igual a 40,000

student_tuition40k = df_grades['Tuition'] >= 44000
# Mostrar el resultado booleano
print(student_tuition40k)

# Filtrar el DataFrame usando la condición anterior
print(df_grades[student_tuition40k])

# Forma directa: Estudiantes con matrícula >= 40k
df_grades[df_grades['Tuition'] >= 40000]

# Filtrar por igualdad: Estudiantes en la facultad de 'Arts'
print(df_grades[df_grades['Faculty'] == 'Arts'])

# Múltiples condiciones: Al menos 3 clases saltadas Y (AND) 5 horas de oficina o más
print(df_grades[(df_grades['ClassesSkipped'] >= 5) & (df_grades['OfficeHoursParticipated'] >= 5)])

# --- AGREGAR COLUMNAS ---

# Crear una lista de ciudades (debe coincidir con la longitud del DataFrame)
city = ['Vancouver','Toronto','Calgary','Edmonton','Regina', 'Burnaby', 'Coquitlam', 'London', 'Ottawa', 'Texas',
       'Coquitlam', 'London', 'Ottawa', 'Texas','Edmonton','Regina', 'Burnaby', 'Coquitlam', 'London', 'Ottawa', 
        'Texas', 'Toronto','Calgary','Edmonton','Regina', 'Burnaby', 'Coquitlam', 'London',  'Texas','Edmonton'
       ]
# Asignar la lista a una nueva columna llamada 'City'
df_grades['City'] = city

# Usar insert() para añadir una columna en una posición específica (índice 1)
df_grades.insert(1, "Age", [21, 23, 24, 21, 25, 18, 22, 25, 28, 34, 
                     22, 23, 25, 21, 25, 26, 24, 23, 29, 31, 
                     28, 24, 24, 23, 22, 20, 23, 25, 28, 33 
                    ])

# --- AGREGAR FILAS ---

# Crear datos para un nuevo estudiante
new_student = {'StudentID': 20123420, 'Age':21, 'FirstName': 'Scottie', 'LastName': 'Barnes', 'GradeAverage': 'A', 
               'Faculty': 'Science', 'Tuition': 50000,'OfficeHoursParticipated': 0, 'ClassesSkipped': 0, 'City': 'Toronto'}

# Convertir a DataFrame
df2 = pd.DataFrame(data=new_student, index=[30])

# Concatenar el nuevo estudiante al DataFrame original
df_grades = pd.concat([df_grades,df2])

# --- ELIMINAR DATOS ---

# Eliminar fila por número de índice (ej. borrar al estudiante recién agregado)
df_grades = df_grades.drop([30])

# Identificar estudiantes de 'Business' para borrarlos
business_students = df_grades['Faculty'] == 'Business'

# Eliminar filas basándose en la condición (usando los índices de esa condición)
df_grades = df_grades.drop(df_grades[business_students].index)

# Eliminar una columna entera (axis=1), por ejemplo 'City'
df_grades = df_grades.drop(['City'], axis = 1)

# Establecer 'StudentID' como el nuevo índice
df_grades = df_grades.set_index('StudentID')

# Revertir al índice numérico original
df_grades = df_grades.reset_index()

# Contar cuántos StudentIDs hay por cada Facultad
df_grades.groupby(by='Faculty')['StudentID'].count()

# Calcular el promedio de edad por cada Facultad
df_grades.groupby(by='Faculty')['Age'].mean()

# Agrupar por Facultad Y Promedio de Notas, luego sumar la Matrícula
df_grades.groupby(by=['Faculty','GradeAverage'])['Tuition'].sum()

# Crear un segundo DataFrame con datos adicionales
data2 = {'StudentID': [20123420,20123421], 'Age':[33,31], 'FirstName': ['Stephen','Klay'], 
         'LastName': ['Curry','Thompson'], 'GradeAverage': ['A','A'], 'Faculty': ['Science','Math'], 
         'Tuition': [31000,41000], 'OfficeHoursParticipated': [3,1], 'ClassesSkipped': [4,6], 
         'State': ['California','California']}
df_grades2 = pd.DataFrame(data2)

# Concatenación VERTICAL (añadir filas abajo)
# Nota: Si las columnas no coinciden exactamente, se crean valores NaN
pd.concat([df_grades,df_grades2])

# Concatenación HORIZONTAL (añadir columnas al lado, axis=1)
# Útil si se añaden datos nuevos para las mismas filas existentes
pd.concat([df_grades,df_grades2], axis = 1)