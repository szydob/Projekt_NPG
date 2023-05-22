import pygame
import time
import random

pygame.init()

#screen variables
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Wonsz z Duszą")
# icon = pygame.image.load("assets/hero.png")
# pygame.display.set_icon(icon)

clock = pygame.time.Clock()

#font and styels variables
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

#color variables
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#varaibles responsible for snake speed and thickness
snake_block = 10
snake_speed = 15

#auxiliary functions
def Your_score(score, type):
     value = score_font.render("Score p1: " + str(score), True, yellow)
     if type == 1:
          dis.blit(value, [0, 0])
     else:
          dis.blit(value, [600, 0])


def our_snake(snake_block, snake_list, color):
     for x in snake_list:
          pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])