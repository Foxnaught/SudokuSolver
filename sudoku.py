import copy
import time

#For a given 2d sudoku grid and a position
#Find the 3x3 box that the position falls into
#and return the values that can possibly be placed there based on the box rule
#The box rule means that in none of the 9 3x3 boxes can there be more than one value 1-9
def getBoxOptions(grid, pos):
	ops = list(range(1, 10))
	
	#Get the top left corner of the box we are checking
	xBox = pos[0] - pos[0] % 3
	yBox = pos[1] - pos[1] % 3
	
	for y in range(3):
		for x in range(3):
			ops = [i for i in ops if i != grid[yBox+y][xBox+x]]
	
	return ops

#For a given grid and position
#return the possible values that can be placed at the position
#based on row rules (no more than 1 value 1-9 in a given row or column)
def getRowOptions(grid, pos):
	ops = list(range(1, 10))
	
	for i in range(9):
		valHorz = grid[pos[1]][i]
		valVert = grid[i][pos[0]]
		
		ops = [x for x in ops if (x != valHorz and x != valVert)]

	return ops

#Check if there are any remaining 0's on the board
#If there are none then the grid is solved
def isDone(grid):
	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0:
				return False
	
	return True

#Try to fill out the grid based on sudoku rules
#If the grid cannot be solved then simply select the box with the fewest options
#and make a temporary grid with one of them and send it to this function again
#If the function returns false then the current grid cannot be solved
#If the function returns a grid then it is at least one solution to the given grid
def recurse(grid):
	lessPos = (0, 0)
	lessOps = []
	lessLen = 0
	for y in range(9):
		for x in range(9):
			if grid[y][x] not in list(range(1, 10)):
				rowOps = getRowOptions(grid, (x,y))
				boxOps = getBoxOptions(grid, (x,y))

				totalOps = [i for i in rowOps if i in boxOps]
				tLen = len(totalOps)
				
				#We found a space with no options, this grid is invalid, return false
				if tLen == 0:
					return False
				
				if lessOps == [] or tLen < lessLen or tLen == lessLen:
					lessOps = totalOps
					lessPos = (x, y)
					lessLen = tLen
	
	if lessLen == 0 and isDone(grid):
		return grid
	
	for op in lessOps:
		tempGrid = copy.deepcopy(grid)
		tempGrid[lessPos[1]][lessPos[0]] = op
		
		solution = recurse(tempGrid)
		
		if solution:
			return solution
	
	return False


grid = []
f = open("sudoku.txt", "r")
line = f.readline()
while(line != ""):
	sLine = [int(x) for x in line.split(" ")]
	for s in range(len(sLine)):
		if sLine[s] == 0:
			sLine[s] = list(range(1, 10))
	
	grid.append(sLine)
	line = f.readline()

pGrid = []
for i in range(9):
	pGrid.append([list(range(1, 10))]*9)

start = time.time()
solved = recurse(grid)
print("Runtime: " + str(time.time() - start))

if solved:
	for line in solved:
		print(line)
else:
	print("There is no valid solution")



















