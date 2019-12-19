import pygame, time, random, sys
from pygame.locals import *
counter = 0 

def Setup():
  pygame.init

#Init
screen = pygame.display.set_mode([500,500])
aura = pygame.image.load('aurora.png')
icek = pygame.image.load('icetile.png')

pyro = pygame.image.load('fire/fire0.png')
flames = [
  pygame.image.load('fire/fire0.png'),
  pygame.image.load('fire/fire1.png')]
fire_frame = 0
pyro = flames[fire_frame]


fork = pygame.image.load('tonist/tonist0.png')
tonist_anim = [
pygame.image.load('tonist/tonist0.png'), 
pygame.image.load('tonist/tonist1.png'), 
pygame.image.load('tonist/tonist2.png'), 
pygame.image.load('tonist/tonist3.png')
]
tonist_frame = 0
tonist = tonist_anim[ tonist_frame ]

pygame.display.set_caption("Infinite Glacier")
clock = pygame.time.Clock()

#Define Colors
blue = [44,58,119]
black = [ 0, 0, 0]
white = [255,255,255]


def Ground():
  global tonist, tonist_frame, tonist_anim
  global pyro, fire_frame, flames

  tonist_frame = (tonist_frame + 1) % len(tonist_anim)
  tonist = tonist_anim[ tonist_frame ]

  fire_frame = (fire_frame + 1) % len(flames)
  pyro = flames[fire_frame]

  screen.blit(tonist, (220, 280))
  screen.blit(pyro, (280, 340))


  #Actual Ground
  for i in range(7):
    screen.blit(icek, (500-(i*96), 404))
  
snow_pos = []

for i in range(50):
    x = random.randrange(0, 500)
    y = random.randrange(0, 500)
    snow_pos.append([x, y])


def Snow():
  for i in range(len(snow_pos)):
    pygame.draw.circle(screen, white, snow_pos[i], 2)
    snow_pos[i][1] += 1
    if snow_pos[i][1] > 500:
          y = random.randrange(-50, -10)
          snow_pos[i][1] = y
          x = random.randrange(0, 500)
          snow_pos[i][0] = x


Setup()
#Main
def Main():
  screen.fill(blue)
  screen.blit(aura, (0, 0))
  Snow()
  Ground()
  pygame.display.flip()
  clock.tick(20)

while True:
  Main()