


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