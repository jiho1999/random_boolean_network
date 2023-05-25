import random

def check_functionality(boolean_function, node, k):
    update = False
    for a in range (0, node):
        for i in range (1, k+1):
            list_0 = []
            list_1 = []
            for j in range (1, 2**k + 1):
                if boolean_function[a][j][i] == 0:
#                        print(boolean_function[a][j])
                        list_0.append(boolean_function[a][j])
                else:
#                        print(boolean_function[a][j])
                        list_1.append(boolean_function[a][j])

#[[[1, 1, 3], [0, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]], 
# [[2, 2, 1], [1, 0, 0], [0, 0, 1], [0, 1, 0], [1, 1, 1]], 
# [[3, 3, 2], [0, 0, 0], [1, 0, 1], [0, 1, 0], [1, 1, 1]]]
            g = 0
            for p in list_0:
                temp_0 = p
                temp_0[i] = 1
                for l in list_1:
                    h = 0
                    for m in range (1, k+1):
                        if l[m] == temp_0[m]:
                            h += 1
                    if h == k:
                        if temp_0[0] == l[0]:
                            g += 1
            if g == (2**k)/2:
                flip_index = random.randint(1, 2**k)
                if boolean_function[a][flip_index][0] == 0:
                    print(boolean_function[a][flip_index][0])
                    print(boolean_function[a][flip_index])
                    boolean_function[a][flip_index][0] = 1
#                    print(boolean_function[a][flip_index])
                else:
#                    print(boolean_function[a][flip_index])
                    boolean_function[a][flip_index][0] = 0
#                    print(boolean_function[a][flip_index])
                update = True
    if update:
        check_functionality(boolean_function, node, k)

    return boolean_function

print(check_functionality([[[1, 1, 3], [0, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]], [[2, 2, 1], [1, 0, 0], [0, 0, 1], 
                      [0, 1, 0], [1, 1, 1]], [[3, 3, 2], [0, 0, 0], [1, 0, 1], [0, 1, 0], [1, 1, 1]]], 3,2))
