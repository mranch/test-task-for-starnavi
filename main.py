def read_matrix():
    with open('input.txt') as input_matrix:
        return [[x for x in r.split()] for r in input_matrix]


def next_step(matrix, current):
    row = current // 10 - 1
    col = current % 10 - 1
    return int(matrix[row][col])


def set_route(matrix):
    start = 11
    current = start
    res = [current]
    next_cell = next_step(matrix, current)
    while current != next_cell:
        res.append(next_cell)
        current = next_cell
        next_cell = next_step(matrix, current)
    return res


if __name__ == '__main__':
    result = read_matrix()
    with open('output.txt', 'w') as output_result:
        output_result.write(" ".join(str(r) for r in set_route(result)))
