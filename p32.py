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
    for k in s1:
        try:
            all_indices.append(s2.index(k))
        except: return False

    # [1,2,3,6,7] -> [[1,2,3], [6,7]]
    all_indices_stacks = []
    indices_stack = []
    print('all_indices = ', all_indices)
    while all_indices:

        # empty indices_stack
        if not indices_stack: 
            indices_stack.append(all_indices.pop())
            print('initial indices_stack = ', indices_stack)

        # not empty indices_stack and checking if they're in a range
        elif indices_stack[-1] - 1 == all_indices[-1]:
            indices_stack.append(all_indices.pop())
            print('after adding indices_stack = ', indices_stack)
        else:
            all_indices_stacks.append(indices_stack)
            indices_stack = []

    print('all_indices_stacks = ', all_indices_stacks)

    for stack in all_indices_stacks:
        string_ = s2[stack[0]:stack[-1]+1]

        if are_permutations(s1, string_): return True
        
    return False


s1 = "ab"
s2 = "eidbaooo"
permutation_seen(s1, s2)