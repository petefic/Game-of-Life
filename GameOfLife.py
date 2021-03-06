import pygame, sys
from pygame.locals import *
from random import randint
import numpy
from copy import copy, deepcopy

#get settings from user
fps = int(raw_input("Generations per second: "))
screenx = int(raw_input("Screen width: "))
screeny = int(raw_input("Screen height: "))
cellsize = int(raw_input("Cell size: "))
seedamt = int(raw_input("Seed amount: "))

#inititalize
pygame.init()
clock = pygame.time.Clock()

#constants
BLACK = (0,0,0)
RED = (255,0,0)
GREY = (30,30,30)
HEIGHT = screeny/cellsize
WIDTH = screenx/cellsize

#set up window
window = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption('Game of Life')
window.fill(BLACK)

#generate random seed
cells = numpy.zeros((WIDTH,HEIGHT), dtype=numpy.int)
for x in range(0,WIDTH):
	for y in range(0,HEIGHT):
		if randint(0,seedamt) == 0:
	    		cells[x][y] = 1

def findNeighbors(grid, x, y):
    if 0 < x < len(grid) - 1:
        xi = (0, -1, 1)
    elif x > 0:
        xi = (0, -1)
    else:
        xi = (0, 1)

    if 0 < y < len(grid[0]) - 1:
        yi = (0, -1, 1)
    elif y > 0:
        yi = (0, -1)
    else:
        yi = (0, 1)

    for a in xi:
        for b in yi:
            if a == b == 0:
                continue
            yield grid[x + a][y + b]

def update(grid, x, y):
	#determine num of living neighbors
	neighbors = findNeighbors(cells,x,y)
	alive = 0
	for i in neighbors:
		if i == 1:
			alive+=1
	
	#if current cell is alive
	if grid[x][y] == 1:
		#kill if less than 2 or more than 3 alive neighbors
		if (alive < 2) or (alive > 3):
			return 0
		else:
			return 1
	#if current cell is dead
	elif grid[x][y] == 0:
		#make alive if 3 alive neighbors
		if alive == 3:
			return 1
		else:
			return 0

#main loop
while True:

	#check if user wants to exit
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        pygame.quit()
	        sys.exit()

	#update cells
	new = numpy.zeros((WIDTH,HEIGHT), dtype=numpy.int)
	for x in range(0,WIDTH):
		for y in range(0,HEIGHT):
			new[x][y] = update(cells,x,y)
	cells = deepcopy(new)
			
	#draw grid
	for x in range(0,screenx,cellsize):
		for y in range(0,screeny,cellsize):
			#if cell is alive
			if cells[x/cellsize][y/cellsize] == 1:
				#draw red square
				pygame.draw.rect(window, RED, [x, y, cellsize, cellsize])
			else:
				#draw black square
				pygame.draw.rect(window, BLACK, [x, y, cellsize, cellsize])
			#draw square border
			pygame.draw.rect(window, GREY, [x, y, cellsize, cellsize], 1)

	#draw updates
	pygame.display.update()

	#generations per second
	clock.tick(fps)