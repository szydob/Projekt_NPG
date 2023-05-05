import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))

pygame.display.set_caption('Snake game')

blue=(0,0,255)
red=(255,0,0)

game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()
quit()
