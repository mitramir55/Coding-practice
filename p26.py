


def helper(start, end, nums, target):
    mid_idx = (end - start) // 2 + start

    if nums[mid_idx] == target:
        return mid_idx

    if end == start + 1 and nums[mid_idx] != target: 
        print('target = ', target)
        print('nums = ', nums)
        if target > nums[mid_idx]: return mid_idx + 1
        else: return mid_idx

    elif nums[mid_idx] > target: return helper(start, end = mid_idx, nums=nums, target=target)
    else: return  helper(start = mid_idx, end = end, nums=nums, target=target)

def searchInsert(nums, target: int) -> int:
    return helper(start=0, end=len(nums), nums=nums, target=target)
    
searchInsert(nums=[1,2,3,4,5], target=5)



def find_in_sorted(nums, target):

    start, end = 0, len(nums)

    while start <= end:
        mid_idx = (end - start) // 2 + start
        if target <= nums[mid_idx]:
            end = mid_idx - 1
        else: 
            start = mid_idx + 1

    return start
