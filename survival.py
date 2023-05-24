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

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        survival()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                # player 1
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

                 #player2   
                if event.key == pygame.K_a:
                    x2_change = -snake_block
                    y2_change = 0
                elif event.key == pygame.K_d:
                    x2_change = snake_block
                    y2_change = 0
                elif event.key == pygame.K_w:
                    x2_change = 0
                    y2_change = -snake_block
                elif event.key == pygame.K_s:
                    y2_change = snake_block
                    x2_change = 0

                    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

        x2 += x2_change
        y2 += y2_change

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_Head_1 = []
        snake_Head_2 = []

        snake_Head_1.append(x1)
        snake_Head_1.append(y1)

        snake_Head_2.append(x2)
        snake_Head_2.append(y2)

        snake_List_1.append(snake_Head_1)
        snake_List_2.append(snake_Head_2)
        
        if len(snake_List_1) > Length_of_snake_1:
            del snake_List_1[0]

        if len(snake_List_2) > Length_of_snake_2:
             del snake_List_2[0]

        for x in snake_List_1[:-1]:
            if x == snake_Head_1:
                game_close = True

        for x in snake_List_2[:-1]:
            if x == snake_Head_2:
                game_close = True

        our_snake(snake_block, snake_List_1, black)
        our_snake(snake_block, snake_List_2, red)

        Your_score(Length_of_snake_1 - 1, 1)
        Your_score(Length_of_snake_2 - 1, 2)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake_1 += 1

        if x2 == foodx and y2 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake_2 += 1
            

        clock.tick(snake_speed)

    pygame.quit()
    quit()
