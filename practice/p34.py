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

            for j in range(1, len(s)+1):
                print('j = ', j)
                print('s[i:j] = ', s[i:j])
                palindromes = all_palindroms(s[i:j])
                if palindromes:
                    print('palindromes = ', palindromes)
                    for suffix in palindromes:
                        res_list.append(suffix)

    return res_list

all_palindroms('abc')


from functools import cache

@cache
def palindrom_substrings_2(s:str) -> list[list]:
    ret_list = []
    if not s: return []

    for i in range(1, len(s) + 1):
        if s[:i] == s[:i][::-1]:
            ret_list .append(s[:i])

            for suffix in palindrom_substrings_2(s[i:]):
                ret_list.append(suffix)
    return ret_list


palindrom_substrings_2('aaa')


def palindrome_parts(s:str) ->list[list[str]]:
    """
    "aab" -> [[a, a, b], [aa, b]]
    """
    stack = []
    res = []
    def dfs(i:int):
        """
        i : index of where we're at when partitioning the string
        """
        print()
        print('i = ', i)
        if i == len(s):
            print('finished stack = ', stack.copy())
            res.append(stack.copy())
            return

        for j in range(i+1, len(s)+1):
            print('j = ', j)
            if s[i:j] == s[i:j][::-1]:
                print('stack before append = ', stack)

                stack.append(s[i:j])
                print('stack after append = ', stack)

                dfs(j) # j = len(s)
                print('stack after dfs = ', stack)

                stack.pop()
                print('stack after pop = ', stack)
    dfs(0)
    return res


palindrome_parts('aab')






# count palindromes

def is_palindrom(s):
    return s == s[::-1]


def palindrome_count(s:str) -> int:

    count = 0
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if is_palindrom(s[i:j]): count += 1
    return count

palindrome_count('aab')

'aab'.pop()

def compressed_form(s):
    letter, res, init_s = '', '', s
    count, ones_c = 0, 0

    for _ in range(len(init_s)+1):
        print()
        if not s:
            res = str(count) + letter + res
        elif not letter:
            letter = s[-1]
            count += 1
        else:
            if letter == s[-1]:
                count +=1
                print('count = ', count)
            else:
                res = str(count) + letter + res
                if count == 1: ones_c += 1
                count, letter = 1, s[-1]
        
        s = s[:-1]
        print('s = ', s)
        print('count = ', count)
    
    return init_s if ones_c == len(init_s) else res
from time import time

start = time()
compressed_form('aabb')
end = time()

print(start - end)


def strCompress(string):
    compressed = []
    lastchar = "" 
    charcount = 0
    for char in string:
        if char == lastchar:
            charcount += 1
        else:
            if lastchar != "":
                compressed.append(lastchar+str(charcount))
            lastchar = char
            charcount = 1
    compressed.append(lastchar+str(charcount)) #append the last character
    compressedStr = ''.join(compressed)  # join the list into a string
    if len(compressedStr)<len(string):
        return compressedStr
    else:
        return string
        

start = time()
strCompress('aabb')
end = time()

print(start - end)

n = 3
nums = [1, 2, 3, 4, 5]
nums_ = nums[-n:]
nums_.reverse()
nums_ + nums[n+1:]



class Solution:
    
    def countSubstrings(self, s: str) -> int:
        if not s: return 0

        def count_palindromes(r, l)->int:
            c = 0
            while l >= 0 and r < len(s):
                if s[l] == s[r]: 
                    c += 1
                    l, r = l-1, r+1
                else: break
            return c

        count = 0
        for i in range(len(s)):
            # odd lengthed strings
            l, r = i, i
            count += count_palindromes(r, l)

            # even lengthed strings
            l, r = i, i + 1
            count += count_palindromes(r, l)

        return count



matrix =  [[1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5], 
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]]

import numpy as np
np.rot90(matrix, -1)
matrix



def rotate_90(matrix):

    n = len(matrix)

    matrix_2 = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):

            matrix_2[j][n - 1 - i] = matrix[i][j]

    return matrix_2
rotate_90(matrix)

matrix = np.rot90(matrix, -1)


matrix



def rot(matrix: list[list]):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]





    n = len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)//2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]




type(matrix)


matrix =  [[0, 10, 20, 30, 40],
            [1, 100, 120, 130, 140],
            [1, 2, 3, 4, 5], 
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]]
            
def set_zero(matrix:list[list]):
    n = len(matrix)
    zero_cols = []

    for i in range(n):
        for j in range(n):

            if matrix[i][j] == 0:
                zero_cols.append(j)
                matrix[i] = [0] * n
                break

    for j in zero_cols:
        for i in range(n):
            matrix[i][j] = 0


for row in range(len(matrix)):
    print(matrix[row])


s1 = "erbottlewat"
s2 = "waterbottle"

def is_rotation(s1, s2):
    # is s2 a rotation of s1
    l = 0

    # l = 3
    while l < len(s1):
        if s1[0] == s2[l]:
            if s2[l:] + s2[:l] == s1:
                return True
        l += 1
    return False


is_rotation(s1, s2)

def is_rotation(s1:str, s2:str)->bool:

    if len(s1) == len(s2) != 0:
        if s1 in s2 * 2:
            return True
    return False








from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # define two pointers
        # fast goes n steps at a time to read the end
        # slow will be the one before the nth from the end
        # slow_temp is the one at nth from the end
        slow_temp, fast = head, head

        while fast:
            slow_temp = slow_temp.next
            for _ in range(n):
                try:
                    fast = fast.next
                except:
                    fast = None
                    break

            # slow will be the node before the one that is n steps from the
            # last node
            if fast:
                slow = slow_temp
        
        slow.next = slow.next.next

        return head