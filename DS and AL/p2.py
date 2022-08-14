# create a tree in python 
# https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree

class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def return_value(self):
        return self.value


root = Node(6)
root.left = Node('left')
root.right = Node('right')



# unival tree

def is_unival(root, value):

    # if we get to the buttom leaf
    if root is None:
        return True
    
    if root.left != root.value:
        return False
    if root.right != root.value:
        return False

    if is_unival(root.left) and is_unival(root.right):
        return True

    return False

def count_univals(root):

    if root==None: return 0
    total_count = count_univals(root.left)+count_univals(root.right)

    if is_unival(root): total_count+=1

    return total_count