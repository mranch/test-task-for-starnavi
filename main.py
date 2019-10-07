import pytest

necessary_result = [11, 55, 15, 21, 44, 32, 13, 25, 43]


def read_matrix(file_name='input.txt'):
    with open(file_name) as input_matrix:
        return [[x for x in r.split()] for r in input_matrix]


def set_route_recurrence(matrix=read_matrix(), start=11):
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
    def __init__(self, start=11, matrix=read_matrix()):
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


@pytest.mark.parametrize("expected", [necessary_result])
def test_set_route_oop(expected):
    vvv = TestTask(matrix=read_matrix('test_input.txt'))
    assert expected == vvv.set_route


@pytest.mark.parametrize("expected", [necessary_result])
def test_set_route_fp(expected):
    func = set_route_recurrence(matrix=read_matrix('test_input.txt'))
    assert expected == func()


if __name__ == '__main__':
    with open('output_oop.txt', 'w') as oop_result:
        testTask = TestTask()
        oop_result.write(" ".join(str(x) for x in testTask.set_route))
    with open('output_recurrence.txt', 'w') as recurrence_result:
        recurrence_result.write(" ".join(str(x) for x in set_route_recurrence()()))
