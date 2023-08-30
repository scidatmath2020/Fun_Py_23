# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:47:22 2023

@author: hp
"""

import pygame

class Peleador():
    def __init__(self,jugador,x,y,giro,hoja_movimientos,pasos_animacion,alcance1,alcance2,sonido):
        self.jugador = jugador
        self.girar = giro
        self.animacion_lista = self.cargar_imagen(hoja_movimientos,pasos_animacion)
        self.accion = 0
        self.indice_frame = 0
        self.imagen = self.animacion_lista[self.accion][self.indice_frame]
        self.actualizar_tiempo = pygame.time.get_ticks()
        self.rect = pygame.Rect((x,y,100,180))
        self.vel_y = 0
        self.corriendo = False
        self.saltando = False
        self.atacando = False
        self.ataque_tipo = 0
        self.alcance_ataque1 = alcance1
        self.alcance_ataque2 = alcance2
        self.ataque_ralentizador = 0
        self.ataque_sonido = sonido
        self.hit1 = False
        self.hit2 = False
        self.salud = 100
        self.vivo = True
        
    def cargar_imagen(self,hoja_movimientos,pasos_animacion):
        animacion_lista = []
        for y, animacion in enumerate(pasos_animacion):
            imagen_temporal_lista = []
            for x in range(animacion):
                imagen_temporal = hoja_movimientos.subsurface(944*x,944*y,944,944)
                imagen_temporal_reescalada = pygame.transform.scale(imagen_temporal,(472,472))
                imagen_temporal_lista.append(imagen_temporal_reescalada)
            animacion_lista.append(imagen_temporal_lista)
        extra = []
        for x in animacion_lista[5]:
            extra.append(x)
            extra.append(x)
            extra.append(x)
        animacion_lista.append(extra)    
        return animacion_lista 
        
    def movimientos(self,ventana_ancho,ventana_alto,superficie,objetivo,round_finalizado):
        VELOCIDAD = 10 # qué tan rápido se mueve cada peleador
        GRAVEDAD = 2
        dx = 0
        dy = 0
        self.corriendo = False
        self.ataque_tipo = 0
        '''reconocer teclas oprimidas'''
        tecla = pygame.key.get_pressed()
        
        '''Solo se puede mover si no esta ejecuando un ataque o si está vivo'''
        if self.atacando == False and self.vivo == True and round_finalizado == False:
            ''' Controles del jugador 1'''
            
            if self.jugador == 1:
                '''Movimiento horizontal'''
                if tecla[pygame.K_a]:
                    dx = -VELOCIDAD
                    self.corriendo = True
                if tecla[pygame.K_d]:
                    dx = VELOCIDAD
                    self.corriendo = True
                '''saltos'''
                if tecla[pygame.K_w] and self.saltando == False:
                    self.vel_y = -30
                    self.saltando = True
                '''Ataques'''
                if tecla[pygame.K_r] or tecla[pygame.K_t]:
                    
                    if tecla[pygame.K_r]:
                        self.ataque_tipo = 1
                    if tecla[pygame.K_t]:
                        self.ataque_tipo = 2
                    self.ataque(superficie,objetivo)
            
            ''' Controles del jugador 2'''
            
            if self.jugador == 2:
                '''Movimiento horizontal'''
                if tecla[pygame.K_LEFT]:
                    dx = -VELOCIDAD
                    self.corriendo = True
                if tecla[pygame.K_RIGHT]:
                    dx = VELOCIDAD
                    self.corriendo = True
                '''saltos'''
                if tecla[pygame.K_UP] and self.saltando == False:
                    self.vel_y = -30
                    self.saltando = True
                '''Ataques'''
                if tecla[pygame.K_KP1] or tecla[pygame.K_KP2]:
                    
                    if tecla[pygame.K_KP1]:
                        self.ataque_tipo = 1
                    if tecla[pygame.K_KP2]:
                        self.ataque_tipo = 2
                    self.ataque(superficie,objetivo)
            
        
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
            
            
        '''Aplicar ralentizador de ataque'''
        if self.ataque_ralentizador > 0:
            self.ataque_ralentizador = self.ataque_ralentizador - 1
        
        '''Actualizar posición del peleador'''
        self.rect.x = self.rect.x + dx
        self.rect.y = self.rect.y + dy
        
    def actualizar(self):
        '''Revisar qué acción se está realizando'''
        if self.salud <= 0:
            self.salud = 0
            self.vivo = False
            self.actualizar_accion(6)
        elif self.hit1 == True or self.hit2 == True:
            if self.hit1 == True:
                self.actualizar_accion(5)
            elif self.hit2 == True:
                self.actualizar_accion(7)
        elif self.atacando == True:
            if self.ataque_tipo == 1:
                self.actualizar_accion(3)
            elif self.ataque_tipo == 2:
                self.actualizar_accion(4)
        elif self.saltando == True:
            self.actualizar_accion(2)
        elif self.corriendo == True:
            self.actualizar_accion(1)
        else:
            self.actualizar_accion(0)
        animacion_ralentizador = 50 # milisegundos
        self.imagen = self.animacion_lista[self.accion][self.indice_frame]
        ''' revisar si ha pasado suficiente tiempo desde la última actualización'''
        if pygame.time.get_ticks() - self.actualizar_tiempo > animacion_ralentizador:
            self.indice_frame = self.indice_frame + 1 
            self.actualizar_tiempo = pygame.time.get_ticks()
        '''revisar si la animación ha finalizado'''
        if self.indice_frame >= len(self.animacion_lista[self.accion]):
            if self.vivo == False:
                self.indice_frame = len(self.animacion_lista[self.accion])-1
            else:
                self.indice_frame = 0
                ''' revisar si la acción es un ataque'''
                if self.accion == 3 or self.accion == 4:
                    self.atacando = False
                    self.ataque_ralentizador = 50
                if self.accion == 5 or self.accion == 7:
                    self.hit1 = False
                    self.hit2 = False
                    '''Si el jugador está recibiendo un ataque, no puede atacar'''
                    self.atacando = False
                    self.ataque_ralentizador = 50
                
        
        
    
    def ataque(self,superficie, objetivo):
        if self.ataque_ralentizador == 0:
            self.atacando = True
            self.ataque_sonido.play()
            if self.ataque_tipo == 1:
                alcance = self.alcance_ataque1
                danio = 5
            elif self.ataque_tipo == 2:
                alcance = self.alcance_ataque2
                danio = 10
            
            rectangulo_ataque = pygame.Rect(self.rect.centerx- (alcance*self.rect.width*self.girar), 
                                            self.rect.y,alcance*self.rect.width,self.rect.height)
            if rectangulo_ataque.colliderect(objetivo.rect):
                #print("Golpe!")
                objetivo.salud = objetivo.salud - danio
                if self.ataque_tipo == 1:
                    objetivo.hit1 = True
                    
                elif self.ataque_tipo == 2:
                    objetivo.hit2 = True
                    
            #pygame.draw.rect(superficie,(0,255,0),rectangulo_ataque)
        
    def actualizar_accion(self,nueva_accion):
        '''revisar si la acción nueva es igaal a la anterior'''
        if nueva_accion != self.accion:
            self.accion = nueva_accion
            self.indice_frame = 0
            self.actualizar_tiempo = pygame.time.get_ticks()
        
    def dibujar(self,superficie):
        img = pygame.transform.flip(self.imagen,self.girar,False)
        #pygame.draw.rect(superficie,(250,0,0),self.rect)
        superficie.blit(img,(self.rect.x-175,self.rect.y-130))
        