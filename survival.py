from variables import *

def survival():
    game_over = False
    game_close = False

    x1 = (dis_width / 8) * 2
    y1 = dis_height / 2

    x2 = (dis_width / 8) * 6
    y2 = dis_height / 2

    x1_change = 0
    y1_change = 0

    x2_change = 0
    y2_change = 0

    snake_List_1 = []
    snake_List_2 = []

    Length_of_snake_1 = 1
    Length_of_snake_2 = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0