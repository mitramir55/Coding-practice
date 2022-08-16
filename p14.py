
from unicodedata import digit
import regex as re
string_ = 'foo001'

def func(string_):
    letters_str = re.findall('\w+', string_)[0] 
    digits_str = re.findall('\d+$', string_)[0]

    # have zero in the beginning?
    zeros = re.findall('^0+', digits_str)

    if not zeros:
        final_digit_str = str(int(digits_str)+1)
    else:
        # create an all zero str 
        initial_d = ['0']*len(digits_str)

        # the non-zero part
        non_zero_nums = int(re.findall('[1-9]+', digits_str)[0])
        non_zero_nums += 1

        # convert int to a list of numbers as strings
        non_zero_nums_str = list(str(non_zero_nums))
        len_non_zero = len(non_zero_nums_str)


        # substitute zeros at the end with non-zero str
        initial_d[-len_non_zero:] = non_zero_nums_str
        final_digit_str = "".join(initial_d)

    ret_str = letters_str + final_digit_str
    return ret_str
    



re.findall('^[1-9]', '0011')

str_ = 'fjksdljfkds8768678'
letters = str_.rstrip('0123456789')
digits = str_[len(letters):]
digits

if digits=='': ret_str = str_ + '1'
else: ret_str = letters + str(int(digits) + 1).zfill(len(digits))
'298'.zfill(8)

def cal(principle, interest_rate, tax_rate, goal):
    i = 0
    while principle < goal: 
        interest = principle * interest_rate
        tax = interest * tax_rate
        principle = principle + interest - tax
        i+=1

    return i



'h'.swapcase()




# seven(times(five())) # must return 35

one(plus(two))

def one():
    return 1
def seven():
    return 7

# functions ------------
def plus(b):
    return lambda a : a + b

def divided_by(b):
    return lambda a : a // b

def minus(b):
    return lambda a : a - b

def times(b):
    return lambda a : a * b

# numbers ----------------
def one(*functs):
    return 1 if len(functs)==0 else functs[0](one())

def seven(*functs):
    return 7 if len(functs)==0 else functs[0](seven())


funct_ = times(seven())
one(times(seven()))
funct_(seven())


inside = plus(one())
inside(seven())


plus(one())
# plus(1) - > a + 1


def one(*funct):
    return 1 if len(funct)==0 else funct(1,)



