"""
Part 2 of our program asks us to mimic a hill-climing search. It finds and outputs the location and height of the
global maximum. For each start location, it then computes and outputs two paths the steepest and the most gradual upward path.
Finally, if requested, it prints a grid showing for each cell how many paths include that cell.

Author: Jimmy Chen
Version: 1
"""

import hw5_util

def get_nbrs(row, col, grid):
    """Returns a list of neighboring coordinates in the grid"""
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


def find_global_max(grid):
    """Finds the global maximum height in the grid.
       Returns a tuple position, value where position is the row, col."""
    max_val = grid[0][0]
    max_pos = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > max_val:
                max_val = grid[i][j]
                max_pos = (i, j)
    return max_pos, max_val


def path_finder(grid, start, max_step, path_type):
    """
    Computes a path from start on grid. It only moves to an adjacent neighbor and only moves upward, while the upward 
    step difference is no more than max_step. Ties are broken by the order returned by get_nbrs.
    THe path_types are steepest or gradual
    """
    path = [start]
    current = start

    while True:
        current_val = grid[current[0]][current[1]]
        nbrs = get_nbrs(current[0], current[1], grid)
        valid_moves = [
            (nbr, grid[nbr[0]][nbr[1]] - current_val)
            for nbr in nbrs
            if 0 < grid[nbr[0]][nbr[1]] - current_val <= max_step
        ]
        if not valid_moves:
            break

        if path_type == "steepest":
            target_diff = max(diff for _, diff in valid_moves)
        elif path_type == "gradual":
            target_diff = min(diff for _, diff in valid_moves)
        else:
            break

        # Choose the first neighbor in the orgi order that meets the target diff
        for nbr, diff in valid_moves:
            if diff == target_diff:
                chosen = nbr
                break

        path.append(chosen)
        current = chosen

    return path


def classify_path(path, grid, global_max_pos):
    """
    Determines whether the path reaches the global maximum, a local maximum, or neither
    """
    final = path[-1]
    if final == global_max_pos:
        return "global maximum"
    
    final_val = grid[final[0]][final[1]]
    nbrs = get_nbrs(final[0], final[1], grid)
    is_local = True
    for nbr in nbrs:
        if grid[nbr[0]][nbr[1]] > final_val:
            is_local = False
            break
    if is_local:
        return "local maximum"
    else:
        return "no maximum"


def format_path(path):
    """
    Formats the path a list of row, col tuples so that 5 locations are printed per line
    """
    result = ""
    i = 0
    while i < len(path):
        line = ""
        # 5 coordinates per line
        for j in range(i, min(i + 5, len(path))):
            line += "({0}, {1}) ".format(path[j][0], path[j][1])
        result += line + "\n"
        i += 5
    return result


def print_path_grid(path_grid_counts):
    """
    Prints the path grid counts with a fixed width for each cell. A dot is printed for cells not used.
    """
    for row in path_grid_counts:
        formatted_cells = []
        for count in row:
            if count == 0:
                formatted_cells.append("{:>2}".format('.'))
            else:
                formatted_cells.append("{:>2}".format(count))
        print(" ".join(formatted_cells))


if __name__ == "__main__":
    # Get the grid number from the user
    grid_num = grid_input_loop()
    
    # Get the grid using the grid number chosen by the user
    grid = hw5_util.get_grid(grid_num)
    
    max_step_input = input("Enter the maximum step height: ").strip()
    print(max_step_input)
    max_step = int(max_step_input)
    
    path_grid_response = input("Should the path grid be printed (Y or N): ").strip()
    print(path_grid_response)
    
    print('Grid has {} rows and {} columns'.format(len(grid), len(grid[0])))
    global_max_pos, global_max_val = find_global_max(grid)
    print("global max: {} {}".format(global_max_pos, global_max_val))
    
    start_locations = hw5_util.get_start_locations(grid_num)
    
    # Initialize a grid to count how many times each cell is used by any path
    path_grid_counts = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            row.append(0)
        path_grid_counts.append(row)
    
    # Go through each start location and find the steepest and most gradual paths
    for start in start_locations:
        steepest = path_finder(grid, start, max_step, "steepest")
        gradual = path_finder(grid, start, max_step, "gradual")
        steepest_class = classify_path(steepest, grid, global_max_pos)
        gradual_class = classify_path(gradual, grid, global_max_pos)
        
        # Update the path grid counts for all cells in both paths
        for coord in steepest:
            row_index, col_index = coord
            path_grid_counts[row_index][col_index] += 1
        for coord in gradual:
            row_index, col_index = coord
            path_grid_counts[row_index][col_index] += 1
        
        # Print the steepest and most gradual paths
        print("===")
        print("steepest path")
        print(format_path(steepest))
        # Print the classification of the path (global maximum, local maximum, or neither)
        print(steepest_class)
        
        
        print("...")
        print("most gradual path")
        print(format_path(gradual))
        # Print the classification of the path (global maximum, local maximum, or neither)
        print(gradual_class)
    
    # print the path grid if Y or y is entered
    if path_grid_response.upper() == 'Y':
        print("===")
        print("Path grid")
        print_path_grid(path_grid_counts)