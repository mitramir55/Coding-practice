len('this') == len(set('this'))

s = 'abcbc'

# {'a':0, 'b':1, ...}
letters_dict = {}
left = 0
res = s

for i in range(len(s)):
    if s[i] in letters_dict:
        left = i

    letters_dict[s] = i
    if left !=i and s[left:i] < res:
        res = s[left:i]

res
ord('a')