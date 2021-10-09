from copy import deepcopy
from curses import wrapper
from random import choice
import time


def next_state(grid, row, col):
    height = len(grid)
    width = len(grid[0]) - 1
    indices = [((row-1) % height, (col-1) % width), ((row-1) % height, col), ((row-1) % height, (col+1) % width),
               (row, (col-1) % width), (row, (col+1) % width), ((row+1) % height, (col-1) % width),
               ((row+1) % height, col), ((row+1) % height, (col+1) % width)]
    
    neighbors = sum(int(grid[r][c] == '*') for r, c in indices)
    next_state = ' '

    if grid[row][col] == '*' and neighbors in [2, 3]:
        next_state = '*'
    elif grid[row][col] == ' ' and neighbors == 3:
        next_state = '*'
    
    return next_state


def next_gen(grid):
    next_grid = deepcopy(grid)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            next_grid[r][c] = next_state(grid, r, c)
    
    return next_grid


def draw_grid(stdscr, grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            stdscr.addch(r, c, grid[r][c])

    stdscr.refresh()


def main(stdscr):
    height, width = stdscr.getmaxyx()
    population = [[choice([' ', '*']) for _ in range(width-1)] for _ in range(height)]

    draw_grid(stdscr, population)
    while True:
        population = next_gen(population)
        draw_grid(stdscr, population)
        time.sleep(0.5)
        
    stdscr.getkey()


wrapper(main)

