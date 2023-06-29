def generate_bool_lists(node_num):
    if node_num == 0:
        return [[]]
    else:
        lists = generate_bool_lists(node_num - 1)
        return [lst + [0] for lst in lists] + [lst + [1] for lst in lists]