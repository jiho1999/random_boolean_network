import random
def generate_initial(node):
    # array for initial state of the node
    initial_state = [0 for i in range(node)]

    # generate initial random state of the nodes
    for i in range(0, node):
        initial_state[i] = random.randint(0, 1)

    return (initial_state)

