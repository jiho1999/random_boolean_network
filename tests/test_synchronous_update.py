from core.synchronous_update import synchronous_update


def test_can_update_synchronously():
    initial_state = [1, 1, 0, 0]
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
    expected_synchronously_updated_state = [1, 1, 1, 1]
    result_synchronously_updated_state = synchronous_update(initial_state, boolean_function, 3)

    assert result_synchronously_updated_state == expected_synchronously_updated_state
