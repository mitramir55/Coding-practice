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