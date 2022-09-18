def is_pangram(s)



s = 'this is it'

from string import ascii_lowercase
ascii_lowercase
letters_dict = {ascii_lowercase[i]: i for i in range(len(ascii_lowercase))}
"".join( set(sorted([letter for letter in s.lower() if letter.isalpha()])))

def is_pangram(s):
    
    s_letters = "".join(sorted(set([letter for letter in s.lower() if letter.isalpha()])))
    print(s_letters)
    return ascii_lowercase == s_letters

is_pangram(ascii_lowercase)

def is_pangram(s):
    for char in ascii_lowercase:
        if char not in s.lower(): return False
    return True


reversed([1,2,3])




def snail(array):
    results = []
    while len(array) > 0:
        # go right
        results += array[0]
        del array[0]

        if len(array) > 0:
            # go down
            for i in array:
                results += [i[-1]]
                del i[-1]

            # go left
            if array[-1]:
                results += array[-1][::-1]
                del array[-1]

            # go top
            for i in reversed(array):
                results += [i[0]]
                del i[0]

    return results


# practicing and learning the fundamentals


import numpy as np

def find_uniq(arr):
    unique_values = list(set(arr))
    
    count_dict = {unique_values[i]: arr.count(unique_values[i]) for i in range(len(unique_values))}

    return [k for k, v in count_dict.items() if min(count_dict.values()) == v][0]

arr = [ 1, 1, 1, 2, 1, 1 ]

find_uniq(arr)

a, b = set(arr)

set(arr)

n = 6

len_ = n*2-1

list_ = [' ' * len_] * n
list_
print(len_)
len(list_)


for i in range(0, len_-2):
    print("\ni = ", i)
    print('start: ', int(len_/2)-i)
    print('end: ', int(len_/2)+i)
    str_list = list(list_[i])
    print('raw str_list = ', str_list)

    start = int(len_/2)-i
    end = int(len_/2)+i -1
    n_stars = end - start + 1

    str_list[start: end] = "*" * n_stars
    print('str_list = ', str_list)
    str_ = "".join(str_list)
    list_[i] = str_

    print(list_)
list_
"*" * (10 - 5)

str_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

str_list[1:3] = '*'*2
str_list

len('           ')


def likes(names):

    n = len(names)
    return {
        0: 'no one lies this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} like this'
    }[min(n, 4)]*format(names[:3], others=n-2)

likes(names)