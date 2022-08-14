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


# binary search tree

class Node:
    def __init__(self, val) -> None:
        self.right = None
        self.left = None
        self.val = val

    def insert(self, val):

        # if there is no data in the root
        if self.val is None: self.val = val

        # if the root already has this value
        if self.val == val: return

        # right 
        if val>self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

        # left
        elif val<self.val:
            if self.left is None:
                self.left = Node(val)
            else: 
                self.left.insert(val)

    def print_tree(self):

        print(self.val)

        if self.left: self.left.print_tree()
        if self.right:self.right.print_tree()

    def get_min(self):
        if self.left is None:
            return self.val
        else: return self.left.get_min()

    def get_max(self):
        if self.right is None:
            return self.val
        else: return self.right.get_max()

    def delete(self, val):

        if self == None: return self
        if val < self.val: return self.left.delete(val)
        if val > self.val: return self.right.delete(val)

    # why doesn't this work?
    def exists_1(self, val):
        if self.val == val: return True

        if self.val > val: 
            if self.right == None: return False
            else: return self.right.exists(val)

        if self.val < val: 
            if self.left == None: return False
            else: return self.left.exists(val)


    def exists(self, val):
        
        if self.val == None: return False
        if self.val == val: return True
        if val > self.val:
            return self.right.exists(val)
        if val < self.val:
            return self.left.exists(val)




a = Node(5)
a.insert(20)
a.insert(1)
a.insert(50)
a.insert(0)
a.print_tree()
a.get_max()
a.get_min()
a.exists(0)