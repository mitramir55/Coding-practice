from audioop import mul


n = 12

len(list(range(0, n, 5)))
12//5

multi = 1

n = 25
powers = 0
max_power = n // 5
i = 1
while 5**i <= n:
    powers += n // (5 ** i)
    i += 1
powers



for i in range(1, 26):
    multi *= i
    i += 1

multi
25//5


from collections import Counter

Counter('this') == Counter('sith')

sorted('sith')

f=lambda c: c.upper()

s = 'fdf'
list(map(f, s))
callable(f)
import regex as re

s = '3D2a5d2f'
patterns = re.findall('\d[a-zA-Z]+', s)
re.match('\d', '5d6g').group()

i = 0
final_str_list = []
for sec in patterns:
    print(f'{i}')
    i += 1
    print(sec)
    digit = int(re.match('\d', sec).group())
    letters = re.findall('[a-zA-Z]+', sec)[0]

    ret_str = ''
    for letter in letters:
        ret_str += letter * digit
    
    final_str_list.append(ret_str)

"".join(final_str_list)
re.match('[a-z]', '5fl')#.group()

re.findall('[a-zA-Z]+', '5fl')#.group()

s = 'sdf5d8fd6sdf'
starts_with = re.match('^[a-zA-Z]+', s)
if not starts_with:

    print('yes')



nums = [1,2,3,5,6,]
for j in range(len(nums)-1, -1, -1):
    print(j)


def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)-1, -1, -1):
                if i < j: 
                    if nums[i] + nums[j] == target: return [i, j]
twoSum(nums, 6)


def isValid(s: str) -> bool:
    return True if not s.translate(str.maketrans("", "", '()[]{}')) else False

isValid(s='[]()')

"{{{{}}})"