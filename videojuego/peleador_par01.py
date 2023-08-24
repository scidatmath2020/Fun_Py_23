# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:47:22 2023

@author: hp
"""

import pygame

class Peleador():
    def __init__(self,x,y):
        self.rect = pygame.Rect((x,y,100,180))
        self.vel_y = 0
        self.saltando = False
        
    def movimientos(self,ventana_ancho,ventana_alto):
        VELOCIDAD = 10 # qué tan rápido se mueve cada peleador
        GRAVEDAD = 2
        dx = 0
        dy = 0
        
        '''reconocer teclas oprimidas'''
        tecla = pygame.key.get_pressed()
        
        '''Movimiento horizontal'''
        if tecla[pygame.K_a]:
            dx = -VELOCIDAD
        if tecla[pygame.K_d]:
            dx = VELOCIDAD
        '''saltos'''
        if tecla[pygame.K_w] and self.saltando == False:
            self.vel_y = -30
            self.saltando = True
        
        '''Aplicar gravedad'''
        self.vel_y = self.vel_y + GRAVEDAD
        dy = dy + self.vel_y
        
        '''Mantener a los peleadores dentro de la ventana'''
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > ventana_ancho:
            dx = ventana_ancho - self.rect.right
        if self.rect.bottom + dy > ventana_alto - 90:
            self.vel_y = 0
            self.saltando = False
            dy = ventana_alto - 90 - self.rect.bottom
        
        
        '''Actualizar posición del peleador'''
        self.rect.x = self.rect.x + dx
        self.rect.y = self.rect.y + dy
        
        
    def dibujar(self,superficie):
        pygame.draw.rect(superficie,(250,0,0),self.rect)