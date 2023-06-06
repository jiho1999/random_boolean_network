from find_2point_attractor_network import find_two_point_attractor

def measure_basin_difference(id_state_combination):
    basin_1 = 0
    basin_2 = 0
    basin_difference = 0

    for x in id_state_combination:
        if id_state_combination[x] == 1:
            basin_1 += 1
        else:
            basin_2 += 1

    if basin_1 >= basin_2:
        basin_difference = (basin_1)/(basin_1 + basin_2) - (basin_2)/(basin_1 + basin_2)
    else:
        basin_difference = (basin_2)/(basin_1 + basin_2) - (basin_1)/(basin_1 + basin_2)

    return basin_difference

#highest_id, id_state_combi = find_two_point_attractor([[[0, 0, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 0, 1], [1, 0, 0]], [[0, 1, 0], [1, 0, 1], [0, 0, 0], [1, 0, 1]], 
# [[1, 1, 0], [0, 0, 1], [1, 0, 0], [0, 0, 1]], [[0, 0, 1], [1, 0, 0], [0, 0, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]], 
# [[0, 1, 1], [1, 0, 0], [0, 0, 1], [1, 0, 0]], [[1, 1, 1], [0, 0, 0], [1, 0, 1], [0, 0, 0]]])

#print(measure_basin_difference(id_state_combi))