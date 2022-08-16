def funct_(prod):

    a = 1
    b = 1
    while a * b <=prod:
        prod_temp = a*b
        if prod_temp==prod:
            return [a, b, True]
        else:
            a, b = b, a+b
    return [a, b, False]

funct_(6)