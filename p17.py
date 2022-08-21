input_ = 12
rev = str(input_)
i = 0
ret_str = ''
len_digit = len(str(input_))

for i in range(0, len_digit)[::-1]:
    print(i)
    d = int(rev[i]) * 10**i
    if i!=0: ret_str += str(d) + ' + '
    else: ret_str += str(d)
ret_str


input_ = 123

# 123 -> '321'
input_s = str(input_)[::-1]

res_str = ''

for i in range(len(input_s)):

    curr_d = input_s[i]

    if curr_d==0: continue

    if i == 0: 
        # res_str = '3'
        res_str = curr_d
    else: 
        # '20 + 3'
        res_str = str(int(curr_d) * 10**i) + ' + ' + res_str

res_str


# without walrus
n = 20
if n > 10:
    print(f"{n} is greater than 10")

# with walrus
if (n := 30) > 10:
    print(f"{n} is greater than 10")