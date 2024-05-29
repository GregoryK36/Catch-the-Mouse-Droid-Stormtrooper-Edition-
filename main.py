import pygame
import random
pygame.init()
pygame.font.init()
# set up variables for the display
size = (700, 700)
screen = pygame.display.set_mode(size)
from grandadmiralthrawn import Thrawn
from chopper import Chopper
from mousedroid import Max
bg = pygame.image.load("background.png")
b = Thrawn(500, 500)
c = Chopper(500, 500)
m = Max(600, 600)
run = True
while run:
  keys = pygame.key.get_pressed()  # checking pressed keys
  if keys[pygame.K_d]:
      b.move_direction("right")
      #c.move_direction("right")
      #m.move_direction("right")
  if keys[pygame.K_a]:
      b.move_direction("left")
      c.move_direction("left")
      m.move_direction("left")
  if keys[pygame.K_s]:
      b.move_direction("up")
      c.move_direction("up")
      m.move_direction("up")

  if keys[pygame.K_d]:
    b.move_direction("down")
    c.move_direction('down')
    m.move_direction("down")

  for event in pygame.event.get():  # User did something
    if event.type == pygame.QUIT:  # If user clicked close
        run = False
  else:
        screen.blit(b.image, b.rect)
        screen.blit(c.image, c.rect)
        screen.blit(m.image, m.rect)
        screen.blit(bg, (0, 0))
        pygame.display.update()











