import pygame
pygame.init()
dis=pygame.display.set_mode((800,600))

pygame.display.set_caption('Snake game')

white = (255, 255, 255)
black = (0, 0, 0)
red=(255,0,0)

game_over=False

x1 = 300
y1 = 300

x1_change = 0       
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
                
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    clock.tick(30)

pygame.quit()
quit()
