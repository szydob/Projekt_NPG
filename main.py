from pygame_menu import themes
import pygame_menu
from variables import *
from singleplayer import single_player
from survival import survival

mainmenu = pygame_menu.Menu('Wonsz z Duszą', dis_width, dis_height, theme=themes.THEME_SOLARIZED)

def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)

def level_menu(level):
    mainmenu._open(level)

def main_menu():
    mainmenu.add.button('Single player', single_player)  
    mainmenu.add.button('Survival', survival)
    mainmenu.add.button('Levels', level_menu)
    mainmenu.add.button('Quit', pygame_menu.events.EXIT)

    level = pygame_menu.Menu('Select a Difficulty', dis_width, dis_height, theme=themes.THEME_BLUE)
    level.add.selector('Difficulty :', [('Hard', 1), ('Normal', 2), ('Easy', 3)], onchange=set_difficulty)

    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

    play = pygame.USEREVENT + 0
    
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == play:
                single_player()

            if event.type == survival:
                survival()

            if event.type == pygame.QUIT:
                exit()





   

   
        
            
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
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
