


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

