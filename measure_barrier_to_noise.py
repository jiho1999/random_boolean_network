def measure_barrier_to_noise(random_boolean_network):
    base_to_attractor = {}
    for i in range (0, len(random_boolean_network)):
        base_to_attractor[tuple(random_boolean_network[i][0])] = tuple(random_boolean_network[i])
    
    node_num = len(random_boolean_network[0][0])
    num_steady_state = 0
    for i in range(0, len(random_boolean_network)):
        original_state = tuple(random_boolean_network[i][0])
        for j in range(0, node_num):
            flipped_state = list(original_state)
            if original_state[j] == 0:
                flipped_state[j] = 1
            else:
                flipped_state[j] = 0
            
            flipped_state = tuple(flipped_state)

            if base_to_attractor[flipped_state][-1] in base_to_attractor[original_state]:
                num_steady_state += 1

    fraction_no_attractor_change = num_steady_state / ((2**node_num)*node_num)

    return fraction_no_attractor_change

#print(measure_barrier_to_noise([[[0, 0, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 0, 1], [1, 0, 0]], [[0, 1, 0], [1, 0, 1], [0, 0, 0], [1, 0, 1]],
# [[1, 1, 0], [0, 0, 1], [1, 0, 0], [0, 0, 1]], [[0, 0, 1], [1, 0, 0], [0, 0, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]], 
# [[0, 1, 1], [1, 0, 0], [0, 0, 1], [1, 0, 0]], [[1, 1, 1], [0, 0, 0], [1, 0, 1], [0, 0, 0]]]))