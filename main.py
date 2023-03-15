from random_initial import generate_initial
from boolean_function import boolean_function
from find_attractor import update_list

from synchronous_update import synchronous_update
from itertools import product

def main(initial=None):
    # takes random number of nodes
    node_number = int(input("Enter the number of nodes: "))

    # takes random average degree
    degree_k = int(input("Enter the average degree k: "))

    #initialize initial node status
    initial = generate_initial(node_number)

    #generate boolean function
    bool_func = boolean_function(node_number, degree_k)

    #return synchronous updated node status
#    updated = synchronous_update(initial, bool_func, degree_k)
#    print(updated)

    attractor = update_list(initial, bool_func, degree_k)
    print (attractor)

if __name__ == "__main__":

    main()