def measure_similarity(state1, state2):
    node_num = len(state1)
    hamming_distance = 0
    for i in range(0, node_num):
        if state1[i] == state2[i]:
            hamming_distance += 1

    return hamming_distance / node_num
