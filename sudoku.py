import numpy as np
from datetime import datetime

startTime = datetime.now()


grid = []
with open('grid.txt', 'r') as f:
    for line in f:
        strippedLine = line.strip()
        noSpaces = strippedLine.replace(" ",",")
        listOfLists = noSpaces.split(',')
        sudoku = list(map(int,listOfLists))
        grid.append(sudoku)



def possible(y,x,n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    a = datetime.now() - startTime
    print(f"Completed in {a} seconds.")
    input("More?")

solve()
