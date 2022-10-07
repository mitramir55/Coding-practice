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


{1,2,3}


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        n = len(s)
        visited = set()


        letters_dict = {}
        for i in range(n): letters_dict[s[i]] = i

        for i in range(n):
            if s[i] not in visited:
                while stack and stack[-1] > s[i] and letters_dict[stack[-1]] > i:
                    visited.remove(stack.pop()) 

                stack.append(s[i])
                visited.add(s[i])

        return "".join(stack)






def unique_letters(s:str):

    n = len(s)
    map_ = {s[i]: i for i in range(n)}
    stack = []
    visited_set = set()

    for i in range(n):
        if s[i] not in visited_set:
            while stack and stack[-1] > s[i] and map_[stack[-1]] > i:
                stack.remove(visited_set.pop())

            stack.append(s[i])
            visited_set.add(s[i])

    return "".join(stack)


def is_permutation(s1:str, s2:str):
    return sorted(s1) == sorted(s2)


chr(128)
chr(0)
ord('\x80')
ord('9')


def are_permutations(s1:str, s2:str):

    if not len(s1) == len(s2): return False

    # assuming all characters are ASCII lower and upper-cased 
    character_counts = [0] * 128

    for char in s1:
        index = ord(char)
        character_counts[index] += 1

    for char in s2:
        index = ord(char)
        character_counts[index] -= 1
        if character_counts[index] < 0: return False
    
    return True











s2.index('m')






def are_permutations(s1:str, s2:str):

    if len(s1) != len(s2): return False

    # assuming we are comparing unicode ASCII characters with lower and uppercase
    characters_indices = [0] * 128

    for char in s1:
        characters_indices[ord(char)] += 1
    for char in s2:
        characters_indices[ord(char)] -= 1
        if characters_indices[ord(char)] < 0: return False
    return True


def permutation_seen(s1:str, s2:str):
    """
    s1: string with the letters we're searching for
    s2: main string we're searching in
    """
    
    # find index of letters of s1 in s2
    all_indices = []
    s1_set = set(s1)

    for i in range(len(s2)):
        if s2[i] in s1_set: all_indices.append(i)


    # [1,2,3,6,7] -> [[1,2,3], [6,7]]
    all_indices_stacks = []
    indices_stack = []

    while all_indices or indices_stack:
        print('indices_stack = ', indices_stack)

        # empty indices_stack
        if not indices_stack: 
            indices_stack.append(all_indices.pop())

        elif not all_indices:
            all_indices_stacks.append(indices_stack)
            indices_stack = []

        # not empty indices_stack and checking if they're in a range
        elif indices_stack[-1] == all_indices[-1] + 1:
            indices_stack.append(all_indices.pop())

        # not empty indices stack
        else:
            all_indices_stacks.append(indices_stack)
            indices_stack = []

    print('all_indices_stacks = ', all_indices_stacks)

    for stack in all_indices_stacks:

        if len(stack) > len(s1):
            s1_len = len(s1)
            for i in range(0, len(indices) - s1_len + 1):
                
                stack_i = stack[i:i+s1_len]
                print('stack is ', stack_i)
                string_ = s2[stack_i[-1]:stack_i[0]+1]

                print('string_ = ', string_)
                if are_permutations(s1, string_): return True

        else:
            string_ = s2[stack[-1]:stack[0]+1]

            print('string_ = ', string_)
            if are_permutations(s1, string_): return True
        
    return False


s1 = "adc"
s2 = "dcda"


permutation_seen(s1, s2)




s1_list = list(s1)
idx = s1_list.index('a')
del s1[]


indices = [6, 5, 4, 3, 2, 1, 0]
s1_len = len(s1)
for i in range(0, len(indices) - s1_len):
    print(i)
    print(indices[i:i+3])




def are_permutations(s1:str, s2:str):

    char_arr = [0] * 128
    for letter in s1:
        idx = ord(letter)
        char_arr[idx] += 1
    
    for letter in s2:
        idx = ord(letter)
        char_arr[idx] -= 1
        if char_arr[idx] < 0: return False

    return True



def has_permutation(s1:str, s2:str):

    s1_len = len(s1)
    for i in range(0, len(s2) - s1_len + 1):
        if are_permutations(s1, s2[i: i+s1_len]): return True
    else: False
    
has_permutation(s1='abc', s2 = 'babc')


from collections import Counter
Counter('abdddc')

s = "Mr    John Smith   "

import regex as re

re.sub(' +', "%20", s)

s = s.strip()
 
# Replace All space (unicode is \\s) to %20
s = s.replace(' ', "%20")
 
# Display the result
print(s)


