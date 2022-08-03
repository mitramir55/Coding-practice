def duplicate_encode(word):
    for letter in word:
        
letters_dict = {}

final_word = ''
for letter in word:
    if dict_.get('g'): 
        final_word+=')'
    else:
        final_word+='('
        dict_[letter] = 1

dict_ = {'t':5}
print(dict_.get('g'))

def duplicate_encode(word):
    final_word = ''
    dict_ = {}
    for letter in word:
        if dict_.get('g'): 
            final_word+=')'
        else:
            final_word+='('
            dict_[letter] = 1
            
    return final_word


duplicate_encode(word='this is')


# NOTE: READ THE QUESTION AND THE EXAMPLES COMPLETELY!!!

def duplicate_encode(word):
    return "".join(['(' if word.lower().count(letter)==1 else ')' for letter in word.lower()])


duplicate_encode(word='recede ')