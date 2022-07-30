def digital_root(n):
    n_str = list(str(n))
    print(n_str)
    sum_ = 0
    
    for i in n_str:
        sum_ += int(i)
    return sum_
    
2%10



def digital_root(n):
    sum_ = 0
    n_str = list(str(n))
    print(n_str)
    
    while sum_%10!=sum_ or sum_==0:
        for i in n_str:
            sum_ += int(i)
        
    return sum_
    
len(150)
digital_root(29)    




def digital_root(n):
    
    number = n
    
    while len(str(number))>1 or number == n:
        numbers = [int(i) for i in list(str(number))]
        number = sum(numbers)
        
    return number

digital_root(493193)

29 % 100

10**0 * 9 + 10**1 * 2
529//100

sum(map(int, str(529)))