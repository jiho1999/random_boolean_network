from core.generate_RBN import generate_RBN
import random
import pytest


@pytest.fixture(autouse=True)
def set_random_seed():
    random.seed(234)


def test_generate_rbn():
    result_rbn = generate_RBN(4, 3)
    #expected_rbn =

# boolean function that is used when the seed is 234
"""
[[1, 1, 3, 4], [1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [0, 1, 1, 0],
 [1, 1, 1, 1]],
[[2, 1, 3, 4], [1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 0],
 [0, 1, 1, 1]],
[[3, 2, 3, 4], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0], [1, 0, 1, 1], [0, 1, 0, 0], [1, 1, 0, 1], [0, 1, 1, 0],
 [0, 1, 1, 1]],
[[4, 1, 2, 3], [0, 0, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [0, 1, 1, 0],
 [0, 1, 1, 1]]]
"""