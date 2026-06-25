import pygame
import sys

pygame.init()

#Definir Colores
BLUE = ( 0, 0, 255)
GREEN = ( 0, 255, 0)

#Definir tamaño de la ventana principal
size = (1000, 800)

#Crear ventana principal
screen = pygame.display.set_mode(size)
python.display.set_caption("Menú de Inicio")



Juego = True
while Juego:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
           Juego = False

    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN, (175, 25, 600, 200), 0)
    

    
    pygame.display.flip()

#Cerrar ventana principal
pygame.quit()
sys.exit()
