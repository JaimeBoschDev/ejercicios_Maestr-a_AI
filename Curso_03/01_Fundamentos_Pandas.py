import pandas as pd
import math

#! Pandas 
#? Imagine que se encuentra trabajando como científico de datos para una 
#? frutería y le piden analizar las ventas de los últimos 2 años para lo 
#? que se requiere que: 
#? 1. Cargue el conjunto de datos en un DataFrame 
#? 2. Inspeccione los datos 
#? 3. Haga un filtrado de datos, donde se seleccionen aquellas ventas cuya cantidad sea mayor a 4 y cuyo producto sean “Naranjas” 
#? 4. Investigue el conjunto y rellene aquellos datos cuya “Cantidad” sea nula por el valor medio de la columna 
#? 5. Elimine posibles duplicados basándose en la combinación de “Fecha” y “Producto” 
#? 6. Añada una nueva columna “Total de Venta” que sea el resultado de multiplicar “Cantidad” por “Precio Unitario” 
#? 7. Reindexe el DataFrame basándose en la columna “Total de Venta” de mayor a menos. 

# Leer el archivo CSV
df = pd.read_csv('dataset_ventas.csv')

#! Mostrar las primeras 5 filas del dataframe para verificar su contenido
print("2. Inspeccione los datos ", df.head())

# Supongamos que las columnas son "categoria" y "valor"
categoria_filtro = 'Naranjas'  # El string con el que vas a comparar

df_Filtrado_Naranjas = df[ (df["Producto"]== categoria_filtro) & (df["Cantidad"] > 4) ]

# Mostrar el resultado
print("Haga un filtrado de datos, donde se seleccionen aquellas ventas cuya cantidad sea mayor a 4 y cuyo producto sean Naranjas", df_Filtrado_Naranjas)

# Obtener la media de la columna "valor"
media_valor = df['Cantidad'].mean()
# Redondear la media al siguiente entero
media_redondeada = math.ceil(media_valor)

# Mostrar el resultado
print(f"La media de la columna 'Cantidad' es: {media_redondeada}")

# Rellenar los valores nulos con la media redondeada
df['Cantidad'].fillna(media_redondeada, inplace=True)

# Mostrar el DataFrame actualizado
print("Investigue el conjunto y rellene aquellos datos cuya “Cantidad” sea nula por el valor medio de la columna ", df)

# Eliminar duplicados basados en la combinación de las columnas 'columna1' y 'columna2'
df_sin_duplicados = df.drop_duplicates(subset=['Producto', 'Fecha'], keep='first')

# Mostrar el DataFrame sin duplicados
print("Elimine posibles duplicados basándose en la combinación de “Fecha” y “Producto” \n" , df_sin_duplicados)

# Añadir una nueva columna 'resultado' que sea la multiplicación de 'columna1' y 'columna2'
df['Total de Venta'] = df['Precio Unitario'] * df['Cantidad']

print("Añada una nueva columna “Total de Venta” que sea el resultado de multiplicar “Cantidad” por “Precio Unitario” \n\n", df)

# Ordenar el DataFrame por la columna 'resultado' de mayor a menor
df_sorted = df.sort_values(by='Total de Venta', ascending=False)

# Reindexar el DataFrame para que los índices sean consecutivos después de ordenar
df_sorted.reset_index(drop=True, inplace=True)

# Mostrar el DataFrame ordenado y reindexado
print("Reindexe el DataFrame basándose en la columna “Total de Venta” de mayor a menos. ", df_sorted)