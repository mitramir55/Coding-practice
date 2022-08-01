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
        
        num = letters_dict[letter]
        if num>12: 
            new_letter = reverse_letters_dict[num%13]
        else: 
            new_letter = reverse_letters_dict[num+13]

        new_letters_list.append(new_letter)

    return "".join(new_letters_list)

rot13('m')