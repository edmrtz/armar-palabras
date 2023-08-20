import pygame as pg
pg.init()
pg.mixer.init()

#Botones
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        accion = False
        
        # Poscision del mouse
        pos = pg.mouse.get_pos()
        

        # Verifica si el mouse hace click en algun lugar
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                accion = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
    

        #Dibuja un boton en la pantalla
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return accion