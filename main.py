import random
from itertools import chain, zip_longest


def get_random_map(row_count, col_count):
    return [
        [("." if random.randint(0, 5) < 4 else ("o" if random.randint(0, 1) == 0 else "x")) for _ in range(col_count)]
        for _ in range(row_count)]


def pretty_matrix(matrix):
    return "\n".join("  ".join(row) for row in matrix)

for i in range(10):
    print(pretty_matrix(get_random_map(10, 10)))
    print()
