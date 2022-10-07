def move_zeros(nums):
    zero_length = len(nums) - len([num for num in nums if num!=0])
    return nums.append([0] * zero_length)

zeros_idx = []
for i, k in enumerate(nums):
    if k==0: zeros_idx.append(i)
for i in zeros_idx.reverse():
    del nums[i]

nums += len(zeros_idx) * [0]

for i in l.reverse():
    print(i)

nums = [1, 2, 3, 0, 5]
n = len(nums)
count = 0

for i in range(n-1, -1, -1):
    print(i)
    if nums[i] == 0:
        del nums[i]
        count += 1

nums += count * [0]

nums

for i in range(n, -1, -1):
    print(i)


s1 = "abc"
s2 = "cbaebabacd"

from collections import Counter

def find_anagram(s1, s2):

    cnt = Counter(s1)
    match = 0
    s1_set = set(s1)
    all_indices = []

    for i, k in enumerate(s2):
        if k in s1_set:
            cnt[k] -= 1
            if cnt[k] == 0: match += 1

        if i >= len(s1) and s2[i - len(s1)] in s1_set:
            if cnt[s2[i- len(s1)]] == 0: match -= 1
            cnt[s2[i- len(s1)]] -= 1

        if match == len(s1):
            all_indices.append(i-len(s1))

    return all_indices


def is_palindrom_permutation(s:str):
    chars_map = {}
    for k in s.lower():
        if k != ' ': 
            chars_map[k] = chars_map.get(k, 0) + 1

    # pythonic: 
    # from collections import Counter
    # chars_map = Counter(s)
    return len([1 for (k, v) in chars_map.items() if v % 2 == 1]) <= 1

is_palindrom_permutation(s = 'tact coea')
