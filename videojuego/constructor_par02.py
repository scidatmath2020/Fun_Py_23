# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:57:32 2023

@author: hp
"""

import os
import pygame


ruta_principal = "C:\\Users\\hp master\\OneDrive\\Escritorio\\juego_dbz\\"
os.chdir(ruta_principal)

from peleador_par01 import *

#%%

pygame.init()


'''crear ventana del juego'''

VENTANA_ANCHO = 1200
VENTANA_ALTO = 600

ventana = pygame.display.set_mode((VENTANA_ANCHO,VENTANA_ALTO))
pygame.display.set_caption("Dragon Ball Z de SciData")

'''Configurar frames por segundo'''
reloj = pygame.time.Clock()
FPS = 60

'''Cargar el escenario'''
escenario_imagen = pygame.image.load(ruta_principal + "activos\\imagenes\\fondos\\torneo.png")

'''Cargar imagenes de los peleadores'''
jugador1_hoja = pygame.image.load(ruta_principal + "activos\\imagenes\\guerreros\\otro_goku_sf.png")
jugador2_hoja = pygame.image.load(ruta_principal + "activos\\imagenes\\guerreros\\otro_vegeta_sf.png")

'''Definir número de pasos de las animaciones'''
jugador1_pasos = [10,4,1,5,12,4,4]
jugador2_pasos = [10,6,1,5,12,5,5]


def dibujar_escenario():
    escenario_escalado = pygame.transform.scale(escenario_imagen,(VENTANA_ANCHO,VENTANA_ALTO))
    ventana.blit(escenario_escalado,(0,0))

'''funcion para marcar las barras de salud'''
def dibujar_salud(salud,x,y):
    radio = salud/100
    pygame.draw.rect(ventana,(255,255,255),(x-5,y-5,410,40))
    pygame.draw.rect(ventana,(255,0,0),(x,y,400,30))
    pygame.draw.rect(ventana,(255,255,0),(x,y,400*radio,30))



'''Crear dos instancias de la clase Peleador'''

peleador1 = Peleador(200,330,jugador1_hoja,jugador1_pasos)
peleador2 = Peleador(900,330,jugador2_hoja,jugador2_pasos)   
    
run = True
while run:
    reloj.tick(FPS)   
    
    
    '''dibujar el escenario'''
    dibujar_escenario()
    
    '''dibujar peleadores'''
    peleador1.dibujar(ventana)
    peleador2.dibujar(ventana)

    '''dibujar rectángulos de salud'''
    dibujar_salud(peleador1.salud,120,20)
    dibujar_salud(peleador2.salud,680,20)

    '''mover jugadores'''
    peleador1.movimientos(VENTANA_ANCHO,VENTANA_ALTO,ventana,peleador2)
#    peleador2.movimientos(VENTANA_ANCHO)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    '''actualizar pantalla'''
    pygame.display.update()
    
pygame.quit()













