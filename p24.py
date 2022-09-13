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



def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    dict = {'(' : ')', '[' : ']', '{' : '}'}
    stack = []
    for i in s:
        if i in dict.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            a = stack.pop()
            if i!= dict[a]:
                return False
    return stack == []


s = '{(})'
isValid(s)


def is_valid_2(s):

    par1 = {'{': 1, '}': -1, 'count': 0}
    par2 = {'[': 1, ']': -1, 'count': 0}
    par3 = {'(': 1, ')': -1, 'count': 0}


    for k in s:

        if k in par1:
            par1['count'] += par1[k]
            if par1['count'] < -1: return False

        elif k in par2:
            par2['count'] += par2[k]
            if par2['count'] < -1: return False

        elif k in par3:
            par3['count'] += par3[k]
            if par3['count'] < -1: return False

    # "{{}"
    if par1['count'] > 0 or par2['count'] > 0 or par3['count'] > 0:
        return False

    return True

s = "([)]"
is_valid_2(s)