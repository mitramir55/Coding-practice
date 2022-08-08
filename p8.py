
def in_matrix(i, j, array):
    return 0 <= i < len(array) and 0 <= j < len(array)

def is_visited(i, j, array):
    return array[i][j] == '0'


directions = [
    lambda i, j: (i, j+1),
    lambda i, j: (i+1, j),
    lambda i, j: (i, j-1),
    lambda i, j: (i-1, j)
]


def snail(array):
    
    print('started ...')
    print('This is the array len: ', len(array))
    print("\n array is : ", array)
    if len(array[0]) == 0: return []
    if len(array[0]) == 1: return array[0]
    direction_cnt = 0
    return_list = []

    i, j = 0, 0
    return_list.append(array[i][j])

    # visited mark
    array[0][0] = '0'

    while True: 
        # which way to go?
        direction_function = directions[direction_cnt%4]

        tmp_i, tmp_j = direction_function(i, j)
        
        # is it time to change direction?
        if (not in_matrix(tmp_i, tmp_j, array)) or is_visited(tmp_i, tmp_j, array):
            direction_cnt += 1
            print('direction_cnt = ', direction_cnt)

        else:
            # if still in this direction
            # change the i and j and append the value
            i, j = tmp_i, tmp_j
            return_list.append(array[i][j])

            # then mark it as visited
            array[i][j] = '0'

            # is it all in?
            if len(return_list) == len(array)**2:
                print('returned the list')
                return return_list

snail([[1]])



import numpy as np
def snail(array):

    final_list = []
    array = a

    while len(array)>0:   
        print(array)
        final_list += array[0].tolist()
        array = np.rot90(array[1:])

    return final_list


array_ = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]

snail(array_)


print(array_)
array_ = np.array(array_)
print(array_)
array_ = array_.tolist()


array_.pop(0)


array_ = np.rot90(array_)