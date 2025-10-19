import pygame
import sys
import random

pygame.init()
szelesseg = 800
magassag = 600
screen = pygame.display.set_mode((szelesseg, magassag))
pygame.display.set_caption("Solid Snake")

icon = pygame.image.load("solidsnake.png")
pygame.display.set_icon(icon)
