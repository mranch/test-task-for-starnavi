def read_matrix():
    with open('input.txt') as input_matrix:
        return [[x for x in r.split()] for r in input_matrix]


def set_route_recurrence(matrix, start=11):
    current = start

    def next_step_recurrence():
        row = current // 10 - 1
        col = current % 10 - 1
        return int(matrix[row][col])

    def create_result_list(current_list=[]):
        nonlocal current
        current_list.append(current)
        if current == next_step_recurrence():
            return current_list
        else:
            current = next_step_recurrence()
            return create_result_list(current_list)
    return create_result_list


class TestTask:
    def __init__(self, start=None, matrix=read_matrix()):
        TestTask.res = [start]
        TestTask.start = start
        TestTask.matrix = matrix

    def next_step(self, current):
        row = current // 10 - 1
        col = current % 10 - 1
        return int(self.matrix[row][col])

    @property
    def set_route(self):
        current = self.start
        next_cell = self.next_step(current)
        while current != next_cell:
            self.res.append(next_cell)
            current = next_cell
            next_cell = self.next_step(current)
        return self.res


if __name__ == '__main__':
    result = read_matrix()
    testTask = TestTask(start=11)
    with open('output_oop.txt', 'w') as output_oop:
        output_oop.write(" ".join(str(x) for x in testTask.set_route))
    func = set_route_recurrence(result)
    with open('output_recurrence.txt', 'w') as output_recurrence_result:
        output_recurrence_result.write(" ".join(str(r) for r in func()))
