import string
string.ascii_lowercase

string.ascii_letters

letters_list = list(string.ascii_lowercase)


letters_dict = {}
for i in range(len(letters_list)):
    letters_dict[letters_list[i]] = i 


reverse_letters_dict = {v: k for (k, v) in letters_dict.items()}
reverse_letters_dict
letters_dict


def rot13(word):
    new_letters_list = []
    ref_word_list = list(word)

    for letter in ref_word_list:
        print(letter)
        
        # NaL = not a letter
        try:
            num = letters_dict[letter.lower()]
        except: 
            num = 'NaL'
            print('nal')

        # append the main item found if it's not a letter
        if num == 'NaL':
            new_letters_list.append(letter)

        # append the new letter if it is a letter

        else:
            if num>12: 
                new_letter = reverse_letters_dict[num%13]
            else: 
                new_letter = reverse_letters_dict[num+13]

            if letter.isupper():new_letter = new_letter.upper()

            new_letters_list.append(new_letter)

    return "".join(new_letters_list)

rot13('m, to')



# better solution

import string
from string import ascii_lowercase, ascii_uppercase

def rot13(message):
    lower = str.maketrans(ascii_lowercase, ascii_lowercase[13:] + ascii_lowercase[:13])
    upper = str.maketrans(ascii_uppercase, ascii_uppercase[13:] + ascii_uppercase[:13])
    return message.translate(lower).translate(upper)

lower = str.maketrans(ascii_lowercase, ascii_lowercase[13:] + ascii_lowercase[:13])
'ak'.translate(lower)

ascii_lowercase[13:] + ascii_lowercase[:13]

ascii_lowercase[13:] + ascii_lowercase[:13]
<<<<<<< HEAD

=======
import string
string.ascii_lowercase

import string



all_letters = string.ascii_lowercase
alphabet_dict = {}
for i in range(1, len(all_letters)+1): 
    alphabet_dict[all_letters[i-1]] = i




        
import string

all_letters = string.ascii_lowercase
alphabet_dict = {}
for i in range(1, len(all_letters)+1): 
    alphabet_dict[all_letters[i-1]] = i

        
        
def alphabet_position(text: str) -> str:
    numbers_list = []
    
    for letter in text:
        
        if letter.lower() in alphabet_dict.keys(): 
            
            number_str = str(alphabet_dict[letter.lower()])
            numbers_list.append(number_str)
        
    return " ".join(numbers_list)

ord('b')

def alphabet_position(text:str) ->str:
    return " ".join(str(ord(letter)-96) for letter in text if letter.isalpha())
alphabet_position(
    'miti'
)
>>>>>>> 6877b48ddcc849f6d76fc0fa784aa03416766dcb
