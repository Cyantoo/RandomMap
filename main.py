import random
from itertools import chain, zip_longest


def get_random_map(row_count, col_count, obstacle_density, obscuring_proportion):
    return [
        [("." if random.random() > obstacle_density else ("o" if random.random() < obscuring_proportion else "x")) for _ in range(col_count)]
        for _ in range(row_count)]


def pretty_matrix(matrix):
    return "\n".join("  ".join(row) for row in matrix)

for i in range(10):
    print(pretty_matrix(get_random_map(10, 10, 1./3, 1./2)))
    print()
