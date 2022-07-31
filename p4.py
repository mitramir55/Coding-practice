def square_digits(num):
    print( "".join(str(int(digit)**2) for digit in list(str(num))))


square_digits(9119)

for i in map(int, str(520)):
    print(i)