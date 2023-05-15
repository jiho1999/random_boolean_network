from random_initial import generate_initial
from boolean_function import boolean_function
from find_attractor import update_list

from synchronous_update import synchronous_update
from itertools import product

import pandas as pd
import openpyxl

#generate the boolean lists
def generate_bool_lists(n):
    if n == 0:
        return [[]]
    else:
        lists = generate_bool_lists(n-1)
        return [lst+[0] for lst in lists] + [lst+[1] for lst in lists]


def main(initial=None):
    # takes random number of nodes
    node_number = int(input("Enter the number of nodes: "))

    # takes random average degree
    degree_k = int(input("Enter the average degree k: "))

    #initialize initial node status
    initial = generate_initial(node_number)

    #initialize all possibilites of initial node status
    initial_node = generate_bool_lists(node_number)

    #generate boolean function
    bool_func = boolean_function(node_number, degree_k)

    #return synchronous updated node status
#   updated = synchronous_update(initial, bool_func, degree_k)


    #generate attractor list
#    attractor_lst = [0 for i in range(2**(node_number))]
#    a = 0
#    for x in initial_node:
#        attractor_lst[a] = update_list(x, bool_func, degree_k)
#        a += 1
#        print(x)

#    print(attractor_lst)

    #generate state transition list
    state_trans = [0 for i in range(2**(node_number))]
    a = 0
    for x in initial_node:
        temp = update_list(x, bool_func, degree_k)
        state_trans[a] = temp
        a += 1
    print(state_trans)   

    df = pd.DataFrame(state_trans)
#    df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
#                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])
    
    with pd.ExcelWriter('pandas_to_excel.xlsx') as writer:
        df.to_excel(writer, sheet_name='sheet1')

    #find an attractor from one random initial node
 #   attractor= update_list(initial, bool_func, degree_k)
 #   print (attractor)

if __name__ == "__main__":
    
    main()
    