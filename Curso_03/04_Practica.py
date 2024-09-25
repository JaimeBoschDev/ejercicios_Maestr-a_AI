import pandas as pd


#*### **Uso Avanzado de Pandas y NumPy**

#***Contexto**:  
#*En una academia de ciencia de datos, los estudiantes enfrentan el desafío de analizar un dataset de ventas de videojuegos para identificar tendencias y patrones, agrupando datos por género, examinando correlaciones de ventas regionales, y combinando esta información con otro dataset de calificaciones de juegos para entender el impacto en las ventas globales.
#*
#***Objetivos:**
#*
#?- **Preparar datos para el análisis**:
#!  - Asegurar que los datos estén completos y listos para el análisis.
#*  
#?- **Análisis de ventas**:
#!  - Encontrar los juegos con ventas superiores a un millón de copias.
#*
#?- **Identificación de géneros populares**:
#!  - Determinar qué géneros atraen a más jugadores.
#*
#?- **Visualización de tendencias**:
#!  - Mostrar las ventas totales por año y género a través de una tabla pivote para visualizar las tendencias de la industria.
#*
#?- **Análisis combinado**:
#!  - Combinar el dataset de ventas con el de calificaciones para explorar cómo la recepción crítica afecta a las ventas.


df = pd.read_csv('video_game_sales.csv')

print(df.head(15))

#? Filtro por aquellos juegos que tengan más de un Millon de ventas

games_over_million = df[df['Global_Sales'] > 1] 
print("\nJuegos con Ventas Globales Superiores a un Millón de Copias (Primeros 5):") 
print(games_over_million.head()) 

#?  - Determinar qué géneros atraen a más jugadores.

average_sales_by_genre = df.groupby('Genre')['Global_Sales'].mean().sort_values(ascending=False) 
print("\nVentas Medias por Género:") 
print(average_sales_by_genre) 


#? Mostrar las ventas totales por año y género a través de una tabla pivote para visualizar las tendencias de la industria.
pivot_table = df.pivot_table(values='Global_Sales', index='Year_of_Release', columns='Genre', aggfunc='sum') 

#? Explicación de los parámetros:
#*values='Global_Sales':
#*
#*Especifica la columna cuyos valores quieres analizar, en este caso, las ventas globales (Global_Sales).
#*Los valores en esta columna se utilizarán como datos en la tabla pivote.
#*index='Year_of_Release':
#*
#*Define el índice de la tabla pivote. En este caso, se organiza por el año de lanzamiento (Year_of_Release), que se convertirá 
#* en las filas de la tabla.
#*columns='Genre':
#*
#*Define las columnas de la tabla pivote basándose en el género de los videojuegos (Genre). Cada columna representará un género diferente.
#*aggfunc='sum':
#*
#*Especifica la función de agregación que se usará para combinar los datos. En este caso, la función sum sumará las ventas 
#* globales de los juegos que caen dentro del mismo año y género.

print("\n Pivote:") 
print(pivot_table) 