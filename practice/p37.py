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


def permute(nums):
    res = []
    if len(nums) == 1:
        print(f'reached the end: nums = {nums[:]}')
        return [nums[:]]
    for _ in range(len(nums)):
        n = nums.pop(0)
        print('popping ', n)
        perms = permute(nums)
        for perm in perms:
            perm.append(n)
        
        print(f'extending: nums = {perms}')
        res.extend(perms)
        nums.append(n)
        print()
    return res

permute([1,2,3,4])




def find_subsets(nums):

    res = []
    subset = []

    def dfs(i):
        if i == len(nums):
            res.append(subset[:])
            
        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)

    dfs(0)
    return res


set([ [1,2,3], [1,2,3]])



from collections import defaultdict
def unique_permutations(nums):

    nums_count = defaultdict(int)
    for num in nums: nums_count[num] = nums_count.get(num, 0) + 1
    print(nums_count)

    perm = []
    res = []

    def dfs():
        if len(perm) == len(nums): 
            res.append(perm[:])
            return

        for num in nums_count:
            if nums_count[num] > 0: 

                perm.append(num)

                # after decreasing the value by one, we increase it so 
                # for the next number in the nums, we will have the same
                # distribution
                nums_count[num] -= 1
                dfs()
                nums_count[num] += 1

                perm.pop()
    dfs()
    return res


unique_permutations([1, 1, 3])




def create_target_2(nums, target):

    res, stack = [], []
    sum_ = 0

    def dfs(sum_):
        if sum_ == target:
            res.append(stack[:])
        for num in nums:
            while sum_ < target:
                sum_ += num
                stack.append(num)
                dfs(sum_)
                sum_ -= num
                stack.pop()

    dfs(sum_)
    return stack


create_target([1, 2, 5], target=5)












def make_target(coins, target):
    coins = sorted(coins, reverse=True)
    coins_set = set(coins)
    sum_, temp_sum = 0, 0
    res, stack = [], []
    

    for i in coins:
        if i > target:
            continue

        if sum_ == target: 
            res.append(stack[:])
            print("sum_ == target and stack is ", stack)
            stack = []
            sum_ = 0
        
        while temp_sum < target:
            sum_ = temp_sum
            stack.append(i)
            temp_sum += i
            if target - temp_sum in coins_set:
                sum_ = target
                stack.append(target - temp_sum)
                break
            elif temp_sum > target:
                sum_ = 0
                stack = []
                break

    return res[0]

make_target(coins=[4, 1], target=9)



def coin_change(coins, amount):

    dp = [amount + 1] * (amount + 1)

    # to get from index i to target we have to have n coins
    dp[0] = 0

    for am in range(1, amount + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[am] = min(dp[am], 1 + dp[am - coin])
    return dp[amount] if dp[amount] != amount + 1 else -1








def coin_change(amount, coins):

    dp = (amount + 1) * [0]
    dp[0] = 1
    for i in range(len(coins)-1, -1, -1):
        next_dp = [0] * (amount + 1) # + 1 cause we have 0
        next_dp[0] = 1
        for am in range(1, amount + 1):
            next_dp[am] = dp[am]
            if am - coins[i] >= 0:
                next_dp[am] += next_dp[am - coins[i]]
            dp = next_dp
    
    return dp[amount]







def coin_ways(coins, amount):

    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        new_dp = [0] * (amount + 1) 
        new_dp[0] = 1

        for am in range(amount + 1):
            new_dp[am] = dp[am] # the element below
            if am - coin >= 0:
                new_dp[am] += new_dp[am - coin] # the left element
            dp = new_dp

    return new_dp[-1]






class Solution:
    def __init__(self, cnt) -> None:
        self.cnt = 0
            
    def tree_sum(self, root, amount):

        def dfs(root, amount):

            if not root: return None
            test(root, amount)
            dfs(root.left, amount)
            dfs(root.right, amount)

        def test(node, amount):

            if node.val == amount: self.cnt += 1
            if node.val < amount:
                test(node.left, amount-node.val)
                test(node.right, amount-node.val)

        return self.cnt


def lca_in_bst(p, q, root):

    ans = root
    while ans:
        if root.val > p.val and root.val > q.val:
            ans = ans.left
        elif root.val < p.val and root.val < q.val:
            ans = ans.right
        else:
            return ans


def lca_bt(p, q, root):

    # base case
    if not root: return None
    if root==q or root==p: return root

    left = lca_bt(p, q, root.left)
    right = lca_bt(p, q, root.right)

    if right and left: return root
    else: return right or left


from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    m: first list len
    n: second list
    """
    nums1, nums2 = nums1[:m], nums2[:n]
    i, j = m, n
    ret_list = []

    if not nums1 or not nums2: return nums1 or nums2

    while nums1 != [] and nums2 != [] :
        print("nums1 = ", nums1)
        print("---")
        print("nums2 = ", nums2)

        if nums1[0] < nums2[0]:
            ret_list.append(nums1.pop(0))
        else:
            ret_list.append(nums2.pop(0))

        print("ret_list = ", ret_list)
        print()
        
    while nums1!= [] : 
        ret_list.append(nums1.append(nums1.pop(0)))
    while nums2!= [] : 
        ret_list.append(nums2.append(nums2.pop(0)))

    return ret_list


merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)




set("eat")==set("tea")



[0] * 26

from collections import defaultdict
def get_anagrams(strs):

    chars_dict = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for letter in s: count[ord(letter) - ord("a")] += 1
        chars_dict[tuple(count)].append(s)

    return chars_dict.values()


get_anagrams(['ate', 'eat', 'mean'])

num = 1
nums = [4,5,6,7,0,1,2]

def search(nums, target):
    try:
        return nums.index(target)
    except:
        return -1

search(nums, 0)



1 ^ 5 ^ 10 


nums = [1,2,3,1000]
nums[1000]



def find_duplicate_val(nums):
    fast, slow, check = 0, 0, 0

    while True:

        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow==fast:
            break

    while True:
        slow = nums[slow]
        check = nums[check]
        if slow == check: break
    return check



import heapq

class KthLargest:

    def __init__(self, k: int, nums):

        self.kth = k
        self.heap_ = nums
        heapq.heapify(self.heap_)

        while len(self.heap_) > self.k:
            heapq.heappop(self.heap_)

    def add(self, val) -> int:
        heapq.heappush(self.heap_, val)
        if len(self.heap_) > self.kth:
            heapq.heappop(self.heap_)
        return self.heap_[0]


for (i,j) in zip(range(2), range(4)):
    print(i,j)



s = "cabaf"
i = 1
j = 4
s[i:j] == s[i:j:-1]

s[j-1:i-1:-1] 
len(s)
n = len(s)

for i in range(n):
    for j in range(n, i, -1):

        print('s[i:j] = ', s[i:j])
        print('s[i:j:-1]', s[j:i:-1])
        print('i = ', i)
        print('j = ', j)

        print()
        if s[i:j] == s[i:j:-1] and len(s[i:j]) > max_len:
            max_len = len(s[i:j])
            res_pal = s[i:j]