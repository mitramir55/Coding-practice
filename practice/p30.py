
import itertools
from turtle import pos


set_ = set([1,2,3])

set_.add(1)

set_.remove(1)




# first way
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
    
        chars_set = set()
        left_i, max_len = 0, 0
        
        for right_i in range(len(s)):
            
            while s[right_i] in chars_set:
                # we go on until it's empty
                chars_set.remove(s[left_i])
                left_i += 1
                
            chars_set.add(s[right_i])
            max_len = max(max_len, right_i - left_i + 1)
            
        return max_len



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
    
        chars_dict = {}
        left_i, max_len = 0, 0
        
        for right_i, l in enumerate(s):
            
            if l in chars_dict and left_i <= chars_dict[l]:
                left_i = chars_dict[l] + 1
            else:
                max_len = max(max_len, right_i - left_i + 1)
                
            chars_dict[l] = right_i
            
        return max_len


a = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]



for i in zip(*a):
    print(i)
import itertools
list(itertools.chain.from_iterable(a))


def post_order(root):
    res = []
    res += post_order(root.left)
    res += post_order(root.right)
    res += [root.val]

    return res

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            res = []
            if root:
                res += [root.val]
                res += self.preorderTraversal(root.left)
                res += self.preorderTraversal(root.right)
            return res


