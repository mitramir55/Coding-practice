


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


    

        








def valid_solution(arr):
    
    # check the main array
    if not check_lines(arr): return False
    
    # three by three matrixes inside them
    # idx: [0][0, 1, 2], [1][0, 1, 2], [2][0, 1, 2] -> [0: 2] [0: 2]
    # [0:3] [0:3] - [3:6] [0:]
    print('\nstarting smaller ones...')
    for i in range(0, 7):
        for j in range(0, 7):
            matrix = [m[j: j+3] for m in arr[i: i+3]]
            valid_bool = is_valid_matrix(matrix)
            if valid_bool != 0: 
                print(f'inside [i: i+3][j: j+3] = {i}: {i+3}, {j}: {j+3}')
                print('matrix is :', matrix)
                print('the result is ', is_valid_matrix(matrix))
                return False

    return True

def is_valid_matrix(matrix):
    
    len_ = len(matrix)
    dict_ = {k: 0 for k in range(1, 10)}
    
    for i in range(len_):
        for j in range(len_):
            
            val = matrix[i][j]
            print(val)
            dict_[val] = dict_.get(val, 0) + 1
            
    return sum(1 for i in dict_.values() if i==0 or i>1)


def check_lines(arr):
    
    # {1: 1, 2:1, ...}
    # check each row and each column
    arr_len = len(arr)
    
    for i in range(arr_len):
        print()
        print('array is : ')
        print(arr)
    
        hori_dict = {k: 0 for k in range(1, 10)}
        vert_dict = {k: 0 for k in range(1, 10)}

        for j in range(arr_len):
            hori_val = arr[i][j]
            verti_val = arr[j][i]

            hori_dict[hori_val] = hori_dict.get(hori_val, 0) + 1
            vert_dict[verti_val] = vert_dict.get(verti_val, 0) + 1
            
        if sum(1 for i in vert_dict.values() if i==0 or i>1) or sum(1 for i in hori_dict.values() if i==0 or i>1): 
            print('not summed to one')
            print('vert_dict: \n', vert_dict)
            print('hori_dict: \n', hori_dict)
            
            return False
        
        return True


[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 8, 3, 4, 2, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 2, 8, 6, 1, 7, 9]