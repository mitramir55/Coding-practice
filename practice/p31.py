import numpy as np
from itertools import chain

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        board = np.array(board)
        
        # checking horizontal arrays
        for arr in board:
            seen_set = set()
            for element in arr:
                if element == '.': continue
                else: 
                    if element in seen_set: 
                        print('row false')
                        return False
                    seen_set.add(element)
            
        # checking for vertical columns
        for arr in board.T:
            seen_set = set()
            
            for element in arr:
                if element == '.': continue
                else: 
                    if element in seen_set: 
                        print('col false')
                        return False
                    seen_set.add(element)
            
        # checking the 3 x 3 boxes
        for i in range(3):
            sec1 = board[i*3: (i+1)*3]
            
            for j in range(3):
                seen_set = set()
                sec2 = sec1.T[j*3: (j+1)*3]
                print('sec2: \n', sec2)
                
                for element in chain.from_iterable(sec2):
                    if element == '.':
                        continue
                    else:
                        if element in seen_set: 
                            return False
                        seen_set.add(element)
                        
                        
        return True





import numpy as np
from itertools import chain


def is_valid(arr):
    arr = [k for k in arr if k != '.']
    return len(arr) == len(set(arr))

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # horizontal check
        for arr in board:
            if not is_valid(arr): return False

        # vertical check
        for arr in zip(*board):
            if not is_valid(arr): return False

        # for 3 x 3 matrixes
        for i in range(3):
            for j in range(3):
                arr = [board[x][y] for x in range(i*3, (i+1)*3) 
                for y in range(j*3, (j+1)*3)]

                if not is_valid(arr): return False
                
        return True



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_lists_vals = []
        for ll in lists:
            while ll:
                all_lists_vals.append(ll.val)
                ll = ll.next
                
        sorted_list = sorted(all_lists_vals)
        head = curr = ListNode(0)
        for val in sorted_list:
            curr.next = ListNode(val=val)
            curr = curr.next
            
        return head.next
    

print(" this is coooool \"\"")
# studied 2 series of Java

import math
def max_profit(nums):
    max_profit, min_start = 0, nums[0]

    for num in nums[1:]:

        min_start = min(min_start, num)
        temp_profit = num - min_start
        max_profit = max(temp_profit, max_profit)

    return max_profit


def is_cycle(root):
    if root == None: return True
    slow, fast = root, root.next

    while slow != fast:
        if not fast or not fast.next: break
        fast = fast.next.next
        slow = slow.next
    return  fast == slow



def find_intersection(headA, headB):
    root1, root2 = headA, headB

    while root1 != root2:
        root1 = root1.next if root1 else headB
        root2 = root2.next if root2 else headA

    return root1 

def find_majority(nums):
    count, prev = 0, nums[0]
    for num in nums:
        if num==prev:
            count += 1
        
        elif count == 0 and num != prev:
            prev = num
        else:
            count -= 1

    return num

import regex as re
s = "3[a2[c]]"
s = "3[a]2[bc]"

def replace_pattern(patt):

    times = int(re.findall('\d', patt)[0])
    letters = re.findall("\[(\w*)\]", patt)[0]
    return times * letters


found_spans = re.findall("\d\[\w*\]", s)
found_spans


print('s = ', s)


while '[' in s:
    found_spans = re.findall("\d\[\w*\]", s)
    for span in found_spans:
        replacement = replace_pattern(span)
        s = s.replace(span, replacement)




re.sub('(2[c])', 'cc', s)

patt = "2[c]"
times = int(re.findall('\d', patt)[0])
letters = re.findall("\[(\w*)\]", patt)
times
letters