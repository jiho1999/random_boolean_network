from core.bool_func_link_functionality import make_functionality
import pytest
import random


@pytest.fixture(autouse=True)
def set_random_seed():
    random.seed(123)


@pytest.fixture
def sample_boolean_function():
    return [[[1, 1, 3], [0, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]],
            [[2, 2, 1], [1, 0, 0], [0, 0, 1], [0, 1, 0], [1, 1, 1]],
            [[3, 3, 2], [0, 0, 0], [1, 0, 1], [0, 1, 0], [1, 1, 1]]]


def test_can_check_bool_func_link_functionality(sample_boolean_function):
    node_number = 3
    average_degree_k = 2
    expected_functional_boolean_function = [[[1, 1, 3], [0, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]],
                       [[2, 2, 1], [1, 0, 0], [0, 0, 1], [0, 1, 0], [1, 1, 1]],
                       [[3, 3, 2], [1, 0, 0], [1, 0, 1], [0, 1, 0], [1, 1, 1]]]
    result_functional_boolean_function = make_functionality(sample_boolean_function, node_number, average_degree_k)

    assert result_functional_boolean_function == expected_functional_boolean_function, f"Expected: {expected_functional_boolean_function}, Got: {result_functional_boolean_function}"
