import copy
import time

def getBoxOptions(grid, pos):
	ops = list(range(1, 10))
	
	#Get the top left corner of the box we are checking
	xBox = pos[0] - pos[0] % 3
	yBox = pos[1] - pos[1] % 3
	
	for y in range(3):
		for x in range(3):
			ops = [i for i in ops if i != grid[yBox+y][xBox+x]]
	
	return ops
	
def getRowOptions(grid, pos):
	ops = list(range(1, 10))
	
	for i in range(9):
		valHorz = grid[pos[1]][i]
		valVert = grid[i][pos[0]]
		
		ops = [x for x in ops if (x != valHorz and x != valVert)]

	return ops

def isDone(grid):
	for y in range(9):
		for x in range(9):
			if grid[y][x] not in list(range(1, 10)):
				return False
	
	return True


def getRel(grid, values):
	rel = 0
	for y in range(9):
		for x in range(9):
			if grid[y][x] in values:
				rel += 1
	
	return rel

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
				
				if lessOps == [] or tLen < lessLen or (tLen == lessLen and getRel(grid, totalOps) < getRel(grid, lessOps)):
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



















