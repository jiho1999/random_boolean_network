from find_attractor import update_list
from bool_func_link_functionality import make_functionality
from boolean_function import boolean_function

#generate the boolean lists
def generate_bool_lists(n):
    if n == 0:
        return [[]]
    else:
        lists = generate_bool_lists(n-1)
        return [lst+[0] for lst in lists] + [lst+[1] for lst in lists]

def generate_RBN(node_number, degree_k):
    #initialize all possibilites of initial node status
    initial_node = generate_bool_lists(node_number)

    #generate boolean function and make it functional
    bool_func = boolean_function(node_number, degree_k)
    bool_func = make_functionality(bool_func)

    #generate state transition list
    random_Boolean_network = [0 for i in range(2**(node_number))]
    a = 0
    for x in initial_node:
        temp = update_list(x, bool_func, degree_k)
        random_Boolean_network[a] = temp
        a += 1

    return random_Boolean_network
