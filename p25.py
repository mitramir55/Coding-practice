def helper(s, e, nums, target):

    # [1, 2, 3, 4, 5]
    mid_idx = (e - s) // 2 + s
    mid_val = nums[mid_idx]

    if e == s + 1 and mid_val != target: 
        if mid_val > target: return mid_idx
        else: return mid_idx + 1
 
    elif mid_val == target: return mid_idx
    elif mid_val > target:
        return helper(s = s, e = mid_idx, target = target, nums = nums)
    else: return helper(s = mid_idx, e = e, target = target, nums = nums)

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        
        return helper(s = 0, e = len(nums), target = target, nums = nums)



# target = 0
#  s     m     e
# [1, 2, 3, 4, 5]
# 0      2      len(nums) - 1
s = 0
e = len(nums) - 1
while s < e:

    mid_idx = (e - s) // 2 + s
    if nums[mid_idx] >= target:
        e = mid_idx - 1
    else: s = mid_idx

return s


