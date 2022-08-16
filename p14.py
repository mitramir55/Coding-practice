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
