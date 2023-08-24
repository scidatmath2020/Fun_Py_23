# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:57:32 2023

@author: hp
"""

import os
import pygame
from peleador import *

ruta_principal = "C:\\Users\\hp master\\OneDrive\\Escritorio\\juego_dbz\\"

os.chdir(ruta_principal)

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

def dibujar_escenario():
    escenario_escalado = pygame.transform.scale(escenario_imagen,(VENTANA_ANCHO,VENTANA_ALTO))
    ventana.blit(escenario_escalado,(0,0))

'''Crear dos instancias de la clase Peleador'''
    
peleador1 = Peleador(200,330)
peleador2 = Peleador(900,330)   
    
run = True
while run:
    reloj.tick(FPS)   
    
    
    '''dibujar el escenario'''
    dibujar_escenario()
    
    '''dibujar peleadores'''
    peleador1.dibujar(ventana)
    peleador2.dibujar(ventana)

    '''mover jugadores'''
    peleador1.movimientos(VENTANA_ANCHO,VENTANA_ALTO)
#    peleador2.movimientos(VENTANA_ANCHO)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    '''actualizar pantalla'''
    pygame.display.update()
    
pygame.quit()













