import pygame, sys
from pygame.locals import *
from random import randint
import numpy

#inititalize
pygame.init()
clock = pygame.time.Clock()

#constants
BLACK = (0,0,0)
RED = (255,0,0)
GREY = (30,30,30)
SCREENX = 800
SCREENY = 600
CELLSIZE = 10
HEIGHT = SCREENY/CELLSIZE
WIDTH = SCREENX/CELLSIZE


#set up window
window = pygame.display.set_mode((SCREENX, SCREENY))
pygame.display.set_caption('Game of Life')
window.fill(BLACK)

#generate random seed
cells = numpy.zeros((WIDTH,HEIGHT))
for x in range(0,WIDTH):
	for y in range(0,HEIGHT):
	    r = randint(0,15)
	    if r == 0:
	        cells[x][y] = 1

#main loop
done = False
while not done:
	
	#generations per second
	clock.tick(7)

	#check if user wants to exit
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        done=True

	#update cells
	for x in range(0,WIDTH):
		for y in range(0,HEIGHT):
			
			#get neighbors
			neighbors = []
			if x!=0 and y!=HEIGHT-1:
				neighbors.append(cells[x-1][y+1])
			if y!=HEIGHT-1:
				neighbors.append(cells[x][y+1])
			if x!=WIDTH-1 and y!=HEIGHT-1:
				neighbors.append(cells[x+1][y+1])
			if x!=0:
				neighbors.append(cells[x-1][y])
			if x!=WIDTH-1:
				neighbors.append(cells[x+1][y])
			if x!=0 and y!=0:
				neighbors.append(cells[x-1][y-1])
			if y!=0:
				neighbors.append(cells[x][y-1])
			if x!=WIDTH-1 and y!=0:
				neighbors.append(cells[x+1][y-1])

			#determine # of living neighbors
			alive = 0
			for i in neighbors:
				if i == 1:
					alive+=1

			#if current cell is dead
			if cells[x][y] == 0:
				#make alive if 3 alive neighbors
				if alive == 3:
					cells[x][y] = 1
			#if current cell is alive
			elif cells[x][y] == 1:
				#kill if less than 2 or more than 3 alive neighbors
				if (alive<2) or (alive>3):
					cells[x][y] = 0
	        
	#draw grid
	for x in range(0,SCREENX,CELLSIZE):
		for y in range(0,SCREENY,CELLSIZE):
			if cells[x/CELLSIZE][y/CELLSIZE] == 1:
				#alive cell
				pygame.draw.rect(window, RED, [x, y, CELLSIZE, CELLSIZE])
			else:
				#dead cell
				pygame.draw.rect(window, BLACK, [x, y, CELLSIZE, CELLSIZE])
			pygame.draw.rect(window, GREY, [x, y, CELLSIZE, CELLSIZE], 1)

	#draw updates
	pygame.display.flip()

pygame.quit()