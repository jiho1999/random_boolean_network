from generate_bool_lists import generate_bool_lists
from measure_similarity import measure_similarity
import pandas as pd


def measure_degree_distribution(noise_trajectory):
    # make several noise trajectory into one trajectory list
    trajectory_lst = []
    for element in noise_trajectory:
        for i in range(0, len(element)):
            trajectory_lst.append(element[i])

    # initialize boolean dictionary that stores the number of links for each state
    bool_dictionary = dict()
    for i in range(0, len(trajectory_lst)):
        bool_dictionary[i] = 0

    # store number of links in boolean dictionary
    for i in range(0, len(trajectory_lst) - 1):
        compared_element = trajectory_lst[i]
        for j in range(i + 1, len(trajectory_lst)):
            if measure_similarity(compared_element, trajectory_lst[j]) > 0.8:
                bool_dictionary[i] += 1
                bool_dictionary[j] += 1

    # store the number of links k and number of states that correspond to the number k
    max_val = max(bool_dictionary.values())
    degree_distribution_dict = dict()

    for key in range(1, max_val + 1):
        degree_distribution_dict[key] = 0

    for value in bool_dictionary.values():
        if value != 0:
            degree_distribution_dict[value] += 1

    return degree_distribution_dict


print(measure_degree_distribution([[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0]],
                                [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0]]]))

"""
        # Convert dictionary to DataFrame
        df = pd.DataFrame(list(degree_distribution_dict.items()), columns=['Key', 'Value'])

        # Specify the filename
        filename = 'degree_distribution.xlsx'

        # Export DataFrame to Excel
        df.to_excel(filename, index=False)
"""
