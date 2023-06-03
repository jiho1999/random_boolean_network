def synchronous_update(initial_stat, boolean_function, k):
    num_nodes = len(initial_stat)
    updated_status = [0 for i in range(num_nodes)]

    for i in range(0, num_nodes):
        # connected node in Boolean Node
        con_node = [0 for i in range(k)]
        # connected node's initial status
        con_stat_init = [0 for i in range(k)]
        # boolean_node for each ith node
        boolean_node = boolean_function[i]

        # creating connected node in order of Boolean Node
        for j in range(0, k):
            con_node[j] = boolean_node[0][j + 1]

        # creating connected node's initial status
        for l in range(0, k):
            target = con_node[l]
            con_stat_init[l] = initial_stat[target - 1]

        for l in range(1, 2 ** k):
            a = 0
            for n in range(0, k):
                if boolean_node[l][n+1] == con_stat_init[n]:
                    a += 1
                if a == k:
                        updated_status[i] = boolean_node[l][0]

    return updated_status