from core.generate_state_update_list import generate_state_update_list


def test_generate_state_update_list():
    initial_state = [0, 0, 1, 0]
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
    expected_state_update_list = [[0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 1], [1, 0, 1, 1], [0, 0, 0, 0], [1, 0, 1, 1]]
    result_state_update_list = generate_state_update_list(initial_state, boolean_function, 3)

    assert result_state_update_list == expected_state_update_list
