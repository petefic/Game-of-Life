import pygame, sys
from pygame.locals import *

#inititalize everything
pygame.init()
clock = pygame.time.Clock()

#define colors
blk = (0,0,0)
red = (255,0,0)
white = (255,255,255)

#set up window
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game of Life')

#main loop
done = False
while not done:
	#30 fps
	clock.tick(30)

	for event in pygame.event.get():
		#check if user wants to exit
	    if event.type == pygame.QUIT:
	        done=True

	window.fill(white)

	#draw updates
	pygame.display.flip()

pygame.quit()

