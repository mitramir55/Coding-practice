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


def path_sum(root, target):

    cnt = 0
    dfs(root)


    def dfs(node):

        if not node: return None

        test(node)
        dfs(node.right)
        dfs(node.left)

    def test(node, target):

        if target == node.val:
            cnt += 1
        if not node or target < 0 or target < node.val: return None
        test(node.left, target - node.val)
        test(node.right, target - node.val)




    return cnt


def count_ways(n: int, m:int):

    row = [1] * n
    for i in range(m-1):
        new_row = [1] * n
        for j in range(n-2, -1, -1):
            new_row[j] = row[j] + new_row[j+1]
        row = new_row
    return row[0]




def tribunatchi(n: int)-> int:

    three_nums = [0, 1, 1]
    for i in range(3, n+1):
        three_nums[i%3] = sum(three_nums)

    return three_nums[n%3]


a = [0, 1, 1, 0]

[1 for i in a if i==0 else 0]



[0,0,0,0], 0
[0,1,0,0], 1 
[0,0,0,0], 2 
[0,0,1,0], 3
[0,0,0,0], 4


[0,0,0,0,0], 0
[0,0,0,0,1], 1 
[0,0,0,1,0], 2
[0,0,1,0,0], 3





l = [1,2,3,4,5]

def get_sub(l):
    ret_list = []
    subset = []

    def dfs(i):
        if i >= len(l):
            ret_list.append(subset.copy())
            return 

        subset.append(l[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)

    dfs(0)

    return ret_list 

get_sub(l)



def get_num_paths(n, m):
    """
    n: number of cols
    m: number of rows
    """
    row = n * [1]

    for i in range(m-2, -1, -1):
        new_row = n * [1]
        for j in range(n-2, -1, -1):
            new_row[j] = new_row[j+1] + row[j]
        row = new_row
    return row[0]





def get_nums_path_with_obs(grid):
    n = len(grid[0])
    m = len(grid)

    grid2 = [[0]*n for _ in range(m)]

    def helper(i, j):
        if i>=m or j>=n or grid[i][j]: return 0
        if i == m-1 or j== n-1: return 1
        grid2[i][j] = helper(i, j+1) + helper(i+1, j)
        return grid2[i][j]

    helper(0, 0)
    return grid2[0][0]

dividend = 231
divisor = 3
import math 



math.exp(math.log(dividend) - math.log(divisor))



'''

i <<=1 is the same as i = i * 2, and temp <<= 1, is the same as temp *=2

The inner loop tries to subtract with (2* divisor), (4 * divisor) and so on from dividend until the dividend is smaller than the 2n * divisor. Once dividend is smaller than 2n*divisor, we set n = 1 and start again.

Let's take an example: 50 / 4
At the start,
temp, i = divisor, 1 # dividend = 50, temp = 4, i = 1
dividend -= temp # dividend = 46, temp = 4 , i = 1
res += i # res = 1
i <<= 1 # dividend = 46, temp = 4 , i = 2
temp <<= 1 # dividend = 46, temp = 8 , i = 2

Second iteration:
dividend -= temp # dividend = 38, temp = 8 , i = 2
res += i # res = 3
i <<= 1 # dividend = 38, temp = 8 , i = 3
temp <<= 1 # dividend = 38, temp = 12 , i = 3

and so on, when dividend > temp, we start over again with temp = 4, and i = 1
'''

def divide(divisor, dividend):

    positive = (divisor < 0) == (dividend < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0

    while dividend <= divisor:
        temp, i = divisor, 1

        while dividend <= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1
    res = res if positive else -res
    return min(max(res, -2147483648), 2147483647)


def permute(nums):

    res = []

    if len(nums) == 1:
        return [nums[:]] # what's the difference with nums.copy()?

    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        for perm in perms:
            perm.append(n)
        
        res.extend(perms)
        nums.append(n)
    return res


permute(nums=[1,2,3,4])