from ast import main


'2' in '251'


def valid_solution(arr):

    # check the main array
    main_arr_bool = is_valid(arr)
    if not main_arr_bool: return False

    # three by three matrixes inside them
    # idx: [0][0, 1, 2], [1][0, 1, 2], [2][0, 1, 2] -> [0: 2] [0: 2]
    # [0:3] [0:3] - [3:6] [0:]
    for i in range(0, 7):
        for j in range(0, 7):
            matrix = arr[i: i+3][j: j+3]
            if not is_valid(matrix): return False

    return True

def is_valid(arr):
    
    # {1: 1, 2:1, ...}
    # check each row and each column
    arr_len = len(arr)
    for i in range(arr_len):
    
        hori_dict = {k: 0 for k in range(1, 10)}
        vert_dict = {k: 0 for k in range(1, 10)}

        for j in range(arr_len):
            hori_val = arr[i][j]
            verti_val = arr[j][i]

            hori_dict[hori_val] = hori_dict.get(hori_val, 0) + 1
            vert_dict[verti_val] = vert_dict.get(verti_val, 0) + 1
            
        if sum(1 for i in vert_dict.values() if i==0 or i>1) or sum(1 for i in hori_dict.values() if i==0 or i>1): 
            return False
        
        return True


    

        



