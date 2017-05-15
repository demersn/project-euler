# Highest product of four adgacent number in the grid
# Up, Down, Left, Right, diagonally

import numpy as np


# Import the grid
with open('P_11_grid.txt') as f:
    f = [x.strip() for x in f]  # Open file

grid = np.zeros((len(f), len(f)))  # Init grid
for line in range(len(f)):  # Make into array of array
    grid[line] = f[line].split()
grid = grid.astype(int)  # Make array of integers

print(grid)
# Up and Down are the same
prod_u_max = 0
for ll in range(len(grid)-3):
    for cc in range(len(grid)):
        prod_u = grid[ll][cc]*grid[ll+1][cc]*grid[ll+2][cc]*grid[ll+3][cc]
        if prod_u > prod_u_max:
            prod_u_max = prod_u

# Left Rigt are the same
prod_lr_max = 0
for cc in range(len(grid)-3):
    for ll in range(len(grid)):
        prod_lr = grid[ll][cc]*grid[ll][cc+1]*grid[ll][cc+2]*grid[ll][cc+3]
        if prod_lr > prod_lr_max:
            prod_lr_max = prod_lr

# Diagonal
prod_d_max = 0
for ll in range(len(grid)-3):
    for cc in range(len(grid)-3):
        prod_d = grid[ll][cc]*grid[ll+1][cc+1]*grid[ll+2][cc+2]*grid[ll+3][cc+3]
        if prod_d > prod_d_max:
            prod_d_max = prod_d

# Anti-Diagonal
prod_ad_max = 0
for ll in range(3, len(grid)-3):
    for cc in range(len(grid)-3):
        prod_ad = grid[ll][cc]*grid[ll-1][cc+1]*grid[ll-2][cc+2]*grid[ll-3][cc+3]
        if prod_ad > prod_ad_max:
            prod_ad_max = prod_ad

all_max = [prod_u_max, prod_lr_max, prod_d_max, prod_ad_max]
abs_max = max(all_max)
print(all_max)
print(abs_max)
