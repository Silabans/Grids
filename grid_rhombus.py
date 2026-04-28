class Grid:
    def __init__(self, grid_size, char:str = "."):
        self.grid_size =  grid_size
        self.grid = ["."] * grid_size**2
        
    def get(self, x, y):
        return self.grid[y * self.grid_size + x]
    
    def set(self, x, y, char):
        self.grid[y * self.grid_size + x] = char
        
    def display(self):
        print("  " + "  ".join(str(i) for i in range(self.grid_size)))
        for j in range(self.grid_size):
            print(str(j), end=" ")
            for k in range(self.grid_size):
                print(self.get(k, j), end="  ")
            print()
                
grid = Grid(5)

def rhombus(grid):
    mid = grid.grid_size // 2
    placeholder = mid

    for row_num in range(grid.grid_size):
        empty_spaces = abs(placeholder)
        for i in range(grid.grid_size - 2 * empty_spaces):
            grid.set(mid + (mid - empty_spaces) - i, row_num, "O")
            
        placeholder = placeholder - 1
    
rhombus(grid)
grid.display()
    