from principal import *
from configuracion import *
import random
import math
import pygame
# Inicializa Pygame y sus módulos
pygame.init()

# Inicializa el módulo de mezcla de Pygame
pygame.mixer.init()

#lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario):
    file = open("lemario.txt", "r")
    lista = file.readlines()
    file.close()

    for palabra in lista:
      diccionario.append(palabra.strip())

    return diccionario

#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)
def dame7Letras():
  vocales = ["a", "e", "i", "o", "u"]
  consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w']
  dificiles = ["k", "x", "y", "z"]

  letras = random.sample(vocales, 3) + random.sample(consonantes, 3) + random.sample(dificiles, 1)

  random.shuffle(letras)

  return ''.join(letras)

def dameLetra(letrasEnPantalla): #elige una letra de las letras en pantalla
  letra = random.choice(letrasEnPantalla)
  return letra

#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario, palabrasAcertadas):
     if esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario, palabrasAcertadas):
        # Aquí puedes agregar el código para reproducir el sonido
        pygame.mixer.Sound('musica_correcta.wav').play()
        return Puntos(candidata)
     else:
        # Aquí puedes agregar el código para reproducir el sonido de palabra incorrecta
        pygame.mixer.Sound('musica_incorrecta.ogg').play()
        return (-1)

#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario

#[MODIFICACION PARA PUNTO EXTRA SIN REPETIDOS]
#Para evitar que el usuario ingrese una palabra ya utilizada agrego una lista para     llevar un registro de las palabras ingresadas por el usuario. Luego modifico la función esValida para verificar si la palabra candidata ya ha sido ingresada antes

def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario, palabrasAcertadas):
  for letra in candidata:
    if letra not in letrasEnPantalla:
      return False

  if letraPrincipal not in candidata:
    return False

  if candidata not in diccionario:
    return False

  if candidata in palabrasAcertadas:
    return False

  palabrasAcertadas.append(candidata)
  return True

#devuelve los puntos
def Puntos(candidata):
  longitud = len(candidata)

  if longitud == 7:
    return (10)
  elif longitud >= 5:
    return (longitud)
  elif longitud == 4:
    return (2)
  else:
    return (1)

#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
  lista = []

  for palabra in diccionario:
    contador = 0
    for letra in palabra:
      if letra in letrasEnPantalla and letraPrincipal in palabra:
        contador += 1

    if contador == len(palabra):
      lista.append(palabra)

  return lista
