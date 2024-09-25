
import numpy as np

#? Crear un array a partir de una lista 
lista = [1, 2, 3] 
array = np.array(lista) 

#? Crear un array a partir de una tupla 
tupla = (4, 5, 6) 
array = np.array(tupla) 

#?2) Generación de Arrays Numéricos. NumPy proporciona funciones para generar arrays con valores predefinidos, como ceros, unos o secuencias numéricas. 

zeros = np.zeros(5)  #! Crea un array de 5 elementos con valores 0.0 
unos = np.ones(3)  #! Crea un array de 3 elementos con valores 1.0 
secuencia = np.arange(1, 6)  #! Crea un array con valores del 1 al 5 

#?3) Creación de Arrays Vacíos. También puedes crear arrays vacíos de cierto tamaño sin inicializar sus valores. 

vacio = np.empty(4)  #! Crea un array de 4 elementos sin valores definidos 

#? 4) Arrays de Números Aleatorios. NumPy incluye una variedad de funciones para generar arrays de números aleatorios. 
#? Crear un array de números aleatorios entre 0 y 1 
aleatorios = np.random.rand(3)  # Crea un array de 3 elementos 

#* Aritmética de arrays y operaciones vectorizadas NumPy permite realizar operaciones aritméticas básicas (suma, resta, multiplicación, división) 
#* de forma vectorizada sobre arrays. Esto significa que puedes aplicar una operación a cada elemento del array sin necesidad de bucles explícitos, 
#* lo que resulta en un código más eficiente y conciso. 

#?1) Suma. Se puede realizar la suma de dos o más arrays utilizando el operador + o la función np.add() 

#? Crear dos arrays 
array1 = np.array([1, 2, 3]) 
array2 = np.array([4, 5, 6]) 

#? Sumar los dos arrays 
resultado = array1 + array2 
print(resultado, "1")

#? También puedes usar np.add()
 
resultado = np.add(array1, array2) 
print(resultado, "2")

#* RESTA
#? También puedes usar np.subtract()    
resultado = np.subtract(array1, array2)
print(resultado, "3")

#* MULTIPLICACIÓN
#? También puedes usar np.dot()    
resultado = np.dot(array1, array2)
print(resultado, "4")

#! Adicionalmente, NumPy ofrece una amplia gama de funciones matemáticas para aplicar a todo el array como: 

# Crear un array de ángulos en radianes    
angulos = np.array([0, np.pi/4, np.pi/2])    

# Calcular el seno de los ángulos    
seno = np.sin(angulos)    

# Calcular el coseno de los ángulos 
coseno = np.cos(angulos) 

# Crear un array de números    
numeros = np.array([1, 2, 3, 4, 5])    

# Calcular el exponencial de los números    
exponencial = np.exp(numeros)    

# Calcular el logaritmo natural de los números    
logaritmo_natural = np.log(numeros)    

# Calcular el logaritmo en base 10 de los números    
logaritmo_base_10 = np.log10(numeros) 

datos = np.array([12, 15, 18, 20, 22])    

# Calcular la mediana    
mediana = np.median(datos)  # Resultado: 18.0    

# Calcular la desviación estándar    
desviacion_estandar = np.std(datos)  # Resultado: 3.391164991562634    

# Calcular la varianza    
varianza = np.var(datos)  # Resultado: 11.559999999999999    

# Calcular el percen l 75    
percentil_75 = np.percentile(datos, 75)  # Resultado: 20.0 

#*  Comparación Elemento a Elemento 

array1 = np.array([1, 2, 3, 4]) 
array2 = np.array([4, 2, 2, 4]) 

# Compara si los elementos de array1 son mayores que los de array2 
# 
comparacion = array1 > array2  # Resultado: [False, False, True, False] 
print(comparacion)


array = np.array([1, 2, 3, 4, 5, 6]) 

# Uso de operaciones lógicas para filtrar 
filtro = (array > 2) & (array < 5)  # Resultado: [False, False, True, True, False, False] 