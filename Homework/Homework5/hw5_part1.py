"""
Part 1 of our program asks us to mimic a hill-climing search. We will take a list of lists that holds heights.
Our goals for part 1 is to find neighbors given a start locations, be able to print the grid, and also see if a path is valid.
Author: Jimmy Chen
Version: 1
"""

import hw5_util

def get_nbrs(row, col, grid):
    """Returns a list of neighboring coordinates (row, col) in the grid"""
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
    """Prompts the user to input a grid number until a valid grid number is entered"""
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
            print("".join("{:4d}".format(num) for num in row))


def print_neighbors(start_locations, grid):
    """Prints the neighbors of each start location."""
    for location in start_locations:
        row, col = location
        neighbors = get_nbrs(row, col, grid)
        printpt = 'Neighbors of ' + str(location) + ': ' + ' '.join(map(str, neighbors))
        print(printpt)

def check_path(path, grid):
    """Validates a path on the grid by checking if the consecutive coordinates are neighbors
    Compute total downward and upward movement in the path"""
    for i in range(len(path) - 1):
        current = path[i]
        nxt = path[i+1]
        if nxt not in get_nbrs(current[0], current[1], grid):
            print('Path: invalid step from {} to {}'.format(current, nxt))
            return

    # If we got here, the path is valid
    print('Valid path')
    downward = 0
    upward = 0

    # Get the elevation value at the starting coordinate
    prev_val = grid[path[0][0]][path[0][1]]
    # Walk through the path starting at the second coordinate
    for coord in path[1:]:
        curr_val = grid[coord[0]][coord[1]]
        if curr_val < prev_val:
            downward += prev_val - curr_val
        elif curr_val > prev_val:
            upward += curr_val - prev_val
        prev_val = curr_val

    print("Downward " + str(downward))
    print("Upward " + str(upward))
            
    
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
    
    # Get the path associated with the grid number and check if the path is valid
    path = hw5_util.get_path(grid_num)
    check_path(path, grid)
    