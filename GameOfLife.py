import pygame, sys
from pygame.locals import *

#inititalize everything
pygame.init()
clock = pygame.time.Clock()

#define colors
blk = (0,0,0)
red = (255,0,0)
grey = (30,30,30)

#set up window
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game of Life')
window.fill(blk)

gridsize=10
#draw grid
for x in range(0,1280,gridsize):
	for y in range(0,720,gridsize):
		pygame.draw.rect(window, grey, [x, y, gridsize, gridsize], 1)

#main loop
done = False
while not done:
	#30 fps
	clock.tick(30)

	for event in pygame.event.get():
		#check if user wants to exit
	    if event.type == pygame.QUIT:
	        done=True

	

	#draw updates
	pygame.display.flip()

pygame.quit()

