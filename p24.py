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
