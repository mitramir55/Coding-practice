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