import pygame
import pygame_menu
from pygame_menu import themes
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Wonsz z Dusza')

game_over = False

x1 = dis_width/2
y1 = dis_height/2

snake_block = 10
snake_speed = 30

x1_change = 0       
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

#menu section
mainmenu = pygame_menu.Menu('Wonsz z Duszą', dis_width, dis_height, theme=themes.THEME_SOLARIZED)
mainmenu.add.button('Single player')
mainmenu.add.button('Survival')
mainmenu.add.button('Levels')
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(dis_width/2, dis_height/2))
    dis.blit(mesg, mesg_rect)   
   
def game_loop():
    game_over = False
    game_close = False

    foodx = round(random.randrange(0, dis_width - s))
    foody = round(random.randrange(0, dis_width - s))
    

    
while not game_over:

    while game_close == True:

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
                
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    pygame.display.update()
    
    clock.tick(snake_speed)
    
message("You lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
