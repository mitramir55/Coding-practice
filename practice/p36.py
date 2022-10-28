from collections import defaultdict, deque
import heapq


# initializing list
li = [5, 7, 9, 1, 3]
heap_ = []

for i in li:
    heapq.heappush(heap_, i)

heap_


heapq.heapify(li)
heapq.heappush(li, 3)
li

print(type(li))
print(li)

li.heappush(2)


class DinnerPlates:
    def __init__(self, capacity):
        self.c = capacity
        self.q = [] # :heap -> store the self.q in this -> record the available stack, will use heap to quickly find the smallest available stack
        self.stacks = [] # :list -> record values of all stack of plates, its last nonempty stack are the rightmost position

    def push(self, val):
        # To push, we need to find the leftmost available position
        # first, let's remove any stacks on the left that are full
        # 1) self.q: if there is still available stack to insert plate
        # 2) self.q[0] < len(self.stacks): the leftmost available index self.q[0] is smaller than the current size of the stacks
        # 3) len(self.stacks[self.q[0]]) == self.c: the stack has reached full capacity
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            # we remove the filled stack from the queue of available stacks
            heapq.heappop(self.q)

        # now we reach the leftmost available stack to insert

        # if the q is empty, meaning there are no more available stacks
        if not self.q:
            # open up a new stack to insert
            heapq.heappush(self.q, len(self.stacks))

        # for the newly added stack, add a new stack to self.stacks accordingly
        if self.q[0] == len(self.stacks):
            self.stacks.append([])

        # append the value to the leftmost available stack
        self.stacks[self.q[0]].append(val)

    def pop(self):
        # To pop, we need to find the rightmost nonempty stack
        # 1) stacks is not empty (self.stacks) and
        # 2) the last stack is empty
        while self.stacks and not self.stacks[-1]:
            # we throw away the last empty stack, because we can't pop from it
            self.stacks.pop()

        # now we reach the rightmost nonempty stack

        # we pop the plate from the last nonempty stack of self.stacks by using popAtStack function
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        # To pop from a stack of given index, we need to make sure that it is not empty
        # 1) the index for inserting is valid and，
        # 2) the stack of interest is not empty
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            # we add the index into the available stack
            heapq.heappush(self.q, index)
            # take the top plate, pop it and return its value
            return self.stacks[index].pop()

        # otherwise, return -1 because we can't pop any plate
        return -1



from typing import Optional
from collections import defaultdict, deque


def breadth_first_search(edges: list[list], source: int, destination: int, n: int):

    q = deque([source])
    seen = set([source])
    dictionary = defaultdict(list)
    for s, d in edges:
        dictionary[s].append(d)
        dictionary[d].append(s)

    while q:
        node = q.popleft()
        if node == destination:
            return True
        else:
            for dest in dictionary[node]:
                if dest not in seen:
                    seen.add(seen)
                    q.append(dest)

    return False


def deapth_first_search(source, destination, edges, n):

    neighbors = defaultdict(list)
    for s, d in edges:
        neighbors[s].append(d)
        neighbors[d].append(s)

    seen = set()
    def dfs(node):
        if node == destination: return True
        if node in seen: return False

        seen.add(node)
        for neighbor in neighbors[node]:
            if dfs(neighbor): return True
        return False
    return dfs(source)





nums = [-10,-3,0,5,9]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: list[int]) -> Optional[TreeNode]:

    if not nums: return None
    mid_idx = len(nums) // 2

    root = TreeNode(nums[mid_idx])
    root.left = sortedArrayToBST(nums[:mid_idx])
    root.right = sortedArrayToBST(nums[mid_idx:])

    return root

def sortedArrayToBST(nums: list[int]) -> Optional[TreeNode]:

    def helper(l, r):
        if l > r:
            return None
        mid_idx = (l - r) // 2 + l
        
        root = TreeNode(val=nums[mid_idx])
        root.left = helper(l, mid_idx - 1)
        root.right = helper(mid_idx + 1, l)
        return root

    return helper(0, len(nums) - 1)




def level_order_traversal(root: Optional[TreeNode]) -> list[list[int]]:

    ret_list = []
    level_nodes = [root]

    while level_nodes and root:
        curr_level_vals = []
        next_level_nodes = []

        for node in level_nodes:
            curr_level_vals.append(node.val)
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)

        ret_list.append(curr_level_vals)
        level_nodes = next_level_nodes
    return ret_list




def level_order_traversal(root: Optional[TreeNode]) -> list[list[int]]:

    level_nodes, ret_list = [root], []

    while root and level_nodes:
        ret_list.append([node.val for node in level_nodes])
        left_right_pairs = [(node.left, node.right) for node in level_nodes]
        level_nodes = [leaf for pair in left_right_pairs for leaf in pair if leaf]

    return ret_list

[leaf for pair in pairs for leaf in pair]











from collections import deque
from typing import Optional


def depth_first_search(source: int, destination:int, edges:list[tuple[int]]) -> bool:

    neighbors = defaultdict(list)
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)

    seen = set()
    def dfs(node):
        if node == destination: return True
        if node in seen: return False
        seen.add(node)

        for neighbor in neighbors[node]:
            if dfs(neighbor): return True
        return False
    
    return dfs(source)





import math
class TreeNode:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

def is_binary_search_tree(root: Optional[TreeNode]):

    r_bound, l_bound = math.inf, - math.inf

    def is_BST(node, r_bound, l_bound):

        if not node: return True
        if not l_bound < node.val < r_bound: return False

        is_BST(node.left, l_bound=l_bound, r_bound=node.val)
        is_BST(node.right, l_bound=node.val, r_bound=r_bound)
        

    return is_BST(root, r_bound, l_bound)