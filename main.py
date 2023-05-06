import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))

pygame.display.set_caption('Snake game')

white = (255, 255, 255)
black = (0, 0, 0)
red=(255,0,0)

game_over=False

x1 = 300
y1 = 300

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis, black, [200, 150, 10, 10])
 
pygame.quit()
quit()
