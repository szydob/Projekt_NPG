import pygame
import time
import random

pygame.init()

#screen variables
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Wonsz z Duszą")
icon = pygame.image.load("assets/hero.png")
pygame.display.set_icon(icon)