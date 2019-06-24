from collections import namedtuple
from itertools import chain

Package = namedtuple('Package', ('price', 'weight'))


def generate_cell(i, w, grid, items):
    res = 0
    prev_row = i - 1
    if i > 0:
        res = grid[prev_row][w]
        alt_w = w - items[i].weight
        if alt_w >= 0:
            res = max(
                grid[prev_row][alt_w] + items[i].price,
                res
            )

    return res

def find_max_idx(grid):
    max_idx = (-1, -1)
    for i, row in enumerate(grid):
        w = row.index(max(row))
        if max_idx == (-1, -1) or grid[i][w] > grid[max_idx[0]][max_idx[1]]:
            max_idx = (i, w)

    return max_idx

def build_grid(items, capacity):
    item_count = len(items) + 1
    capacity = capacity + 1
    grid = []
    for i in range(item_count):
        grid.append([generate_cell(i, w, grid, items) for w in range(capacity)])

    return grid


def get_optimal_set(i, total, grid, items):
    if i > 0 and total > 0:
        total, o_items = (total, []) if total in grid[i - 1] else (total - items[i].price, [i])
        return o_items + get_optimal_set(i - 1, total, grid, items)

    return []
        


if __name__ == '__main__':
    items = {
        1: Package(9, 7),
        2: Package(2, 1),
        3: Package(7, 3),
        4: Package(6, 5)
    }

    grid = build_grid(items, 8)
    i, w = find_max_idx(grid)
    total = grid[i][w]
    print(get_optimal_set(i, total, grid, items))