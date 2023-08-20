#! /usr/bin/env python
import os, random, sys, math
import pygame as pg # Abrevia el modulo de pygame a pg (ej: pg.init())
from pygame.locals import *

from configuracion import *
from funciones import *
from extras import *
import botones
import math

# Funciones
def menu():

    # Inicializa el juego
    pg.init()
    clock = pg.time.Clock()
    FPS = 60
    
    # Musica del menu
    pg.mixer.init()
    pg.mixer.music.load('musica_menu.ogg')
    pg.mixer.music.play(-1)


    # Preparacion de la pantalla
    screen = pg.display.set_mode((ANCHO, ALTO))
    pg.display.set_caption('Menu')

    # Cargar la imagen de los botones
    cargar_titulo = pg.image.load('bg_titulo.png').convert_alpha()
    cargar_jugar = pg.image.load('btn_jugar.png').convert_alpha()
    cargar_salir = pg.image.load('btn_salir.png').convert_alpha()

    # Crea los botones:
    titulo = botones.Button(110, 0, cargar_titulo, 0.65)
    jugar = botones.Button(270, 180, cargar_jugar, 0.9)
    salir = botones.Button(270, 400, cargar_salir, 0.9)

    # Variables para el fondo animado
    fondo = pg.image.load("bg_menu.png").convert()
    fondo_ancho = fondo.get_width()
    scroll = 0
    tiles = math.ceil(ANCHO / fondo_ancho) + 1

    # Loop principal
    run = True
    while run:
        
        clock.tick(FPS)
        
        # Fondo en movimiento
        for i in range(0, tiles):
            screen.blit(fondo, (i * fondo_ancho + scroll, 0))

        # Velocidad del fondo
        scroll -= 1
        
        # Reset del fondo en movimiento
        if abs(scroll) > fondo_ancho:
            scroll = 0

        
        # Botones en pantalla
        titulo.draw(screen)
        if jugar.draw(screen):
            # Acción a realizar al hacer clic en el botón
            run = False
        if salir.draw(screen):
            pg.quit()
        
        # Control de eventos
        for event in pg.event.get():
            # Salir del Juego
            if event.type == pg.QUIT:
                pg.quit()

        pg.display.update()

    pg.quit()

def juego():
    #Centrar la ventana y despues inicializar pg
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pg.init()
    
    # Musica de fondo
    pg.mixer.init()
    pg.mixer.music.load('musica_juego.ogg')
    pg.mixer.music.play(-1)

    # Preparar la ventana
    pg.display.set_caption("Armar palabras con...")
    screen = pg.display.set_mode((ANCHO, ALTO))


    # Variables para el fondo animado
    clock = pg.time.Clock()
    FPS = 60
    bg_game = pg.image.load("bg_game.png").convert()
    bg_ancho = bg_game.get_width()
    scroll = 0
    tiles = math.ceil(ANCHO / bg_ancho) + 1

    # Tiempo total del juego
    gameClock = pg.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    # Variables del juego
    candidata = ""
    diccionario = []
    palabrasAcertadas = []
    puntos = 0

    #lee el diccionario
    lectura(diccionario)

    #elige las 7 letras al azar y una de ellas como principal
    letrasEnPantalla = dame7Letras()
    letraPrincipal = dameLetra(letrasEnPantalla)

    #se queda con 7 letras que permitan armar muchas palabras, evita que el juego sea aburrido
    while(len(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))< MINIMO):
        letrasEnPantalla = dame7Letras()
        letraPrincipal = dameLetra(letrasEnPantalla)

    #el siguiente print sirve para testear el juego y jugarlo más fácil
    print(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))

    #dibuja la pantalla la primera vez
    dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)

    segundos = True
    while segundos > fps/1000:
        
        # Fotograma del fondo
        clock.tick(FPS)
        
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()
        if True:
            fps = 60

        # Fondo en movimiento
        for i in range(0, tiles):
            screen.blit(bg_game, (i * bg_ancho + scroll, 0))

        # Velocidad del fondo
        scroll -= 2.5
        
        # Reset del fondo en movimiento
        if abs(scroll) > bg_ancho:
            scroll = 0

        #Buscar la tecla apretada del modulo de eventos de pg
        for e in pg.event.get():

            #QUIT es apretar la X en la ventana
            if e.type == pg.QUIT:
                pg.quit()
                return()
            #Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                candidata += letra   #va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    candidata = candidata[0:len(candidata)-1] #borra la ultima
                if e.key == K_RETURN:  #presionó enter
                    puntos += procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario, palabrasAcertadas)
                    candidata = ""
                
        segundos = TIEMPO_MAX - pg.time.get_ticks()/1000

        #Dibujar de nuevo todo
        dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)

        pg.display.update()
    
    # Llama la pantalla de cierre
    cierre(palabrasAcertadas, puntos)

