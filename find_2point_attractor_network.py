import math

#•	make random networks with 2-point attractors only (ignore the rest)
#-	set each state’s ID to 0 
#-	start with 0000… state, give it ID = 1 
#-	keep stepping until you find an attractor, and every state you step to get ID = 1 
#-	restart with next state, if it has no ID (or ID = 0). Set it to ID = 2, keep going and setting all states to ID = 2 

#if you run into a state with non-0 ID, change all ID = 2 to this non-0 ID 
#if you find an attractor with no ID -> this is attractor 2! 

#-	Repeat until all states have ID 
#-	Highest ID = attractor number 
[[[0, 0, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 0, 1], [1, 0, 0]], [[0, 1, 0], [1, 0, 1], [0, 0, 0], [1, 0, 1]], 
 [[1, 1, 0], [0, 0, 1], [1, 0, 0], [0, 0, 1]], [[0, 0, 1], [1, 0, 0], [0, 0, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]], 
 [[0, 1, 1], [1, 0, 0], [0, 0, 1], [1, 0, 0]], [[1, 1, 1], [0, 0, 0], [1, 0, 1], [0, 0, 0]]]

# make dictionary for 2 point attractor random networks
def generate_bool_lists(node_num):
    if node_num == 0:
        return [[]]
    else:
        lists = generate_bool_lists(node_num-1)
        return [lst+[0] for lst in lists] + [lst+[1] for lst in lists]

def find_two_point_attractor(random_boolean_network):
    # et the number of nodes from the number of states in random Boolean network
    node_num = int (math.log(len(random_boolean_network), 10) / math.log(2, 10))

    # generate the dictionary for random Boolean network's state combinations of basin ID
    state_combination = generate_bool_lists(node_num)
    ID_state_combination = {}
    for i in range (0, 2**node_num):
        temp_state = tuple(state_combination[i])
        ID_state_combination[temp_state] = 0

    # Give correct basin ID to each state in random Boolean network
    id = 0
    for i in range(0, len(random_boolean_network)):
        id = max(ID_state_combination.values()) + 1
        for j in range(0, len(random_boolean_network[i])):
            state = random_boolean_network[i][j]
            state_tuple = tuple(state)
            
            if ID_state_combination[state_tuple] == 0:
                ID_state_combination[state_tuple] = id
            elif ID_state_combination[state_tuple] == id:
                ID_state_combination[state_tuple] = id
            else:
                temp_id = ID_state_combination[state_tuple]
                for k in range(0, j):
                        temp_state = tuple(random_boolean_network[i][k])
                        ID_state_combination[temp_state] = temp_id
                break

    # Find the highest assigned ID, which corresponds to the total number of basins
    highest_id = max(ID_state_combination.values())

    return highest_id



print(find_two_point_attractor([[[0, 0, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 0, 1], [1, 0, 0]], [[0, 1, 0], [1, 0, 1], [0, 0, 0], [1, 0, 1]], 
 [[1, 1, 0], [0, 0, 1], [1, 0, 0], [0, 0, 1]], [[0, 0, 1], [1, 0, 0], [0, 0, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]], 
 [[0, 1, 1], [1, 0, 0], [0, 0, 1], [1, 0, 0]], [[1, 1, 1], [0, 0, 0], [1, 0, 1], [0, 0, 0]]]))
