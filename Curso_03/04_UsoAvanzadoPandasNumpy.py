import numpy as np
import pandas as pd
#!Técnicas Avanzadas en NumPy

#*NumPy es una biblioteca potente para la computación científica, permitiendo realizar operaciones complejas de álgebra lineal y manipulación de matrices.

#* Operaciones Matriciales y Álgebra Lineal: 
#?                                          NumPy facilita operaciones como la suma, resta, multiplicación de matrices, transposición 
#?                                            e inversión de matrices, así como el cálculo de eigenvalores y eigenvectores.


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicación de matrices
C = np.dot(A, B)

# Eigenvalores y eigenvectores
valores, vectores = np.linalg.eig(A)
print("Solución valores",valores)

# Solución de sistemas de ecuaciones
b = np.array([9, 8])
x = np.linalg.solve(A, b)

print("Solución x",x)


#* Indexación Booleana: 
#?                   Selecciona elementos de un array usando máscaras booleanas basadas en condiciones.

datos = np.array([10, 20, 30, 40, 50])
mascara = datos > 30
resultados = datos[mascara]
print("resultados", resultados)

#! Manipulación de Datos Complejos con Pandas

#*Pandas ofrece herramientas avanzadas para la manipulación y análisis de datos tabulares, permitiendo agrupar, pivotar y combinar conjuntos de datos de manera eficiente.

#*Agrupación de Datos: 
#?               Utilizando la función groupby(), es posible dividir un conjunto de datos en grupos basados en una columna, 
#?               y aplicar operaciones como suma dentro de cada grupo, similar a un GROUP BY en SQL.


datos = {'Categoría': ['A', 'B', 'A', 'B', 'A', 'B'], 'Valor': [10, 15, 12, 18, 8, 20]}
df = pd.DataFrame(datos)

grupos = df.groupby('Categoría')
print("grupos", grupos['Valor'])
suma_por_grupo = grupos['Valor'].sum()
print("suma_por_grupo", suma_por_grupo)


#* Pivoteo de Tablas: 
#?                   pivot() permite reorganizar los datos de una estructura tabular, facilitando su análisis.

datos = {'Fecha': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02'], 'Categoría': ['A', 'B', 'A', 'B'], 'Valor': [10, 15, 12, 18]}
df = pd.DataFrame(datos)
print("df", df)
tabla_pivote = df.pivot(index='Fecha', columns='Categoría', values='Valor')
print("\n tabla_pivote", tabla_pivote)


#* Combinación de Datasets:
#?                          merge(): Combina DataFrames en función de una columna común, similar a las uniones en SQL.

df1 = pd.DataFrame({'clave': ['A', 'B', 'C'], 'valor1': [1, 2, 3]})
df2 = pd.DataFrame({'clave': ['B', 'C', 'D'], 'valor2': [4, 5, 6]})

resultado = pd.merge(df1, df2, on='clave', how='inner')
print("\n \n resultado merge \n", resultado)


#?                  concat(): Apila DataFrames por filas o columnas.

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']})
df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'], 'B': ['B3', 'B4', 'B5']})

resultado = pd.concat([df1, df2])
print("\n resultado concat \n", resultado)
