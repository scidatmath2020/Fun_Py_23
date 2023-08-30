# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:57:32 2023

@author: hp
"""

import os
import pygame
from pygame import mixer


ruta_principal = "C:\\Users\\hp master\\OneDrive\\Escritorio\\juego_dbz\\"
os.chdir(ruta_principal)

from peleador_par03 import *

#%%

mixer.init()
pygame.init()

'''crear ventana del juego'''

VENTANA_ANCHO = 1200
VENTANA_ALTO = 600

ventana = pygame.display.set_mode((VENTANA_ANCHO,VENTANA_ALTO))
pygame.display.set_caption("Dragon Ball Z de SciData")

'''Configurar frames por segundo'''
reloj = pygame.time.Clock()
FPS = 60

'''definir variables del juego'''
contador_intro = 4
ultima_actualizacion_tiempo = pygame.time.get_ticks()
victorias = [0,0] # [victorias de jugador 1, victorias del jugador 2]
round_finalizado = False
ROUND_FINALIZADO_RALENTIZADOR = 2000

'''Cargar música de fondo'''
pygame.mixer.music.load(ruta_principal + "activos\\audio\\dbz.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1,0.0,5000) # -1: ciclo continuo; 0.0 inicia el audio desde el princio; 5000 milisegundos para alcanzar el audio máximo

jugador1_grito = pygame.mixer.Sound(ruta_principal + "activos\\audio\\goku.wav")
jugador1_grito.set_volume(1)
jugador2_grito = pygame.mixer.Sound(ruta_principal + "activos\\audio\\vegueta.wav")
jugador2_grito.set_volume(1)

'''Cargar el escenario'''
escenario_imagen = pygame.image.load(ruta_principal + "activos\\imagenes\\fondos\\torneo.png")

'''Cargar imagenes de los peleadores'''
jugador1_hoja = pygame.image.load(ruta_principal + "activos\\imagenes\\guerreros\\otro_goku_sf.png")
jugador2_hoja = pygame.image.load(ruta_principal + "activos\\imagenes\\guerreros\\otro_vegeta_sf.png")

'''Cargar imagen de victoria'''

imagen_victoria = pygame.image.load(ruta_principal + "activos\\imagenes\\iconos\\victory.png")


'''Definir fuentes'''
contador_fuente = pygame.font.Font(ruta_principal + "activos\\fuentes\\turok.ttf",80)
victorias_fuente = pygame.font.Font(ruta_principal + "activos\\fuentes\\turok.ttf",30)

'''Definir nombres de los jugadores'''
peleador1_nombre = "Goku"
peleador2_nombre = "Vegueta"


'''Definir número de pasos de las animaciones'''
jugador1_pasos = [10,4,1,5,12,4,4]
jugador2_pasos = [10,6,1,5,12,5,5]

'''Definir alcances de los peleadores'''
jugador1_alcance_ataque1 = 1.2
jugador1_alcance_ataque2 = 1.5

jugador2_alcance_ataque1 = 1.5
jugador2_alcance_ataque2 = 1.2


'''Función para añadir textos'''
def dibujar_texto(texto, fuente, color_texto, x,y):
    img = fuente.render(texto, True, color_texto)
    ventana.blit(img,(x,y))


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

peleador1 = Peleador(1,200,330,
                     False,
                     jugador1_hoja,
                     jugador1_pasos,
                     jugador1_alcance_ataque1,
                     jugador1_alcance_ataque2,
                     jugador1_grito)
peleador2 = Peleador(2,900,330,
                     True,
                     jugador2_hoja,
                     jugador2_pasos,
                     jugador2_alcance_ataque1,
                     jugador2_alcance_ataque2,
                     jugador2_grito)   
    
run = True
while run:
    reloj.tick(FPS)   
    
    
    '''dibujar el escenario'''
    dibujar_escenario()
    
    '''dibujar peleadores'''
    peleador1.dibujar(ventana)
    peleador2.dibujar(ventana)

    '''Revisar si algún jugador ha perdido el round'''
    if round_finalizado == False:
        if peleador1.vivo == False:
            victorias[1] = victorias[1] + 1
            round_finalizado = True
            hora_round_finalizado = pygame.time.get_ticks()
        elif peleador2.vivo == False:
            victorias[0] = victorias[0] + 1
            round_finalizado = True
            hora_round_finalizado = pygame.time.get_ticks()
    else:
        '''mostrar letrero de victoria'''
        ventana.blit(imagen_victoria, (VENTANA_ANCHO/2 - 150, VENTANA_ALTO/3 - 100))
        if pygame.time.get_ticks() - hora_round_finalizado > ROUND_FINALIZADO_RALENTIZADOR:
            round_finalizado = False
            contador_intro = 4
            peleador1 = Peleador(1,200,330,
                                 False,
                                 jugador1_hoja,
                                 jugador1_pasos,
                                 jugador1_alcance_ataque1,
                                 jugador1_alcance_ataque2,
                                 jugador1_grito)
            peleador2 = Peleador(2,900,330,
                                 True,
                                 jugador2_hoja,
                                 jugador2_pasos,
                                 jugador2_alcance_ataque1,
                                 jugador2_alcance_ataque2,
                                 jugador2_grito)   
            
            

    '''dibujar rectángulos de salud'''
    dibujar_salud(peleador1.salud,120,20)
    dibujar_salud(peleador2.salud,680,20)
    dibujar_texto(f"{peleador1_nombre}: {victorias[0]}", victorias_fuente, (128,0,0), 400, 50)
    dibujar_texto(f"{peleador2_nombre}: {victorias[1]}", victorias_fuente, (128,0,0), 750, 50)

    '''Actualizar cuentra regresiva'''
    if contador_intro <= 0:
        '''mover jugadores'''
        peleador1.movimientos(VENTANA_ANCHO,VENTANA_ALTO,ventana,peleador2,round_finalizado)
        peleador2.movimientos(VENTANA_ANCHO,VENTANA_ALTO,ventana,peleador1,round_finalizado)
    else:
        '''mostrar contador de tiempo en la pantalla'''
        dibujar_texto(str(contador_intro), contador_fuente, (255,0,0), VENTANA_ANCHO/2, VENTANA_ALTO/3 - 100)
        '''actualizar contador intro'''
        if pygame.time.get_ticks() - ultima_actualizacion_tiempo >= 1000:
            contador_intro = contador_intro - 1 
            ultima_actualizacion_tiempo = pygame.time.get_ticks()
            

    peleador1.actualizar()
    peleador2.actualizar()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    '''actualizar pantalla'''
    pygame.display.update()
    
pygame.quit()













