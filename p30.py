
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