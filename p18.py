from fnmatch import translate
import string


import string
from string import ascii_lowercase, ascii_uppercase
's'.translate('s'.maketrans())

len(string.ascii_lowercase)
string.ascii_uppercase

new_alphabet = ascii_lowercase[2:] + ascii_lowercase[:2]
txt = 'this is '
txt.translate(txt.maketrans(ascii_lowercase, new_alphabet))

import regex as re 

re.findall('\(', txt)

re.findall('\)', txt)

txt = 'hi(hi)'
with_par = re.findall(r'.*[\(\)].*', txt)
with_par


re.findall(r'.*\(*.*\).*', txt)

re.findall(r'\(+.*\)+', txt)[0] == re.findall(r'.*\(*.*\).*', txt)[0]
with_par.count('(') == with_par.count(')')

if re.findall(r'\(*.*\)*', txt):

txt.find('(')
    open_idx
txt.index('(')


import regex as re
def valid_parentheses(txt):
    
    if txt=='': return True
    
    open_close_span = re.findall(r'\(+.*\)+', txt)
    all_pars = re.findall(r'.*[\(\)].*', txt)
    
    # fist make sure all parantheses in text are open close
    # so we don't get an open paranthesis at the end
    if open_close_span == all_pars and open_close_span: 
        open_close_span = open_close_span[0]
        
        # there might be something like (jisd()
        # so we count the open and close pars
        return open_close_span.count('(') == open_close_span.count(')')
    
    else: return False









txt_list = list(txt)
close_idx = txt.rfind(')')
open_idx = txt.find('(')

for _ in range(len(txt)//2):

    txt_list = list(txt)
    print(txt)
    close_idx = txt.rfind(')')
    open_idx = txt.find('(')
    print(close_idx)

    if close_idx > open_idx:

        txt_list[close_idx] = ''
        txt_list[open_idx] = ''

        txt = "".join(txt_list)
txt
if re.findall(r'\(', txt) == None: return True


a = -8
int(a/5)
if a%5==0: res = a

if a>0: m = int(a/5) + 1
else: m = int(a/5)

res = 5 * m
res

a = - 16
a + (5 - a) % 5
a = 6
-6%5
a + (-a)% 5

'scissors paper rock lizard spock scissors lizard paper spock rock scissors'



sum_ = 0
# 
int(biggest_p)

binary_l = []

i = 0
num = 12
i = int(num ** (1/2))
i

while num > 0 and i >= 0:
    num -= 2**i
    binary_l.append(i)
    print(i)
    i -= 1

binary_l
binary_placeholder = [0] * (max(binary_l)+1)
binary_placeholder
binary_placeholder[binary_l] = 1

for i in binary_l:
    binary_placeholder[i] = 1
binary_placeholder.reverse()
"".join(str(i) for i in binary_placeholder)

int('12', 2)


bin(12)[2:]
bin(-12)
bin(12)



recipe = {'fjad': 562, 'dsfjk': 656, 'dslkfj': 555}
available = {'fjad': 2, 'dsfjk': 656, 'dslkfj': 555}

[available.get(item, 0)/val for item, val in recipe.items()]


# one space for chars
# three for words
# strip the text and ignore them
"".format(255, 165, 1)
"{:02x}".format(55)

"#{0:02x}{1:02x}{2:02x}".format(255, 165, 1)


def helper(c_count, i, nums_l):

    res = []    

    # if only two numbers were consec
    if c_count == 1: res = [str(nums_l[i-1]), str(nums_l[i])]
    
    # if more than two were consec
    elif c_count >= 2: res = [str(nums_l[i-c_count]) + '-' + str(nums_l[i])]

    return res


def solution(nums_l):
    
    # c_count counts the number of successive integers
    ret_l = []
    c_count = 0

    for i in range(len(nums_l)-1):
        
        # check if the numbers are consecutive
        if nums_l[i] + 1 == nums_l[i+1]:
            c_count += 1
                
        if i == len(nums_l) -2:
            res = helper(c_count, i+1, nums_l)
            ret_l += res

        if nums_l[i] + 1 != nums_l[i+1]:
            
            # ----
            # then if none is true, continue adding numbers to the ret_l
            ret_l.append(str(nums_l[i]))
            if i == len(nums_l) - 2: ret_l.append(str(nums_l[i+1]))
            c_count = 0
        

    return ret_l


a = [1,2,4]   
a.append([1,4])
a        
test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')