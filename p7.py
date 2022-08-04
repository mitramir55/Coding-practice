word = 'this'
word[::-1]
word[-1]

def pig_it(text):
    words_list = []

    for word in text.split(" "):
        final_word = word

        if not word.isalpha(): 
            words_list.append(word)
            continue

        if len(word)>=2:
            final_word[0] = word[-1]
            final_word[-1] = word[0]

        final_word =+ 'ay'
        words_list.append(final_word)
        return " ".join(words_list)

'miti'[-1]





def pig_it(text):
    words_list = []

    for word in text.split(" "):

        if not word.isalpha(): 
            words_list.append(word)
            continue

        if len(word)>=2:
            letters = list(word)
            final_word_letters = letters[:-1]
            print(final_word_letters)
            final_word_letters = final_word_letters.insert(0, 'n')
            print(final_word_letters)

        final_word = "".join(final_word_letters) + 'ay'
        words_list.append(final_word)
        
    return " ".join(words_list)
pig_it('moto')