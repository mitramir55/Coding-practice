p = 'UFFDDFDUDFUFUUFFDDFDUDFUFU'
import regex  as re

def counting_valleys(p): 

    in_valley = False
    n_valley = 0
    base = 0

    #dir_dict = {}
    for d in p: 

        # add if going up
        # decrease if going down
        if d == 'U': base += 1
        elif d == 'D': base -= 1

        # if we've gone down
        if not in_valley and base < 0:
            in_valley = True
            n_valley += 1

        # if we reached level 0
        if in_valley and base == 0:
            in_valley = False

    return n_valley

counting_valleys(p)

from itertools import permutations


s = 'dsfdsf'
ret_l = []
indices = list(range(len(s)))

indices
idx_perms = list(permutations(indices))

for idx in idx_perms:
    ret_l.append(''.join([s[i] for i in idx]))

set(ret_l)



from math import sqrt, ceil

ceil(1.0000000000000000006)

n = 3
list(range(n * (n-1) + 1, n * (n+1), 2))




grid = [['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']]

import numpy as np

np.array(grid).ravel()
# .reshape(1, -1)

sum(grid, [[1]])



import itertools

list(itertools.chain.from_iterable(grid))

list_ = [[[2],[3],[4]]]
list(itertools.chain.from_iterable(list_))

li=['123', '456', '789']

sum( int(i) for i in list(itertools.chain.from_iterable(li)))


list(itertools.chain.from_iterable([[[1, 23]]]))