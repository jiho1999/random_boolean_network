from itertools import product
import random

def boolean_function(node, k, boolean_fuc=None):
    #check the viability of node and k
    if node <= k:
        print("Oops!  That was no valid number.  Try again...")
        return 0

    #random boolean function array
    boolean_func = [0 for i in range(node)]

    #initialize the node number for each node in the boolean_func
    #initialize the random connected nodes to one specific node in the boolean_func
    for j in range(1, node + 1):
        temp = [j for i in range(k + 1)]
        #initilaize each node function
        node_func = [0 for i in range(2 ** k + 1)]
        for i in range(0, 2 ** k + 1):
            node_func[i] = [0 for i in range(k + 1)]

        #algorithm that makes non-repeating random list
        randomList = []
        a = 0
        while a < k + 1:
            ran_node = random.randint (1, node)
            if ran_node not in randomList:
                randomList.append(ran_node)
                a += 1
        #convey the randomList to temporary list that is element of node_func
        for m in range(1, k + 1):
            temp[m] = randomList[m - 1]

        #convey temporary list to node_func
        node_func[0] = temp
        #insert node_func to corresponding boolean_function's index
        boolean_func[j - 1] = node_func

    #initialize the random itertools functions
    for a in range(1, node + 1):
        combinations = list(product([0, 1], repeat=k))
        temp_node = boolean_func[a - 1]
        for l in range(1, 2 ** k + 1):
            random_status = random.randint(0, 1)
            temp_lst = [random_status for i in range(k + 1)]
            temp_tupe = combinations[l-1]
            a = 1
            for x in temp_tupe:
                temp_lst[a] = x
                a += 1
            temp_node[l] = temp_lst

    return boolean_func

bool_func = boolean_function(3, 1)
