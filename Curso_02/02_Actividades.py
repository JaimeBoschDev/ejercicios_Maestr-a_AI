'''
Usando un cuaderno de Jupyter, 
escribe las líneas de código necesarias para 
crear un fichero llamado “managing_files.txt”
 con “Aprendiendo a manejar ficheros con Python”. 
'''
#TODO EJERCICIO 1

with open("managing_files.txt", "w") as archivo:
    archivo.write("Aprendiendo Pÿthon")



#?Trabajando con ficheros Imaginemos que tenemos que leer el fichero anterior, 
#?¿podrías explicar que significa cada uno de las siguientes declaraciones? 

#!  a) f = open(“managing_files.txt”) .- lO ABRE CON PERMISOS DE R
#!  b) f = open(“managing_files.txt”,”a”) .- SOLO PUEDE AGREGAR EL ARCHVIO
                                        #? Esta declaración abre el archivo en modo de "append" ("a"). 
                                        #todo Esto significa que cualquier dato que escribas en el archivo se añadirá al final del contenido existente. 
                                        #? Si el archivo no existe, se creará un nuevo archivo. 
#!  c) f = open(“managing_files.txt”,”r+”) .- PUEDE LEER Y ESCRIBIR PERO EMPEZARA DEL INICIO
                                        #? Esta declaración abre el archivo en modo de lectura y escritura ("r+"). 
                                        #? Puedes leer y escribir en el archivo. Si el archivo no existe, se generará un error. 
                                        #todo Al escribir en el archivo, el contenido se sobrescribirá desde el principio, 
                                        #? lo que puede llevar a la pérdida de datos si no se maneja cuidadosamente. 
#!  d) f = open(“managing_files.txt”,”w”) .-PUEDE LEEER Y ESCRIBIR PERO SIEMPRE REEMPLAZARA
