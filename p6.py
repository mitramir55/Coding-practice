from multiprocessing.reduction import duplicate
from os import times
from string import ascii_lowercase


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
import string
letters = string.ascii_lowercase 
letters_dict = {letters[i]:i+1 for i in range(len(letters))}

def alphabet_position(phrase:str) ->str:

    return " ".join([letters_dict[token] for token in phrase.lower() if token.is_alpha()])


def bouncing_ball(h, bounce, window):

    if h< window:
        return -1
    else:
        times_seen = 1
        while h> window:
            bouncing_heigh = bounce * h
            if bouncing_heigh > window:
                times_seen += 1

    return times_seen


def bouncing_ball(h, bounce, window):
    
    # check height
    if h < window: return -1
    if h < 0: return -1

    # check 0 < bounce<1
    if bounce > 1: return -1
    if bounce <0: return -1

    times_seen = 1
    bouncing_heigh = bounce * h

    while bouncing_heigh > window:
        times_seen += 2
        bouncing_heigh = bounce * bouncing_heigh

    return times_seen


bouncing_ball(30, 0.75, 1.5)
