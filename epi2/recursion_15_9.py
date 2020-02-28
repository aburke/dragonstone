import math
from itertools import product

class SudokuSolver(object):

    def __init__(self, grid):
        self.grid = grid
        self.univ = set(v + 1 for v in range(len(grid)))

    def get_region_items(self, i, j):
        region_size = int(math.sqrt(len(self.grid)))
        I = i // region_size
        J = j // region_size

        get_item = lambda m, q : self.grid[m][q]
        return [get_item(region_size * I + a, region_size * J + b) for a, b in product(range(region_size), repeat = 2)]

    def check_row(self, row_idx):
        return self.univ - set(r for r in self.grid[row_idx] if r is not None)

    def check_column(self, col_idx):
        return self.univ - set(self.grid[i][col_idx] for i in range(len(self.grid)) if self.grid[i][col_idx] is not None)

    def check_region(self, row_idx, col_idx):
        return self.univ - set(self.get_region_items(row_idx, col_idx))

    def check_missing(self, i, missing):
        if i < len(missing):
            row_idx, col_idx = missing[i]
            
            
            options = self.check_row(row_idx).intersection(
                self.check_column(col_idx).intersection(
                    self.check_region(row_idx, col_idx)
                )
            )

            for choice in options:
                self.grid[row_idx][col_idx] = choice
                if i + 1 < len(missing):
                    self.check_missing(i + 1, missing)
                    m, q = missing[i + 1]
                    if self.grid[m][q] is not None:
                        break    
                    self.grid[row_idx][col_idx] = None

    def solve(self):
        missing = [(q, i) for q in range(len(self.grid)) for i, x in enumerate(self.grid[q]) if x is None]
        self.check_missing(0, missing)
            
            



if __name__ == "__main__":
    # grid = [
    #     [1, None, None, None], 
    #     [None, 4, None, 2], 
    #     [None, None, 4, None], 
    #     [4, None, None, 3]
    # ]
    grid = [
        [5, 3, None, None, 7, None, None, None, None],
        [6, None, None, 1, 9, 5, None, None, None],
        [None, 9, 8, None, None, None, None, 6, None],
        [8, None, None, None, 6, None, None, None, 3],
        [4, None, None, 8, None, 3, None, None, 1],
        [7, None, None, None, 2, None, None, None, 6],
        [None, 6, None, None, None, None, 2, 8, None],
        [None, None, None, 4, 1, 9, None, None, 5],
        [None, None, None, None, 8, None, None, 7, 9]
    ]
    ss = SudokuSolver(grid)
    ss.solve()
    print(ss.grid)