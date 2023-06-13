import random
from core.boolean_function import boolean_function
from synchronous_update import synchronous_update

# generate the boolean lists
def generate_bool_lists(node_num):
    if node_num == 0:
        return [[]]
    else:
        lists = generate_bool_lists(node_num-1)
        return [lst+[0] for lst in lists] + [lst+[1] for lst in lists]
    
def generate_noise_trajectory(node_num, degree_k):
    # generate collection of initial states
    initial_state = generate_bool_lists(node_num)
    # select one random initial state (N_init) of one boolean network (There are two ways)

    # 1. select one initial state from the collection of all the possible initial states
    ran_num = random.randint(0, len(initial_state) - 1)
    N_init = initial_state[ran_num]

    # 2. generate random initial state by generating random state of each node
#    N_init = []
#    for i in range (0, node_num):
#	    N_init[i] = random.randint(0, 1)

    #generate boolean function
    bool_func = boolean_function(node_num, degree_k)

    # update the initial state about 500 times with noise probability p_noise = 0.01
    # as it update the states, save the sample in T_collection with the collection probability p_sample = 0.1
    T_collection = []
    for _ in range(500):
        # Update the state with noise probability p_noise = 0.01

        N_updated = synchronous_update(N_init, bool_func, degree_k)
        if random.random() <= 0.1:  # Collection probability p_sample = 0.1
            T_collection.append(N_updated)

    return T_collection



