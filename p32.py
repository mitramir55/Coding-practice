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
