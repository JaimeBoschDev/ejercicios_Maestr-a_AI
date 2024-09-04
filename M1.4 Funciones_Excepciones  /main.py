'''
Usando un cuaderno de Jupyter, se debe crear una función que calcule el área de un círculo utilizando un radio proporcionado como argumento. 
'''

def calcula_area_circulo(radio):
    return radio*3.1416


resultado = calcula_area_circulo(4)
print("Area => ", resultado)

'''
Trabajando con funciones Supongamos que tienes una función llamada viajar que simula un viaje y acepta tres argumentos:
 inicio, destino y precio,
  
    con el siguiente encabezado “def viajar(inicio, destino, precio=500)”. 
    
    Identifique cuál de las siguientes invocaciones son válidas: 
        • viajar("Ciudad A", "Ciudad B") SI
        • viajar(inicio="Ciudad A", destino="Ciudad B", precio=350)  SI
        • viajar(inicio="Ciudad A", precio=400, destino="Ciudad B") SI
        • viajar("Ciudad A", destino="Ciudad B", 300) SI
        • viajar(destino="Ciudad B", inicio="Ciudad A") SI
        • viajar("Ciudad A", "Ciudad B", precio="350") SI
'''

def calcular_imc():
    try:
        altura = int(input("Proporcione su altura en cm =>"))
        peso = int(input("Proporcione su peso en kg =>"))
        imc = peso / (altura*2)
        print("Tu IMC fue de => ", imc)
    except TypeError as e:
           print(f"Ocurrió un TypeError, deberías intentarlo de nuevo")
          

calcular_imc()