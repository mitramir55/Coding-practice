def square_digits(num):
    print( "".join(str(int(digit)**2) for digit in list(str(num))))


square_digits(9119)

for i in map(int, str(520)):
    print(i)

def create_dict(word):
    word_letters = list(word)
    counts = dict()

    for letter in word_letters:
        counts[letter] = counts.get(letter, 0) + 1
        
    return counts

def anagrams(word, words):

    accepted_words = []
    reference_dict = create_dict(word)

    for candidate in words:
        counts_dict = create_dict(candidate)
        if reference_dict == counts_dict:accepted_words.append(candidate) 

    return accepted_words

anagrams(word='mitikoman', words=['miti', 'moto', 'mtiikoman'])

sorted('mitikoman')