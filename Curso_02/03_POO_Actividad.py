


class Libro:
    def __initi__(self, titulo, autor, añoPublicacion):
        self.titulo= titulo
        self.autor = autor
        self.añoPublicacion = añoPublicacion

    def mostrar_detalles(self):
        print(f"Titulo del Libre: {self.titulo}, su autor es: {self.autor} y fue publicado en el año {self.añoPublicacion}")

class Prestamo(Libro):
    def __init__(self, titulo, autor, añoPublicacion, prestario , fechaPrestamo):
        super().__init__(titulo, autor, añoPublicacion)  
        self.prestario = prestario
        self.fechaPrestamo = fechaPrestamo  

    def mostrar_detalles(self):
        print(f"Libro {self.titulo}  se presto a {self.prestario}")




class TelefonoMovil:     
    def __init__(self, marca, modelo, sistema_operativo, precio):         
        self.marca = marca         
        self.modelo = modelo         
        self.sistema_operativo = sistema_operativo         
        self.precio = precio      
        
    def __eq__(self, otro_telefono):         
        return (self.marca == otro_telefono.marca 
                and self.modelo == otro_telefono.modelo 
                and self.sistema_operativo == otro_telefono.sistema_operativo 
                and self.precio == otro_telefono.precio)      
        
    def __str__(self):         
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Sistema Operativo: {self.sistema_operativo}, Precio: {self.precio}"  
    
# Crear dos instancias de la clase TelefonoMovil 
telefono1 = TelefonoMovil("MarcaA", "ModeloA", "Android", 300) 
telefono2 = TelefonoMovil("MarcaB", "ModeloB", "iOS", 1000) 

 # Comparar los dos teléfonos son_iguales = telefono1 == telefono2  telefono1, telefono2, son_iguales 