def cierre(lista, puntos):
    # Variables para el cierre
    lista_ordenada = []
    diccionario = []
    
    # Lectura del diccionario
    lectura(diccionario)

    # Ordena las palabras en listaOrdenada
    for elemento in diccionario:
        if elemento in lista:
            lista_ordenada.append(elemento)

    # Inicializa la pantalla
    pg.init()

    # Preparacion de la pantalla
    screen = pg.display.set_mode((ANCHO, ALTO))
    pg.display.set_caption('Cierre')

    # Cartel Palabras acertadas
    cargar_titulo = pg.image.load('bg_titulo.png').convert_alpha()
    cargar_subtitulo = pg.image.load('bg_subtitulo.png').convert_alpha()
    cargar_salir = pg.image.load('btn_salir_puntaje.png').convert_alpha()


    # Al apretar algun boton:
    titulo = botones.Button(85, 0, cargar_titulo, 0.7)
    subtitulo = botones.Button(280, 180, cargar_subtitulo, 0.4)
    salir = botones.Button(595, 565, cargar_salir, 0.5)


    # Variables para el fondo animado
    fondo = pg.image.load("bg_menu.png").convert()
    fondo_ancho = fondo.get_width()
    clock = pg.time.Clock()
    FPS = 60
    scroll = 0
    tiles = math.ceil(ANCHO / fondo_ancho) + 1

    fuente_letras = pg.font.Font('fuente_letras.ttf', 35)
    fuente_puntaje = pg.font.Font('fuente_letras.ttf', 45)

    # Renderiza los puntos para mostrarlos en pantalla
    ren = fuente_puntaje.render("PUNTAJE: " + str(puntos), 1, (154, 219, 194))

    # Ciclo Principal

    run = True
    while run:

        clock.tick(FPS)

        for i in range(0, tiles):
            screen.blit(fondo, (i * fondo_ancho + scroll, 0))
        
        # Fondo en movimiento
        scroll -= 1
        
        # Reset del fondo en movimiento
        if abs(scroll) > fondo_ancho:
            scroll = 0

        titulo.draw(screen)

        if salir.draw(screen):
            pg.quit()

        x = 270
        y = 125
        pg.draw.rect(screen, (28,61,78), pg.Rect(x - 80, 225, 650, 320), border_radius = 15)
        
        # Subtitulo palabras armadas 
        subtitulo.draw(screen)
        
        for i in range(len(lista_ordenada)):
            screen.blit(fuente_letras.render(lista_ordenada[i], 3, (140, 219, 194)), (x, y + 130))
            y += 40
            if y >= 400:
                x += 150
                y = 125

        #Cartel Puntaje
        pg.draw.rect(screen, (28,61,78), pg.Rect(195, 580, 290, 70), border_radius = 15)
        screen.blit(ren, (230, 595))
        pg.draw.rect(screen, (28,61,78), pg.Rect(206, 540, 7, 50), border_radius = 5)
        pg.draw.rect(screen, (28,61,78), pg.Rect(470, 540, 7, 50), border_radius = 5)

        #Cartel Boton
        pg.draw.rect(screen, (28,61,78), pg.Rect(630, 540, 7, 41), border_radius = 5)
        pg.draw.rect(screen, (28,61,78), pg.Rect(820, 540, 7, 41), border_radius = 5)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
    
        pg.display.update()

    pg.quit()

# Programa principal
if __name__ == "__main__":
    menu()
    juego()
