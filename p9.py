def is_pangram(s)



s = 'this is it'

from string import ascii_lowercase
ascii_lowercase
letters_dict = {ascii_lowercase[i]: i for i in range(len(ascii_lowercase))}
"".join( set(sorted([letter for letter in s.lower() if letter.isalpha()])))

def is_pangram(s):
    
    s_letters = "".join(sorted(set([letter for letter in s.lower() if letter.isalpha()])))
    print(s_letters)
    return ascii_lowercase == s_letters

is_pangram(ascii_lowercase)

def is_pangram(s):
    for char in ascii_lowercase:
        if char not in s.lower(): return False
    return True


reversed([1,2,3])




def snail(array):
    results = []
    while len(array) > 0:
        # go right
        results += array[0]
        del array[0]

        if len(array) > 0:
            # go down
            for i in array:
                results += [i[-1]]
                del i[-1]

            # go left
            if array[-1]:
                results += array[-1][::-1]
                del array[-1]

            # go top
            for i in reversed(array):
                results += [i[0]]
                del i[0]

    return results
