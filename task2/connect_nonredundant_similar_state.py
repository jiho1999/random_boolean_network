from measure_similarity import measure_similarity
import pandas as pd


def connect_similar_state(noise_trajectory):
    trajectory_set = set()
    for x in noise_trajectory:
        for i in range(0, len(x)):
            if tuple(x[i]) not in trajectory_set:
                trajectory_set.add(tuple(x[i]))

    connection = []
    for i in range(0, len(trajectory_set)):
        trajectory_list = list(trajectory_set)
        tupe = trajectory_list[i]
        for j in range(i + 1, len(trajectory_set)):
            if measure_similarity(tupe, trajectory_list[j]) > 0.7:
                connection.append([tupe, trajectory_list[j]])

    # generate the data frame to change it into excel
    df = pd.DataFrame(connection, columns=['state1', 'state2'])
    with pd.ExcelWriter('similar_state_connection.xlsx') as writer:
        df.to_excel(writer, sheet_name='sheet1')

    return connection


connect = connect_similar_state([[[0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1]],
                                 [[0, 0, 0, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1],
                                  [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0],
                                  [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1],
                                  [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1],
                                  [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1],
                                  [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1],
                                  [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0],
                                  [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1],
                                  [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [0, 1, 1, 1, 1],
                                  [0, 1, 1, 1, 1], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0],
                                  [0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]],
                                 [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]],
                                 [[0, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1]],
                                 [[1, 1, 0, 0, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]],
                                 [[0, 1, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1],
                                  [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]],
                                 [[1, 0, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1],
                                  [0, 0, 0, 1, 1], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1],
                                  [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1],
                                  [0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1],
                                  [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1],
                                  [0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]],
                                 [[1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 1, 1, 0, 1]],
                                 [[0, 1, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 1, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1]],
                                 [[0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 0, 0, 0],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]],
                                 [[0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1],
                                  [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0],
                                  [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1],
                                  [0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1]],
                                 [[1, 1, 1, 1, 0], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [1, 1, 0, 1, 0], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1]],
                                 [[0, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1]],
                                 [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]],
                                 [[1, 1, 1, 1, 0], [0, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1]],
                                 [[1, 1, 1, 1, 0], [0, 1, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [1, 1, 0, 1, 0], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 1, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [1, 1, 0, 1, 0]],
                                 [[1, 0, 0, 0, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]],
                                 [[0, 1, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0],
                                  [0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0],
                                  [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1],
                                  [0, 1, 1, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0],
                                  [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]],
                                 [[0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [1, 1, 0, 1, 0], [0, 0, 1, 0, 0],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1],
                                  [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 0, 1]],
                                 [[0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0],
                                  [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]],
                                 [[1, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1],
                                  [0, 0, 1, 1, 1]]])
print(connect)
