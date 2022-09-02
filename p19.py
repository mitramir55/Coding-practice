import datetime
str(datetime.timedelta(seconds=666))


intervals = [
    ('year', 60 * 60 * 12 * 365),
    ('day', 60 * 60 * 12),
    ('minute', 60 * 60),
    ('second', 60)
]

5 // 360

def get_plural_s(t):
    return 's' if t > 1 else ''

seconds = 500000
dict_ = {}
plural = False

for inter, val in intervals:
    res = seconds // val

    if res != 0:
        if res > 1: p = get_plural_s(res)
        seconds = seconds % val
        dict_[inter + p] = res



dict_
all_l = []
for k, v in dict_.items():
    all_l += [k, v]

ret_dict = {
    0: 'now',
    1: '{} {}',
    2: '{} {} and {} {}',
    3: '{} {}, {} {} and {} {}',
    4: '{} {}, {} {}, {} {} and {} {}'
}[len(dict_)].format(*all_l[::-1])


ret_dict
all_l

*all_l

all_l
dict_.items()


'fdsf'.split()

count_dict = {1:5, 5:0}
any(map(count_dict.values(), 0))
map(count_dict.values(), 0)

sum(1 for i in count_dict.values() if i==0 or i>1)


 arr = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
        [4, 9, 8, 2, 6, 1, 3, 7, 5],
        [7, 5, 6, 3, 8, 4, 2, 1, 9],
        [6, 4, 3, 1, 5, 8, 7, 9, 2],
        [5, 2, 1, 7, 9, 3, 8, 4, 6],
        [9, 8, 7, 4, 2, 6, 5, 3, 1], 
        [2, 1, 4, 9, 3, 5, 6, 8, 7], 
        [3, 6, 5, 8, 1, 7, 9, 2, 4], 
        [8, 7, 9, 6, 4, 2, 1, 3, 5]]

def is_valid(arr):        

    correct = list(range(1,10))
    
    for row in arr:
        if row != correct: return False

    cols = list(zip(*arr))
    for col in cols:
        if col != correct: return False

    for i in range(0, 8, 3):
        # 0, 3, 6
        for j in range(0, 8, 3):
            matrix = [x[i:i+3] for x in arr[j:j+3]]
[*arr]
arr.reshape(-1, 1)

# i = [0, 9]


for i in range(10):
    
    hori_dict = {}
    vert_dict = {}

    for j in range(10):
        hori_val = arr[i][j]
        verti_val = arr[j][i]

        hori_dict[hori_val] = hori_dict.get(hori_val, 0) + 1
        vert_dict[verti_val] = vert_dict.get(hori_val, 0) + 1

    if sum(1 for i in vert_dict.values() if i==0 or i>1) or sum(1 for i in hori_dict if i==0 or i>1): return False
return True