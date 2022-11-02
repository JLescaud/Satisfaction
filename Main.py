import pygame as py
from GameObject import GameObject
from pygame.time import Clock


py.init()
screen = py.display.set_mode((800, 800))
clock = Clock()
square = GameObject(1, 3)

# from https://www.flaticon.com/fr/icones-gratuites/art-deco
icon =py.image.load("icon.png")
py.display.set_icon(icon)  
py.display.set_caption("Satisfaction")


running = True
while running:
    screen.fill((255, 255, 255))
    py.draw.rect(screen, square.color, (square.pos[0], square.pos[1], 50 ,50))
    
    
    square.move()

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    py.display.update()
    clock.tick(60)
py.quit()
