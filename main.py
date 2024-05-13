import pygame
import random
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Balloon Flight!")
# set up variables for the display
size = (700, 700)
screen = pygame.display.set_mode(size)
from grandadmiralthrawn import Thrawn
from chopper import Chopper
b = Thrawn(500, 500)
c = Chopper(500, 500)
run = True
while run:
  keys = pygame.key.get_pressed()  # checking pressed keys
  if keys[pygame.K_d]:
      b.move_balloon("right")
      c.move_balloon("right")
  if keys[pygame.K_a]:
      b.move_balloon("left")
      c.move_balloon("left")
  for event in pygame.event.get():  # User did something
         if event.type == pygame.QUIT:  # If user clicked close
             run = False

         else:
             screen.blit(b.image, b.rect)
             screen.blit(c.image, c.rect)
         pygame.display.update()








