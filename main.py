import random
import os
import time

HEIGHT = 20
WIDTH = 20

def create_grid(height, width):
    grid = []
    for col in range(width):
        col =[]
        for row in range(height):
            col.append(random.randint(0, 1))
        grid.append(col)
    return grid

def print_grid(grid):
    os.system('clear')
    for col in grid:
        line =""
        for row in col:
            if row == 1:
                line += "O"
            else:
                line += "."
        print(line)

def calculate_neighbours(row, col, grid):
    count = 0
    for nx in [-1, 0 ,1]:
        for ny in [-1, 0 ,1]:
            if nx == 0 and ny == 0:
                continue
            if [(0 <= (row + nx) < HEIGHT) and (0 <= (col + ny) < WIDTH)]:
                if grid[row + nx][col + ny] == 1:
                    count += 1
    return count

def update_grid(grid):
    for col in range(WIDTH):
        for row in range(HEIGHT):
            alive_neighbours = calculate_neighbours(row, col, grid)

            if alive_neighbours == 3 and grid[row][col] == 0:
                grid[row][col] = 1
            elif (alive_neighbours == 2 or alive_neighbours == 3) and grid[row][col] == 1:
                grid[row][col] = 1
            elif alive_neighbours < 2 or alive_neighbours > 3 and grid[row][col] == 1:
                grid[row][col] = 0



def main():
    grid = create_grid(HEIGHT, WIDTH)
    while True:
        print_grid(grid)
        time.sleep(1)
        update_grid(grid)

main()