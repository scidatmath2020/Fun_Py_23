# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:08:37 2023

@author: hp
"""

def saludo():
    print("hola mundo")


class CarroBásico:
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        pass
    
    def frenar(self):
        pass
    
class CarroConColor:
    def __init__(self,color = "negro"):
        self.color = color # Esto es un atributo
        
    def describir(self):
        print(f"Carro de color {self.color}")
    
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        pass
    
    def frenar(self):
        pass    
    
class CarroVariable:
    def __init__(self,modelo, velocidad_maxima, color = "negro"):
        self.color = color # Esto es un atributo
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el carro está detenido
        
    def describir(self):
        descripcion = f"Carro modelo {self.modelo} de color {self.color} con velocidad máxima de {self.velocidad_maxima} km/h"
        return descripcion
    
    def estado(self):
        if self.velocidad == 0:
            print("El carro está detenido")
        else:
            print(f"El carro va a {self.velocidad} km/h")
    
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        pass
    
    def frenar(self):
        pass    

class Carro:
    def __init__(self,modelo, velocidad_maxima, color = "negro"):
        self.color = color # Esto es un atributo
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el carro está detenido
        
    def describir(self):
        descripcion = f"Carro modelo {self.modelo} de color {self.color} con velocidad máxima de {self.velocidad_maxima} km/h"
        return descripcion
    
    def __repr__(self):
        return "Hola mundo"#self.describir()
    
    def estado(self):
        if self.velocidad == 0:
            print("El carro está detenido")
        elif self.velocidad > 0:
            print(f"El carro va a {self.velocidad} km/h")
        else:
            print(f"El vehículo va marcha atrás a {-self.velocidad} km/h")
            
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Subiendo la velocidad en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad + diferencia_velocidad
            self.velocidad = min(self.velocidad,self.velocidad_maxima)
        else:
            print("No se puede acelerar negativamente")
            
    def frenar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Frenando en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad - diferencia_velocidad
            self.velocidad = max(self.velocidad,-5) 


class Autobús(Carro):
    def acelerar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Subiendo la velocidad en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad + diferencia_velocidad
            self.velocidad = min(self.velocidad,100)
        else:
            print("No se puede acelerar negativamente")
            
    def frenar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Frenando en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad - diferencia_velocidad
            self.velocidad = max(self.velocidad,0)