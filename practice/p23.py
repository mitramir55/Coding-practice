import string
string.ascii_lowercase
ord('.')

import itertools
itertools.combinations(['+', '*'])

m = 1
n = 1
k = 1

max(max(eval( f'( {a} {op1} {b}) {op2} {c}') , eval(f' {a} {op1} ({b} {op2} {c} )')) for op1 in '+*' for op2 in '+*' for a in [m, n, k] for b in  [m, n, k] for c in [m, n, k])


max(max(eval(f'{a}{op1}({b}{op2}{c})'), eval(f'({a}{op1}{b}){op2}{c}')) for op1 in '+*' for op2 in '+*')

import regex as re
re.findall('[1-9]', '255')

st = 'sdfsdf. fdsfs'

all(sec.isdigit() and str(int(sec)) for sec in st.split('.'))














import regex as re


# True
'46652'.isdigit()

# False -> + not
re.match('^0\d+', '05')

# IP validation
def validate(s):
    return s.count('.') == 3 and all(sec.isdigit() and re.match('^0\d+', sec)==None and -1 < int(sec) < 266 for sec in s.split('.'))

validate('1.1.1.06')



alphabet_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

from collections import Counter
Counter({'red': 4, 'blue': 2}) 
Counter('56255')

powers_dict = {'2':0, '5':0}
n = 100:

for i < n:
    num = i
    while num % 2 == 0:
        powers_dict['2'] += 1
        num /= 2

    while num % 5 == 0:
        powers_dict['5'] += 1
        num /= 5
    i += 1

    return min(powers_dict.values())


