


def in_order(root):

	ret_list = []

	if not root: return True

	ret_list += in_order(root.left)
	ret_list.append(root.val)
	ret_list += in_order(root.right)
	
	return ret_list

class ListNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def are_sym(root1, root2):

	if root1.val == root2.val == None: return True
	if not root1.val or not root2.val: return False
	
	if root1.val == root2.val:
		return are_sym(root1.left, root2.right) and are_sym(root1.right, root2.left)

def is_sym(root):
	
	if not root: return True
	
	return are_sym(root.left, root.right)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        for k in nums:
            nums_dict[k] = nums_dict.get(k, 0) + 1
            
            
        return [k for k, v in nums_dict.items() if v == 1][0]


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        if not curr: return False
        passed_vals = {curr.val: 0}
        i = 1
        curr = curr.next
        
        while curr:
            if curr.next not in passed_vals: 
                curr = curr.next
                passed_vals[curr] = i
                i += 1
                
            else: return True
            
        return False
    

def has_cycle(root):
    slow = root
    fast = root.next
    # s, f
    #  , s,   , f
    #  ,  ,  s,  ,   ,   , f
    #  ,  ,   , s,   ,   ,  ,  ,  , f 
    # 1, 2 , 3, 4, 5, 6, 7, 8
    while slow != fast:
        slow = slow.next
        fast = fast.next.next