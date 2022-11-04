class Solution:
    def canFinish(self, numCourses: int, edges: List[List[int]]) -> bool:
        edges_dict = defaultdict(list)
        for n, m in edges:
            edges_dict[n].append(m)

        seen = set()

        def dfs(node):

            if node in seen: return False
            # if we don't have any prerequisite
            if edges_dict[node] == []: return True

            seen.add(node)

            for prereq in edges_dict[node]:
                if not dfs(prereq): return False
            
            seen.remove(node)
            edges_dict[node] = []

            return True

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

def is_subtree(root: Optional[TreeNode], subtree: Optional[TreeNode]) -> bool:

    def helper(r1, r2):

        if not r1 or not r2: return r1 == r2
        if r1.val == r2.val and helper(r1.right, r2.right) and helper(r1.left, r2.left): return True
        return False
    
    
    if helper(root, subtree): return True
    if not root or not subtree: return False
    return (is_subtree(root.left, subtree) or is_subtree(root.right, subtree))


def hasPathSum(root: TreeNode, target_num: int):

    if not root: return False
    
    def helper(r, sum_):
        if not root: return False
        sum_ = root.val + sum_
        if not root.left or not root.right: return sum_ == target_num
        return helper(r.left, sum_) or helper(r.right, sum_)
        
    return helper(root, sum_=0)