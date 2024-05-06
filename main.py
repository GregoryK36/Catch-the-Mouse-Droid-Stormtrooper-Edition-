import pygame
import random
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Balloon Flight!")
# set up variables for the display
size = (1000, 1000)
screen = pygame.display.set_mode(size)
from grandadmiralthrawn import Thrawn
b = Thrawn(500, 500)
run = True
while run:
     keys = pygame.key.get_pressed()  # checking pressed keys
     if keys[pygame.K_SPACE]:
        b.move_balloon("up")
     else:
         b.move_balloon("down")
     for event in pygame.event.get():  # User did something
         if event.type == pygame.QUIT:  # If user clicked close
             run = False
     screen.blit(b.image, b.rect)
     pygame.display.update()








