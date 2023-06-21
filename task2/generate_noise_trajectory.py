import random
from core.boolean_function import boolean_function
from core.synchronous_update import synchronous_update
from generate_bool_lists import generate_bool_lists


def generate_noise_trajectory(node_num, degree_k):
    # generate collection of initial states
    initial_state = generate_bool_lists(node_num)
    # select one random initial state (N_init) of one boolean network (There are two ways)

    # generate boolean function
    bool_func = boolean_function(node_num, degree_k)

    trajectory_collection = []
    number_trajectory = 0
    while number_trajectory * 500 <= 10000:
        # 1. select one initial state from the collection of all the possible initial states
        ran_num = random.randint(0, len(initial_state) - 1)
        N_init = initial_state[ran_num]
        """
        # 2. generate random initial state by generating random state of each node
            N_init = []
            for i in range (0, node_num):
                N_init[i] = random.randint(0, 1)
        """
        # update the initial state about 500 times with noise probability p_noise = 0.01
        # as it update the states, save the sample in T_collection with the collection probability p_sample = 0.1
        T_collection = []
        # append the initial state before it starts the noise trajectory
        T_collection.append(N_init)
        for i in range(500):
            # Update the state with noise probability p_noise = 0.01
            if i == 0:
                N_updated = synchronous_update(N_init, bool_func, degree_k)
            else:
                N_updated = synchronous_update(N_updated, bool_func, degree_k)

            if random.random() <= 0.01:
                N_updated = [1 if x == 0 else 0 for x in N_updated]

            if random.random() <= 0.1:  # Collection probability p_sample = 0.1
                T_collection.append(N_updated)

        number_trajectory += 1
        trajectory_collection.append(T_collection)

    return trajectory_collection
