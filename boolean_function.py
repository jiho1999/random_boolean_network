from itertools import product
from bool_func_link_functionality import make_functionality
import random

"""
def boolean_function(node, k, boolean_fuc=None):
    # check the viability of node and k
    if node <= k:
        print("Oops!  That was no valid number.  Try again...")
        return 0

    # random boolean function array
    boolean_func = [0 for i in range(node)]

    # initialize the node number for each node in the boolean_func
    # initialize the random connected nodes to one specific node in the boolean_func
    for j in range(1, node + 1):
        temp = [j for i in range(k + 1)]
        # initialize each node function
        node_func = [0 for i in range(2 ** k + 1)]
        for i in range(0, 2 ** k + 1):
            node_func[i] = [0 for i in range(k + 1)]

        # algorithm that makes non-repeating random list
        randomList = []
        a = 0
        while a < k + 1:
            ran_node = random.randint(1, node)
            if ran_node not in randomList:
                randomList.append(ran_node)
                a += 1
        # convey the randomList to temporary list that is element of node_func
        for m in range(1, k + 1):
            temp[m] = randomList[m - 1]

        # convey temporary list to node_func
        node_func[0] = temp
        # insert node_func to corresponding boolean_function's index
        boolean_func[j - 1] = node_func

    # initialize the random itertools functions
    for a in range(1, node + 1):
        combinations = list(product([0, 1], repeat=k))
        temp_node = boolean_func[a - 1]
        for l, temp_tupe in enumerate(combinations, start=1):
            random_status = random.randint(0, 1)
            temp_lst = [random_status] + list(temp_tupe)
            temp_node[l] = temp_lst

    # make the boolean function functional
    boolean_func = make_functionality(boolean_func, node, k)

    return boolean_func
"""

def boolean_function(node, k, boolean_func=None):
    if node <= k:
        print("Oops! That was no valid number. Try again...")
        return 0

    boolean_func = [0] * node

    for j in range(1, node + 1):
        node_func = [[0] * (k + 1) for _ in range(2 ** k + 1)]

        randomList = set()
        while len(randomList) < k:
            ran_node = random.randint(1, node)
            randomList.add(ran_node)
        temp = [j] + list(randomList)
        
        node_func[0] = temp
        boolean_func[j - 1] = node_func

        combinations = list(product([0, 1], repeat=k))
        for l, temp_tupe in enumerate(combinations, start=1):
            random_status = random.randint(0, 1)
            temp_lst = [random_status] + list(temp_tupe)
            node_func[l] = temp_lst

    boolean_func = make_functionality(boolean_func, node, k)

    return boolean_func

#bool_func = boolean_function(4, 3)
#print(bool_func)

