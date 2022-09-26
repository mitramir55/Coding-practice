
import itertools
from turtle import left, pos, right

from DS and AL.6.0001.4. Merge_sort import merge_sort


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

def helper(root1, root2):
    if not root1 and not root2: return True
    if not root1 or not root2: return False
    if root1.val == root2.val:
        return helper(root1.left, root2.right) and helper(root1.right, root2.left)
    return False

def is_sym(root):
    if not root: return True
    if root: return helper(root.left, root.right)



def max_depth(root):
    height = 0
    if root:
        height = max(max_depth(root.right), max_depth(root.left)) + 1 
    return height



def reverse_ll(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next: return None
                
        curr = head2 = reverse_ll(head)
        if n == 1: head2 = curr.next
        else:
            position = 1
            while position < n-1:
                position += 1
                curr = curr.next
            curr.next = curr.next.next
        
        
        return reverse_ll(head2)


class Solution:
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
    fast, slow = head, head

    for _ in range(n): fast = fast.next
    # list = [1] and n = 1 -> next will be None
    if not fast: return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    
    return head










    


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        all_vals = []
        while curr:
            all_vals.append(curr.val)
            curr = curr.next
        all_vals = sorted(all_vals)
        
        head = curr = ListNode(0)
        for val in all_vals:
            curr.next = ListNode(val=val)
            curr = curr.next
            
        return head.next



def compare_and_sort(left_arr, right_arr):

    res = []

    while left_arr and right_arr:

        if left_arr[0] < right_arr[0]:
            res.append(left_arr[0])
            del left_arr[0]
        else: 
            res.append(right_arr[0])
            del right_arr[0]

    res += left_arr or right_arr
    return res


def merge_sort(arr):
    if len(arr) < 2: return arr
    mid_idx = len(arr) // 2

    left_sorted = merge_sort(arr[:mid_idx])
    right_sorted = merge_sort(arr[mid_idx:])

    return compare_and_sort(left_sorted, right_sorted)
    


arr = [2, 5, 3, 6, 8, 10]

merge_sort(arr)




# 1 -> 2 -> 0 -> 5


def compare_and_sort(left_root, right_root):

    head = res_ll = ListNode(0)

    while left_root and right_root:

        if right_root.val < left_root.val:
            res_ll.next = right_root.val
            right_root = right_root.next
        else:
            res_ll.next = left_root.val
            left_root = left_root.next


    res_ll.next = left_root.next or right_root.next

    return head.next



def merge_sort_ll(head):

    fast, slow = head, head
    while fast.next:
        fast = fast.next.next
        slow = slow.next

    right_sorted = merge_sort(slow)

    slow.next = None
    left_sorted = merge_sort(head)

    return compare_and_sort(left_sorted, right_sorted)
    


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_mid_node(head):
    # because we want the one before the middle
    # we start fast at head.next
    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow

def compare_and_sort(right_root, left_root):

    head = curr = ListNode(0)

    while left_root and right_root:

        if right_root.val < left_root.val:
            curr.next = right_root
            right_root = right_root.next
        else:
            curr.next = left_root
            left_root = left_root.next
        curr = curr.next
        
    if right_root:
        curr.next = right_root
    if left_root:
        curr.next = left_root
    
    return head.next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        head2 = get_mid_node(head)
        right_sorted = self.sortList(head2.next)

        head2.next = None
        left_sorted = self.sortList(head)

        return compare_and_sort(right_sorted, left_sorted)

