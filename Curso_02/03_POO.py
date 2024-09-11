class Automovil: 
    def __init__(self, marca, modelo, año): 
        self.marca = marca 
        self.modelo = modelo 
        self.año = año 

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}") 

#?En este ejemplo, Automovil es una clase con atributos marca, modelo, y año. La palabra clave class se utiliza para definirla.  
#? Instanciación de Objetos  Crear una instancia de una clase significa crear un objeto específico basado en la estructura de esa clase. Por ejemplo, 

mi_auto = Automovil("Toyota", "Corolla", 2020) 

mi_auto.mostrar_informacion()

#! Ejemplo de Encapsulamiento  =========================================

#?Considera una clase CuentaBancaria con una variable privada _saldo. 
#? El saldo solo puede modificarse mediante métodos públicos como depositar o retirar, 
#? garantizando que las reglas de negocio se cumplan. 

class CuentaBancaria: 
    def __init__(self): 
        self._saldo = 0 
        
    def depositar(self, cantidad): 
        if cantidad > 0: 
            self._saldo += cantidad
            return True 
        return False 
    
    def retirar(self, cantidad): 
        if 0 < cantidad <= self._saldo: 
            self._saldo -= cantidad
            return True 
        return False 
    
#! Herencia =========================================
class Vehiculo:     
    def __init__(self, marca, modelo):         
        self.marca = marca         
        self.modelo = modelo  
        
class Automovil(Vehiculo):     
    def __init__(self, marca, modelo, tipo_combustible):         
        super().__init__(marca, modelo)         
        self.tipo_combustible = tipo_combustible


#!Polimorfismo =========================================

class Animal:     
    def emitir_sonido(self):         
        pass  

class Perro(Animal):     
    def emitir_sonido(self):         
        return "Ladrido"  

class Gato(Animal):     
    def emitir_sonido(self):         
        return "Maullido" 