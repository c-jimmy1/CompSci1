"""
Part 1 of our program asks us to mimic a hill-climing search. We will take a list of lists that holds heights.
Our goals for part 1 is to find neighbors given a start locations, be able to print the grid, and also see if a path is valid.
Author: Jimmy Chen
Version: 1
"""

import hw5_util

def get_nbrs(row, col, grid):
    """Returns a list of neighboring coordinates (row, col) in the grid."""
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Above
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col < len(grid[row]) - 1:
        neighbors.append((row, col + 1))  # Right
    if row < len(grid) - 1:
        neighbors.append((row + 1, col))  # Below
    return neighbors


def grid_input_loop():
    """Prompts the user to input a grid number until a valid grid number is entered."""
    while True:
        n = input('Enter a grid index less than or equal to 3 (0 to end): ').strip()
        print(n)
        n = int(n)
        if n <= hw5_util.num_grids() and n >= 0:
            return n


def print_grid(grid_num, response, grid):
    """Prints the grid if the user indicates Y or y"""
    if response.upper() == 'Y':
        print('Grid {}'.format(grid_num))
        for row in grid:
            print(" ".join("{:4d}".format(num) for num in row))


def print_neighbors(start_locations, grid):
    """Prints the neighbors of each start location."""
    for location in start_locations:
        row, col = location
        neighbors = get_nbrs(row, col, grid)
        printpt = 'Neighbors of ' + str(location) + ': ' + ' '.join(map(str, neighbors))
        print(printpt)
    
if __name__ == "__main__":
    # Get the grid number from the user
    grid_num = grid_input_loop()
    
    # Get the grid using the grid number chosen by the user
    grid = hw5_util.get_grid(grid_num)
    
    # Print the grid if the user indicates Y or y
    response = input('Should the grid be printed (Y or N): ').strip()
    print(response)
    print_grid(grid_num, response, grid)
    
    # Print the number of rows and columns in the grid
    print('Grid has {} rows and {} columns'.format(len(grid), len(grid[0])))
    
    # Get the start locations associated with the grid number and print neighbors for each start location
    start_locations = hw5_util.get_start_locations(grid_num)
    print_neighbors(start_locations, grid)
    
    