import pygame, sys
from pygame.locals import *
from random import randint
import numpy

#inititalize
pygame.init()
clock = pygame.time.Clock()

#constants
FPS = 10
BLACK = (0,0,0)
RED = (255,0,0)
GREY = (30,30,30)
SCREENX = 640
SCREENY = 480
CELLSIZE = 10
HEIGHT = SCREENY/CELLSIZE
WIDTH = SCREENX/CELLSIZE


#set up window
window = pygame.display.set_mode((SCREENX, SCREENY))
pygame.display.set_caption('Game of Life')
window.fill(BLACK)

#generate random seed
cells = numpy.zeros((WIDTH,HEIGHT), dtype=numpy.int)
for x in range(0,WIDTH):
	for y in range(0,HEIGHT):
	    cells[x][y] = randint(0,1)

def findNeighbors(grid, x, y):
    if 0 < x < len(grid) - 1:
        xi = (0, -1, 1)
    elif x > 0:
        xi = (0, -1)
    else:
        xi = (0, 1)

    yi = (0, -1, 1) if 0 < y < len(grid[0]) - 1 else ((0, -1) if y > 0 else (0, 1))
    for a in xi:
        for b in yi:
            if a == b == 0:
                continue
            yield grid[x + a][y + b]


#main loop
while True:

	#check if user wants to exit
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        pygame.quit()
	        sys.exit()

	#update cells
	for x in range(0,WIDTH):
		for y in range(0,HEIGHT):
			
			#get neighbors
			neighbors = findNeighbors(cells,x,y)

			#determine num of living neighbors
			alive = 0
			for i in neighbors:
				if i == 1:
					alive+=1

			
			#if current cell is alive
			if cells[x][y] == 1:
				#kill if less than 2 or more than 3 alive neighbors
				if alive < 2:
					cells[x][y] = 0
				elif alive > 3:
					cells[x][y] = 0
				else:
					cells[x][y] = 1
			#if current cell is dead
			elif cells[x][y] == 0:
				#make alive if 3 alive neighbors
				if alive == 3:
					cells[x][y] = 1
				else:
					cells[x][y] = 0
			
	#draw grid
	for x in range(0,SCREENX,CELLSIZE):
		for y in range(0,SCREENY,CELLSIZE):
			#if cell is alive
			if cells[x/CELLSIZE][y/CELLSIZE] == 1:
				#draw red square
				pygame.draw.rect(window, RED, [x, y, CELLSIZE, CELLSIZE])
			else:
				#draw black square
				pygame.draw.rect(window, BLACK, [x, y, CELLSIZE, CELLSIZE])
			#draw square border
			pygame.draw.rect(window, GREY, [x, y, CELLSIZE, CELLSIZE], 1)

	#draw updates
	pygame.display.update()

	#generations per second
	clock.tick(FPS)