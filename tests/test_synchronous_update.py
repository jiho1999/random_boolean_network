import sys
sys.path.append("/Users/jihopark/Desktop/Projects/random_boolean_network/core")

import synchronous_update


def test_can_update_synchronously():
    boolean_function = [
        [[1, 1, 2, 4], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 0],
         [1, 1, 1, 1]],
        [[2, 1, 2, 3], [0, 0, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 0],
         [1, 1, 1, 1]],
        [[3, 1, 3, 4], [1, 0, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0],
         [0, 1, 1, 1]],
        [[4, 1, 3, 4], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0],
         [0, 1, 1, 1]]
    ]

    initial_state = [1, 1, 0, 0]
    assert synchronous_update(initial_state, boolean_function, 3) == [1, 1, 1, 1]
