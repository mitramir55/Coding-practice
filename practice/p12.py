arr = [10, 15, 3, 7]

k = 17

for i in range(len(arr)):

    for j in range(len(arr), 0 , -1):
        print(j)
        if i<j:
            if arr[i] + arr[j] == k:
                print (arr[i], arr[j])

n = 2
arr = [2, 3, 10]

tills_dict = {f'till_{i}': 0 for i in range(n)}
tills_dict

total_sum = 0


def find_min(tills_dict):

    min_till = sorted(tills_dict, key=lambda x:x[1], reverse=True)[0]
    min_ = tills_dict[min_till]

    return min_till, min_

for j in range(len(arr)):
    for i in range(n):

        if tills_dict[f'till_{i}'] == 0: 
            tills_dict[f'till_{i}'] = arr[j]

    min_till, min_ = find_min(tills_dict)
    total_sum += min_

    for i in range(n): tills_dict[f'till_{i}'] -= min_


for j in range(n, len(arr)):
        total_sum += min_
        tills_dict[min_till] = 0
        if tills_dict>1:
            for m in range(len(arr))


dict_ = {'small':1, 'big':20 ,'middle':10}
sorted(dict_, key=lambda x:x[1], reverse=True)[0]

tills_dict = {'till_0': 2, 'till_1': 1, 'till_2': 2, 'till_3': 3, 'till_4': 4}
min_till = sorted(tills_dict.items(), key=lambda x:x[1], reverse=True)
min_ = tills_dict[min_till]
min_
min_till

min_till, min_ = sorted(tills_dict.items(), key=lambda x:x[1])[0]
min_till
n=2
l = n*[0]
l.index(min(l))

# n * k = 89
n = 89
ds = [int(i) for i in str(d)]
ds

# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

k = 1
n = 89
def funct(n, p):
    
sum([d**i for i in range(len())])



