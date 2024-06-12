import pygame
import random
from grandadmiralthrawn import Thrawn
from chopper import Chopper
from mousedroid import Max
import time
import os.path


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Catch the Mouse Droid!")
current_time = round(time.time(),2)
high_score = 0

file_name = "highscore.py"
if os.path.isfile(file_name) == True:
  f = open(file_name, "r")
  data = f.readline().strip()
  f.close()
  if data != "":
    high_score = int(data)






# set up variables for the display
SCREEN_HEIGHT = 800
SCREEN_WIDTH =  600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("background.png")




















name = "Try to catch the mouse droid (Use Chopper or Thrawn)!"
message = "Collision not detected"
user_game_over_one = "Game over, you have won!"
title_screen = "Welcome to the game! USE WASD arrows for movement!"
loss_over = "Game Over!"

#backgound_music = pygame.mixer_music.load("music.mp3")
#pygame.mixer.music.play(-1)



b = Thrawn(707,200)
c = Chopper(500, 200)
m = Max(600, 200)

score = 0
end_game = False
loss_game = False
start_game_one = False
welcome_message =  "Press the screen to play!"
start_game = my_font.render(welcome_message, True, (255, 255, 255))




# render the text for later

display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
click_display = my_font.render("Score: " + str(score), True, (255, 255, 255))
game_display = my_font.render(user_game_over_one, True, (255, 255, 255))
title_display = my_font.render(title_screen, True, (255, 255, 255))
display_loss = my_font.render(loss_over, True, (255, 255, 255))
high_score_message = "Your high score is " + str(high_score)
high_score_display_message = my_font.render(high_score_message, True, (255, 255, 255))
screen.fill((50, 0, 100))
screen.blit(high_score_display_message, (0, 0))



time.sleep(3)














run = True

game = True
game_one = False
backgound_music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
while game:
    screen.fill((50, 0, 0))
    screen.blit(start_game, (0, 15))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False
          game = False
      elif event.type == pygame.MOUSEBUTTONUP:
              game = False
              game_one = True
              run = True







# -------- Main Program Loop -----------
while run == True:

  time_elapsed = (round(time.time(), 1))
  time_grande = round(time_elapsed - current_time, 1)
  time_finale = "Time elapsed:" + str(10 - time_grande)
  time_final = my_font.render((str(time_finale)), True, (255, 255, 255))
  if (10 - time_grande) == 0:
      loss_game = True
      display_loss = my_font.render(loss_over, True, (255, 255, 255))
  keys = pygame.key.get_pressed()  # checking pressed keys
  if keys[pygame.K_d]:
      b.move_direction("right")
  if keys[pygame.K_a]:
      b.move_direction("left")
  if keys[pygame.K_w]:
      b.move_direction("up")
  if keys[pygame.K_s]:
      b.move_direction("down")
  if keys[pygame.K_DOWN]:
      c.move_direction("down")
  if keys[pygame.K_UP]:
      c.move_direction("up")
  if keys[pygame.K_LEFT]:
      c.move_direction("left")
  if keys[pygame.K_RIGHT]:
    c.move_direction("right")
  # collision
  if c.rect.colliderect(m.rect) or b.rect.colliderect(m.rect):
    message = "Collision detected"
    display_message = my_font.render(message, True, (255, 255, 255))
    m.set_location(random.randint(0,500), random.randint(0,280))


    score = score + 10
    click_display = my_font.render("Score: " + str(score), True, (255, 255, 255))
    print(score)
































#  else:
 #     message = "Collision not detected"
  #    display_message = my_font.render(message, True, (255, 255, 255))
















  # --- Main event loop
  for event in pygame.event.get():  # User did something
      if event.type == pygame.QUIT:  # If user clicked close
          run = False


  else:
    screen.blit(bg, (0, 0))
    screen.blit(display_name, (0, 0))
    screen.blit(display_message, (0, 15))
    screen.blit(click_display, (270, 15))
    screen.blit(time_final, (10, 270))
    screen.blit(m.image, m.rect)
    screen.blit(c.image, c.rect)
    screen.blit(b.image, b.rect)



    if end_game == True:
        screen.fill((50, 0, 0))
        screen.blit(game_display, (270, 15))
        screen.blit(click_display, (10, 20))


    if loss_game == True:
        screen.fill((50, 0, 0))
        screen.blit(display_loss, (270, 15))



  pygame.display.update()

print(str(score))
if score > high_score:
  f = open(file_name, "w")
  f.write(str(score))
  f.close()
















# Once we have exited the main program loop we can stop the game engine:
pygame.quit()