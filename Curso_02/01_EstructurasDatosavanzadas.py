'''
Un profesor está gestionando las calificaciones de sus estudiantes en un curso y necesita un programa que le ayude a realizar las siguientes acciones: 
• Agregar un estudiante que se acaba de inscribir en el curso • Calcular el promedio de las calificaciones para analizar como está avanzado el curso 
• Encontrar al estudiante con el promedio más alto para destacarlo y elogiar su empeño 
• Encontrar la sublista de calificaciones de Pedro Martínez del segundo al quinto examen 
'''

registro_calificaciones = { "Juan Pérez": [90, 85, 92, 88, 95], 
                           "María Rodríguez": [78, 85, 88, 92, 79], 
                           "Carlos González": [95, 89, 92, 87, 91], 
                           "Ana López": [88, 92, 85, 90, 94], 
                           "Pedro Martínez": [92, 93, 87, 91, 96] } 

def agregandoEstudiante():
    global registro_calificaciones
    nombre = input("Ingresa el nombre(s) del alumno => ")
    apellido = input("Ingresa el apellido(s) del alumno => ")
    alumno = nombre + " " + apellido
    registro_calificaciones = {**registro_calificaciones, alumno: [] }
    print(registro_calificaciones)

#!=======================================================================================
#! ESTAS SON LAS RESPUESTAS DEL PROFE
#!=======================================================================================
def agregar_estudiante(nombre, calificaciones):
    registro_calificaciones[nombre] = calificaciones 

#!=======================================================================================

def calcular_PromedioCalificaciones():
    global registro_calificaciones
    suma_calificaciones = 0
    cantidad_calificaciones = 0
    for calificaciones in registro_calificaciones.values():
        # Sumar todas las calificaciones
        suma_calificaciones += sum(calificaciones)
        # Contar cuántas calificaciones tiene
        cantidad_calificaciones += len(calificaciones)
    
    if cantidad_calificaciones > 0:  # Evitar división por cero
        promedio = suma_calificaciones / cantidad_calificaciones
    else:
        promedio = 0
    
    print(f"Promedio de calificaciones: {promedio}")

#!=======================================================================================
#! ESTAS SON LAS RESPUESTAS DEL PROFE
#!=======================================================================================
def promedio_curso():
    total_estudiantes = len(registro_calificaciones)
    suma_total = sum(sum(calificaciones) for calificaciones in registro_calificaciones.values())
    numero_total_calificaciones = sum(len(calificaciones) for calificaciones in registro_calificaciones.values())
    return suma_total / numero_total_calificaciones 

#!=======================================================================================



def encontrando_mejorEstudiante():
    global registro_calificaciones

    mejor_estudiante = ""
    mejor_promedio = 0
    
    for estudiante, calificaciones in registro_calificaciones.items():
        # Inicializar suma y contador para cada estudiante
        suma_calificaciones = sum(calificaciones)
        cantidad_calificaciones = len(calificaciones)
    
        if cantidad_calificaciones > 0:  # Evitar división por cero
            promedio_local = suma_calificaciones / cantidad_calificaciones
            if promedio_local > mejor_promedio:
                mejor_estudiante = estudiante
                mejor_promedio = promedio_local
    
    print(f"El mejor estudiante actualmente es: {mejor_estudiante} con un promedio de: {mejor_promedio}")

#!=======================================================================================
#! ESTAS SON LAS RESPUESTAS DEL PROFE
#!=======================================================================================

def estudiante_mejor_promedio(): 
    mejor_promedio = 0 
    nombre_mejor_estudiante = "" 
    for nombre, calificaciones in registro_calificaciones.items():
        promedio = sum(calificaciones) / len(calificaciones) 
        if promedio > mejor_promedio: 
            mejor_promedio = promedio 
            nombre_mejor_estudiante = nombre 
    return nombre_mejor_estudiante 


#!=======================================================================================


def encontrar_calificaciones():
    nombres_ordenados = sorted(registro_calificaciones.keys())
    # Imprimir los nombres ordenados
    print("Tus alumnos son: \n")
    for nombre in nombres_ordenados:
        print(nombre)

    estudiante= input("¿De quien necesitas calificación? =>")
    inicio = int(input("¿Desde que periodo necesitas la calificacion?"))
    final = int(input("Hasta que periodo necesitas la calificacion?"))
    print(f"Calificaciones de {estudiante} son {registro_calificaciones[estudiante][inicio-1:final]}")

#!=======================================================================================
#! ESTAS SON LAS RESPUESTAS DEL PROFE
#!=======================================================================================

def calificaciones_pedro(): return registro_calificaciones["Pedro Martínez"][1:5] 

#!=======================================================================================



def inicio():
    opcion = input(" 1 = Agregar Alumno \n 2 = Calcular el promedio en general \n 3 = Encontrar al mejor estudiante \n 4 = Calificaciones por periodo y por estudiante \n Hola, ¿Que deseas hacer? => ")
    if opcion=="1":
        agregandoEstudiante()
    elif opcion=="2":
        calcular_PromedioCalificaciones()
    elif opcion=="3":
        encontrando_mejorEstudiante()
    elif opcion=="4":
        encontrar_calificaciones()
    else:
        print("La opciónq eu seleccionaste no hace nada")


inicio()


