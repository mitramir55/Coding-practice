from sqlalchemy import all_


word = 'this'
word[::-1]
word[-1]

def pig_it(text):
    words_list = []

    for word in text.split(" "):
        final_word = word

        if not word.isalpha(): 
            words_list.append(word)
            continue

        if len(word)>=2:
            final_word[0] = word[-1]
            final_word[-1] = word[0]

        final_word =+ 'ay'
        words_list.append(final_word)
        return " ".join(words_list)

'miti'[-1]





def pig_it(text):
    words_list = []

    for word in text.split(" "):

        if not word.isalpha(): 
            words_list.append(word)
            continue

        if len(word)>=2:
            letters = list(word)
            final_word_letters = letters[:-1]
            print(final_word_letters)
            final_word_letters = final_word_letters.insert(0, 'n')
            print(final_word_letters)

        final_word = "".join(final_word_letters) + 'ay'
        words_list.append(final_word)
        
    return " ".join(words_list)
pig_it('moto')


<<<<<<< HEAD
def snail(all_arrays):
    

    all_arrays_len = len(all_arrays)
    one_array_len = len(all_arrays[0])

    # 0, 2, 4, ...
    for i in range(0, one_array_len/2 +1, 2):
        all_arrays[i][:] + all_arrays[i:all_arrays_len-i][-1] + all_arrays[-i-1]


all_arrays = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12]]

all_arrays_len = len(all_arrays)
one_array_len = len(all_arrays[0])
one_array_len


i = 0
all_arrays[i][:] + \
     [arr[-1] for arr in all_arrays[i+1:all_arrays_len-i]] + \
         all_arrays[-i-1][i+1::-1] + \
[arr[0] for arr in all_arrays[-all_arrays_len+1+i : -i : -1]]



all_arrays_len
all_arrays[-i-1][i+1::-1] 


[arr[0] for arr in all_arrays[i:all_arrays_len-i:-1]]
all_arrays[::-1]
all_arrays[-all_arrays_len-1+i:-2-i]

l = [1,2,3]

[arr[0] for arr in all_arrays[-all_arrays_len+1+i : -i : -1]]

all_arrays[0][-2:-i:-1]

list_=[]

all_arrays_len = len(all_arrays)
one_array_len = len(all_arrays[0])

for i in range(int(all_arrays_len/2)):

    list_ += \
    all_arrays[i][:] + \
    [arr[-1] for arr in all_arrays[i+1:all_arrays_len-i]] + \
    all_arrays[-i-1][i+1::-1] + \
    all_arrays[-all_arrays_len+1+i : -i : -1]
    print(list_)
=======


directions = [
    lambda i, j: (i, j+1),
    lambda i, j: (i+1, j),
    lambda i, j: (i, j-1),
    lambda i, j: (i-1, j)
]

array = [[1,2,3,4],
         [4,5,6,7],
         [8,9,10,11],
         [12,13,14,15]]

direction_function = directions[2%4]

def in_matrix(i, j):
    return 0<= i < len(array) and 0<= j < len(array)

def is_visited(i, j):
    return array[i][j] == 0

def snail(array):
    direction_cnt = 0
    return_list = []

    i, j = 0, 0
    return_list.append(array[i][j])

    # visited mark
    array[0][0] = 0

    while True:
        # which way to go?
        direction_function = directions[direction_cnt%len(array)]

        tmp_i, tmp_j = direction_function(i, j)

        # is it time to change direction?
        if (not in_matrix(i, j)) or is_visited(i, j):
            direction_cnt += 1

        else:
            # if still in this direction
            # change the i and j and append the value
            i, j = tmp_i, tmp_j
            return_list.append(array[i][j])

            # then mark it as visited
            array[i][j] = 0

            # is it all in?
            if len(return_list) == len(array)**2:
                return return_list

if __name__ == '__main__':
    print (snail(array))

snail(array)
>>>>>>> 8f65d470e942c03378745bae612228c005e8a5c8




<<<<<<< HEAD
directions = [
    lambda i, j: (i, j + 1),
    lambda i, j: (i + 1, j),
    lambda i, j: (i, j - 1),
    lambda i, j: (i - 1, j),
]

array = [[1,2,3,4],
         [4,5,6,7],
         [8,9,10,11],
         [12,13,14,15]]

def in_matrix(i, j):
    return 0 <= i < len(array) and 0 <= j < len(array)

def is_visited(i, j):
    return array[i][j] == 0


def snail(array):
    direction_cnt = 0
    i, j = 0, 0
    ret = []
    ret.append(array[i][j])
    array[i][j] = 0  # mark as visited
    while True:
        direction_func = directions[direction_cnt % 4]  # turning directions in circle
        tmp_i, tmp_j = direction_func(i, j)  # attempt to head one step
        if (not in_matrix(tmp_i, tmp_j)) or is_visited(tmp_i, tmp_j):  # over border or visted
            direction_cnt += 1  # change direction
        else:
            i, j = tmp_i, tmp_j  # confirm this step
            ret.append(array[i][j])
            array[i][j] = 0  # mark as visited
            if len(ret) == len(array)**2:  # simple terminal criteria
                return ret


if __name__ == '__main__':
    print snail(array)
=======
# complete solution to snail working but timing out

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
    if len(array[0]) == 0: return []
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

        else:
            # if still in this direction
            # change the i and j and append the value
            i, j = tmp_i, tmp_j
            return_list.append(array[i][j])

            # then mark it as visited
            array[i][j] = '0'

            # is it all in?
            if len(return_list) == len(array)**2:
                return return_list



>>>>>>> 8f65d470e942c03378745bae612228c005e8a5c8
