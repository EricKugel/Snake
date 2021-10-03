import pygame
from pygame.locals import *
import os
from snake import Snake

pygame.init()
FPS = 12
FramesPerSec = pygame.time.Clock()
SURFACE = pygame.display.set_mode((640,480))
SURFACE.fill(pygame.Color("white"))
pygame.display.set_caption("Snake")

snake = Snake()

while True:
    SURFACE.fill("white")
    
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            os.sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                snake.turn("left")
            elif(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                snake.turn("right")
            elif(event.key == pygame.K_UP or event.key == pygame.K_w):
                snake.turn("up")
            elif(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                snake.turn("down")
    
    snake.update()
    snake.draw(SURFACE)
    
    
    FramesPerSec.tick(FPS)
    pygame.display.update()