from collections import namedtuple
from itertools import product

Pos = namedtuple('Pos', ['x', 'y'])


def path_exists(univ, path, pos):
    if not path:
        return True
    else:
        potentials = get_options(pos, univ)
        actual_options = [p for p in potentials if univ[p.x][p.y] == path[0]]
        pe = False
        for new_pos in actual_options:
            pe = pe or path_exists(univ, path[1:], new_pos)
            if pe:
                break
        return pe

def get_options(pos, univ):
    idx_deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    is_valid = lambda x, y: 0 <= x < len(univ) and 0 <= y < len(univ[0])
    return [Pos(pos.x + x, pos.y + y) for x, y in idx_deltas if is_valid(pos.x + x, pos.y + y)]


if __name__ == "__main__":
    univ = [
        [1, 2, 3],
        [4, 5, 9],
        [5, 6, 7]
    ]
    path = [7, 6, 5, 9, 7, 6, 5, 5]
    pe = False
    for x, y in product(range(len(univ)), repeat=2):
        pe = path_exists(univ, path, Pos(x, y))
        if pe:
            break

    print(pe)