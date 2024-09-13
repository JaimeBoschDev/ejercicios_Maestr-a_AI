
#!Mejora de Código 
#? Imagine que se encuentra trabajando en un proyecto de desarrollo de software 
#? y se le proporciona el siguiente fragmento de código que requiere mejoras 
#? significativas en términos de buenas prácticas y estilos de codificación para que lo analice. 

def CalcularSuma(lista_de_numeros): 
    total = 0 
    for i in range(len(lista_de_numeros)): 
        total = total + lista_de_numeros[i] 
        return total 
    
lista_de_numeros = [10, 20, 30, 40, 50] 

# 2019 – 11 – 25  
resultado = CalcularSuma(lista_de_numeros) 
print("El resultado es:", resultado) 

contador = 100 

def MultiplicarNumeros(a, b): return a * b 

def calcular_suma(lista_de_numeros):
    """     
        Calcula la suma de los números en una lista.          
        Parámetros:     
            lista_de_numeros (list): Lista de números enteros o flotantes.          
            Retorna:     int o float: Suma de los números en la lista.    
    """     
    return sum(lista_de_numeros)  

def multiplicar_numeros(a, b):     
    """     
        Multiplica dos números.          
        Parámetros:     
            a (int o float): Primer número.     
            b (int o float): Segundo número.          
        Retorna:     int o float: Producto de a y b.     
    """     
    return a * b  

# Lista de números para calcular la suma 
lista_de_numeros = [10, 20, 30, 40, 50]             

# Calcular suma y mostrar resultado 
resultado = calcular_suma(lista_de_numeros) 
print("El resultado es:", resultado) 