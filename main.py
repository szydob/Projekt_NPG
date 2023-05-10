import pygame

pygame.init()

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

game_over = False

x1 = dis_width/2
y1 = dis_height/2

snake_block = 10

x1_change = 0       
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
                
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)

    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
