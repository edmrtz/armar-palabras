import pygame as pg
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos):
    fuente_letras = pg.font.Font('fuente_letras.ttf', 35)
    fuente_teclado = pg.font.Font('fuente_letras.ttf', 55)
    fuente_letras_pantalla = pg.font.Font('fuente_titulo.ttf', 100)
    
    pg.draw.rect(screen, (28,61,78), pg.Rect(310, 630, 450, 80), border_radius = 15)
    pg.draw.rect(screen, (176, 239, 222), pg.Rect(370, 685, 330, 5))
    
    ren1 = fuente_teclado.render(candidata, 1, COLOR_TEXTO)
    ren2 = fuente_letras.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos<15):
        ren3 = fuente_letras.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = fuente_letras.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    #escribe grande la palabra (letra por letra) y la letra principal de otro color
    pos = 240
    pg.draw.rect(screen, (176, 239, 222), pg.Rect(190, 93, 680, 140), border_radius=15)
    pg.draw.rect(screen, (28,61,78), pg.Rect(180, 85, 680, 140), border_radius=15)
    for i in range(len(letrasEnPantalla)):
        if letrasEnPantalla[i] == letraPrincipal:
            screen.blit(fuente_letras_pantalla.render(letrasEnPantalla[i], 1, (45, 148, 125)), (pos, 100))
        else:
            screen.blit(fuente_letras_pantalla.render(letrasEnPantalla[i], 1, (176, 239, 222)), (pos, 100))
        pos = pos + TAMANNO_LETRA_GRANDE
    
    screen.blit(ren1, (420, 635))
    screen.blit(ren2, (850, 10))
    screen.blit(ren3, (10, 10))
