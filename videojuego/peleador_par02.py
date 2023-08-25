# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:47:22 2023

@author: hp
"""

import pygame

class Peleador():
    def __init__(self,x,y,hoja_movimientos,pasos_animacion):
        self.girar = False
        self.animacion_lista = self.cargar_imagen(hoja_movimientos,pasos_animacion)
        self.accion = 0
        self.indice_frame = 0
        self.imagen = self.animacion_lista[self.accion][self.indice_frame]
        self.rect = pygame.Rect((x,y,100,180))
        self.vel_y = 0
        self.saltando = False
        self.atacando = False
        self.ataque_tipo = 0
        self.salud = 100
        
    def cargar_imagen(self,hoja_movimientos,pasos_animacion):
        animacion_lista = []
        for y, animacion in enumerate(pasos_animacion):
            imagen_temporal_lista = []
            for x in range(animacion):
                imagen_temporal = hoja_movimientos.subsurface(944*x,944*y,944,944)
                imagen_temporal_reescalada = pygame.transform.scale(imagen_temporal,(472,472))
                imagen_temporal_lista.append(imagen_temporal_reescalada)
            animacion_lista.append(imagen_temporal_lista)
        return animacion_lista 
        
    def movimientos(self,ventana_ancho,ventana_alto,superficie,objetivo):
        VELOCIDAD = 10 # qué tan rápido se mueve cada peleador
        GRAVEDAD = 2
        dx = 0
        dy = 0
        
        '''reconocer teclas oprimidas'''
        tecla = pygame.key.get_pressed()
        
        '''Solo se puede mover si no esta ejecuando un ataque'''
        if self.atacando == False:
            '''Movimiento horizontal'''
            if tecla[pygame.K_a]:
                dx = -VELOCIDAD
            if tecla[pygame.K_d]:
                dx = VELOCIDAD
            '''saltos'''
            if tecla[pygame.K_w] and self.saltando == False:
                self.vel_y = -30
                self.saltando = True
            '''Ataques'''
            if tecla[pygame.K_r] or tecla[pygame.K_t]:
                self.ataque(superficie,objetivo)
                if tecla[pygame.K_r]:
                    self.ataque_tipo = 1
                if tecla[pygame.K_t]:
                    self.ataque_tipo = 2
            
        
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
        
        '''Asegurarse de que los peleadores estén frente a frente'''
        if objetivo.rect.centerx > self.rect.centerx:
            self.girar = False
        else:
            self.girar = True
        
        '''Actualizar posición del peleador'''
        self.rect.x = self.rect.x + dx
        self.rect.y = self.rect.y + dy
    
    def ataque(self,superficie, objetivo):
        self.atacando = True
        rectangulo_ataque = pygame.Rect(self.rect.centerx- (2*self.rect.width*self.girar), 
                                        self.rect.y,2*self.rect.width,self.rect.height)
        if rectangulo_ataque.colliderect(objetivo.rect):
            print("Golpe!")
            objetivo.salud = objetivo.salud - 10 
        pygame.draw.rect(superficie,(0,255,0),rectangulo_ataque)
        
    def dibujar(self,superficie):
        img = pygame.transform.flip(self.imagen,self.girar,False)
        pygame.draw.rect(superficie,(250,0,0),self.rect)
        superficie.blit(img,(self.rect.x-175,self.rect.y-130))
        