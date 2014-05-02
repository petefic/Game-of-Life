import pygame, sys
from pygame.locals import *
from random import randint

#inititalize
pygame.init()
clock = pygame.time.Clock()

#define constants
BLACK = (0,0,0)
RED = (255,0,0)
GREY = (30,30,30)
SCREENX = 1280
SCREENY = 720
CELLSIZE = 10
NUMOFCELLS = (SCREENX/CELLSIZE) * (SCREENY/CELLSIZE)
CELLS = []

#set up window
window = pygame.display.set_mode((SCREENX, SCREENY))
pygame.display.set_caption('Game of Life')
window.fill(BLACK)

#generate random seed
for i in range(NUMOFCELLS):
    r = randint(0,6)
    if r == 0:
        CELLS.append(1)
    else:
        CELLS.append(0)

#draw grid to screen
def drawGrid(SCREENX, SCREENY, CELLSIZE, CELLS):
	currentCell=0
	for x in range(0,SCREENX,CELLSIZE):
		for y in range(0,SCREENY,CELLSIZE):
			if CELLS[currentCell] == 1:
				#alive cell
				pygame.draw.rect(window, RED, [x, y, CELLSIZE, CELLSIZE])
			else:
				#dead cell, just draw grid border
				pygame.draw.rect(window, GREY, [x, y, CELLSIZE, CELLSIZE], 1)
			currentCell+=1

#main loop
done = False
while not done:
	#generations per second
	clock.tick(10)

	for event in pygame.event.get():
		#check if user wants to exit
	    if event.type == pygame.QUIT:
	        done=True

	drawGrid(SCREENX, SCREENY, CELLSIZE, CELLS)

	#draw updates
	pygame.display.flip()

pygame.quit()


