from itertools import product
from collections import deque

data = """AAAA
BBCD
BBCC
EEEC"""

def parse_input():
    lines = [l.strip() for l in data.split('\n')]
    x_lim = len(lines[0])
    y_lim = len(lines)
    grid = {(x, y): lines[y][x] for x, y in product(range(x_lim),
                                                    range(y_lim))}
    # Pad :)

    for y in range(-1, y_lim + 1):
        grid[(-1, y)] = '.'
        grid[(x_lim, y)] = '.'

    for x in range(-1, x_lim + 1):
        grid[(x, -1)] = '.'
        grid[(x, y_lim)] = '.'

    return grid, x_lim, y_lim

def get_neighbors(pos):
    x, y = pos

    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

def get_corner_neighbors(pos):
    x, y = pos

    yield [(x - 1, y), (x - 1, y - 1), (x, y - 1)]
    yield [(x, y - 1), (x + 1, y - 1), (x + 1, y)]
    yield [(x + 1, y), (x + 1, y + 1), (x, y + 1)]
    yield [(x, y + 1), (x - 1, y + 1), (x - 1, y)]

def fill_plot(grid, start):
    Q = deque([start])
    visited = set()
    c = grid[start]
    visited.add(start)
    perimeter = 0

    while Q:
        v = Q.popleft()

        for vn in get_neighbors(v):
            if grid[vn] != c:
                perimeter += 1
            elif vn not in visited:
                visited.add(vn)
                Q.append(vn)

    return perimeter, visited

def compute(grid, x_lim, y_lim):
    visited = set()
    price = 0

    for pos in product(range(x_lim), range(y_lim)):
        if pos not in visited:
            _, plot = fill_plot(grid, pos)
            visited.update(plot)
            c = grid[pos]
            corners = 0

            for plot_pos in plot:
                corners += sum(
                    all(grid[cn] != c for cn in cn_list[::2])
                        or (all(grid[cn] == c for cn in cn_list[::2])
                        and grid[cn_list[1]] != c) for cn_list
                        in get_corner_neighbors(plot_pos)
                )

            price += corners * len(plot)

    print(price)

MATRIX = parse_input()

compute(*MATRIX[:])