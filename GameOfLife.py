import pygame, sys
from pygame.locals import *
from random import randint

#inititalize
pygame.init()
clock = pygame.time.Clock()

#constants
BLACK = (0,0,0)
RED = (255,0,0)
GREY = (30,30,30)
SCREENX = 1280
SCREENY = 720
CELLSIZE = 10
ROWS = SCREENX/CELLSIZE
COLS = SCREENY/CELLSIZE


#set up window
window = pygame.display.set_mode((SCREENX, SCREENY))
pygame.display.set_caption('Game of Life')
window.fill(BLACK)

#generate random seed
cells = [[None for i in range(COLS)] for i in range(ROWS)]
for x in range(0,ROWS):
	for y in range(0,COLS):
	    r = randint(0,6)
	    if r == 0:
	        cells[x][y] = 1
	    else:
	        cells[x][y] = 0

#main loop
done = False
while not done:
	
	#generations per second
	clock.tick(10)

	#check if user wants to exit
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        done=True

	#update cells
	for x in range(0,ROWS):
		for y in range(0,COLS):
			
			#get neighbors
			neighbors = []
			if x!=0 and y!=COLS-1:
				neighbors.append([x-1,y+1])
			if y!=COLS-1:
				neighbors.append([x,y+1])
			if x!=ROWS-1 and y!=COLS-1:
				neighbors.append([x+1,y+1])
			if x!=0:
				neighbors.append([x-1,y])
			if x!=ROWS-1:
				neighbors.append([x+1,y])
			if x!=0 and y!=0:
				neighbors.append([x-1,y-1])
			if y!=0:
				neighbors.append([x,y-1])
			if x!=ROWS-1 and y!=0:
				neighbors.append([x+1,y-1])

			#determine # of living neighbors
			alive = []
			for i in neighbors:
				if cells[i[0]][i[1]] == 1:
					alive.append(i)

			#if current cell is dead
			if cells[x][y] == 0:
				#make alive if 3 alive neighbors
				if len(alive) == 3:
					cells[x][y] = 1
			#if current cell is alive
			else:
				#kill if less than 2 or more than 3 alive neighbors
				if (len(alive)<2)  | (len(alive)>3):
					cells[x][y] = 0
	        
	#draw grid
	currentX=0
	for x in range(0,SCREENX,CELLSIZE):
		currentY=0
		for y in range(0,SCREENY,CELLSIZE):
			if cells[currentX][currentY] == 1:
				#alive cell
				pygame.draw.rect(window, RED, [x, y, CELLSIZE, CELLSIZE])
			else:
				#dead cell, just draw grid border
				pygame.draw.rect(window, BLACK, [x, y, CELLSIZE, CELLSIZE])
				pygame.draw.rect(window, GREY, [x, y, CELLSIZE, CELLSIZE], 1)
			currentY+=1
		currentX+=1

	#draw updates
	pygame.display.flip()

pygame.quit()