from grid import Grid

my_grid = Grid(9)

def rhombus(grid):
    """ Adds a rhombus shape into a grid object that has an odd grid size."""
    mid = grid.grid_size // 2
    placeholder = mid

    for row_num in range(grid.grid_size):
        empty_spaces = abs(placeholder)
        for i in range(grid.grid_size - 2 * empty_spaces):
            grid.set(mid + (mid - empty_spaces) - i, row_num, "O")
            
        placeholder = placeholder - 1
    
rhombus(my_grid)
my_grid.display()
    