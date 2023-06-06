import random

def make_functionality(boolean_function, node, k):
    update = False
    for a in range(0, node):
        for i in range(1, k + 1):
            list_0 = []
            list_1 = []
            for j in range(1, 2 ** k + 1):
                if boolean_function[a][j][i] == 0:
                    list_0.append(boolean_function[a][j])
                else:
                    list_1.append(boolean_function[a][j])

            g = 0
            for p in list_0:
                temp_0 = []
                for q in range(0, len(p)):
                    temp_0.append(p[q])
                temp_0[i] = 1
                for l in list_1:
                    h = 0
                    for m in range(1, k + 1):
                        if l[m] == temp_0[m]:
                            h += 1
                    if h == k:
                        if temp_0[0] == l[0]:
                            g += 1
            if g == (2 ** k) / 2:
                flip_index = random.randint(1, 2 ** k)
                if boolean_function[a][flip_index][0] == 0:
                    boolean_function[a][flip_index][0] = 1
                else:
                    boolean_function[a][flip_index][0] = 0
                update = True
    if update:
        make_functionality(boolean_function, node, k)

    return boolean_function


#functional = make_functionality(
#    [[[1, 1, 3], [0, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]], [[2, 2, 1], [1, 0, 0], [0, 0, 1], [0, 1, 0], [1, 1, 1]],
#     [[3, 3, 2], [0, 0, 0], [1, 0, 1], [0, 1, 0], [1, 1, 1]]], 3, 2)
#print(functional)
