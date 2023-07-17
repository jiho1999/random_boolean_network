from core.boolean_function import boolean_function
import pytest
import random


@pytest.fixture(autouse=True)
def set_random_seed():
    random.seed(234)


def test_can_check_boolean_function():
    node_number = 4
    average_degree_k = 3
    expected_result = [
        [[1, 1, 3, 4], [1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [0, 1, 1, 0],
         [1, 1, 1, 1]],
        [[2, 1, 3, 4], [1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 0],
         [0, 1, 1, 1]],
        [[3, 2, 3, 4], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0], [1, 0, 1, 1], [0, 1, 0, 0], [1, 1, 0, 1], [0, 1, 1, 0],
         [0, 1, 1, 1]],
        [[4, 1, 2, 3], [0, 0, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [0, 1, 1, 0],
         [0, 1, 1, 1]]]
    result = boolean_function(node_number, average_degree_k)

    assert result == expected_result
