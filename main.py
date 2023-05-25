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

    #generate state transition list
    state_trans = [0 for i in range(2**(node_number))]
    a = 0
    for x in initial_node:
        temp = update_list(x, bool_func, degree_k)
        state_trans[a] = temp
        a += 1
    print(state_trans)

    #Generate the list to make the data frame that is compatible to yEd
    state_trans_data_frame = []
    for lst in state_trans:
        for j in range(len(lst) - 1):
            list_1 = lst[j]
            list_2 = lst[j + 1]
            list_3 = [list_1, list_2]
            state_trans_data_frame.append(list_3)
    
    #Filter the redandant element in state_trans_data_frame
    filtered_data_frame = []
    for sublist in state_trans_data_frame:
        if sublist not in filtered_data_frame:
            filtered_data_frame.append(sublist)

    #generate the data frame to chnage it into excel
    df = pd.DataFrame(filtered_data_frame)
    #example of generating data frame
#    df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
#                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

    #generate the excel file with contents in data frame
    with pd.ExcelWriter('pandas_to_excel.xlsx') as writer:
        df.to_excel(writer, sheet_name='sheet1')

    #find an attractor from one random initial node
 #   attractor= update_list(initial, bool_func, degree_k)
 #   print (attractor)

if __name__ == "__main__":
    
    main()
