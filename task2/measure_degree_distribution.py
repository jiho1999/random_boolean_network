from generate_bool_lists import generate_bool_lists
import pandas as pd


def measure_degree_distribution(connection):
    # generate bool_list so we can make boolean dictionary
    node_num = len(connection[0][0])
    bool_list = generate_bool_lists(node_num)

    # initialize boolean dictionary that stores the number of links in each state
    bool_dictionary = dict()
    for key in bool_list:
        bool_dictionary[tuple(key)] = 0

    # store number of links in boolean dictionary
    for con in connection:
        con1 = con[0]
        con2 = con[1]
        if con1 == con2:
            bool_dictionary[con1] += 1
        else:
            bool_dictionary[con1] += 1
            bool_dictionary[con2] += 1

    # store the number of links k and numer of states that correspond to the number k
    max_val = max(bool_dictionary.values())
    degree_distribution_dict = dict()

    for key in range(1, max_val + 1):
        degree_distribution_dict[key] = 0

    for value in bool_dictionary.values():
        if value != 0:
            degree_distribution_dict[value] += 1

    return degree_distribution_dict


"""
        # Convert dictionary to DataFrame
        df = pd.DataFrame(list(degree_distribution_dict.items()), columns=['Key', 'Value'])

        # Specify the filename
        filename = 'degree_distribution.xlsx'

        # Export DataFrame to Excel
        df.to_excel(filename, index=False)
"""
