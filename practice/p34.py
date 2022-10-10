from re import sub
import string


def is_one_edit_away(s1:str, s2:str) -> bool:
    """
    determines if two strings are different by less than two edits.
    cat -> mat : True
    cat -> matt: False
    """
    if abs(len(s1) - len(s2)) > 1: return False
    char_map = [0] * 128
    for k in s1:
        idx = ord(k)
        char_map[idx] += 1
    for k in s2:
        idx = ord(k)
        char_map[idx] -= 1

    # more than two because we're ok with each having one different letter
    if sum(abs(i) for i in char_map) > 2: return False
    return True

is_one_edit_away('mat', 'catt')




def one_way_equal_lens(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if count > 1: return False
    return True

def one_edit_diff_lens(s1, s2):

    # if length wise s2 > s1
    count = i = 0
    while i < len(s1):
        if s2[i + count] == s1[i]:
            i += 1
        else:
            count += 1
            if count > 1: return False
    return True

def is_one_edit_away(s1:str, s2:str) -> bool:

    len_1 = len(s1)
    len_2 = len(s2)

    if abs(len_1 - len_2) > 1: return False

    if len_2 > len_1: return one_edit_diff_lens(s1, s2)
    elif len_2 < len_1: return one_edit_diff_lens(s1, s2)
    else: return one_way_equal_lens(s1, s2)

is_one_edit_away('mat', 'cat')


def decode(s:str) -> str:
    """
    3[a2[bc]] -> a bcbc a bcbc a bcbc
    """
    stack = []
    for i in range(len(s)):

        if s[i] != ']':
            stack.append(s[i])
        else:

            # taking care of the [string]
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr

            # remove the opening parenthesis
            stack.pop()
            # substr -> "bc"

            # taking care of the digit before []
            digit = ""
            while stack and stack[-1].isdigit():
                digit = stack.pop() + digit
            digit = int(digit)

            stack.append(digit * substr)
    return stack

decode(s = '3[a2[bc]]')



def is_one_edit_away(s1:str, s2:str):
    """
    "mat" and "cat" -> True
    "matt" and "cat" -> False
    """
    if abs(len(s1) - len(s2)) > 2: return False

    char_arr = [0] * 128
    for letter in s1:
        index = ord(letter)
        char_arr[index] += 1
    for letter in s2:
        index = ord(letter)
        char_arr[index] -= 1
    return  (abs(i) for i in char_arr) < 2


def is_one_away_diff_lens(s1, s2):
    """
    len(s2) > len(s1)
    "cat" and "caat"
    """
    count, i = 0, 0
    while i < len(s1):
        if s1[i+count] == s2[i]:
            i += 1
        else:
            count += 1
            if count > 1: return False
    return True

def is_one_away_equal_lens(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if count > 1: return False
    return True


def is_one_edit_away_2(s1:str, s2:str):
    """
    "mat" and "cat" -> True
    "matt" and "cat" -> False
    """
    if abs(len(s1) - len(s2)) > 2: return False
    if len(s2) > len(s1):
        return is_one_away_diff_lens(s1, s2)
    elif len(s1) > len(s2):
        return is_one_away_diff_lens(s2, s1)
    else:
        return is_one_away_equal_lens(s1, s2)


is_one_edit_away_2("cat", "matt")








def is_palindrom(s):
    return s == s[::-1]

from functools import cache


@cache
def all_palindroms(s:str) -> list[str]:
    """
    "aab" -> ["a", "b", "aa"]
    """
    res_list = []

    if s=='': return 

    print()
    for i in range(1, len(s)+1):
        print('i = ', i)
        if is_palindrom(s[:i]):
            print('s[:i] = ', s[:i])
            res_list.append(s[:i])

        for j in range(i+1, len(s)+1):
            print('j = ', j)
            print('s[i:j] = ', s[i:j])
            palindromes = all_palindroms(s[i:j])
            if palindromes:
                print('palindromes = ', palindromes)
                for suffix in palindromes:
                    res_list.append(suffix)

    return set(res_list)

all_palindroms('abc')