# first solution time complexity o(n+m) space O(n)
# what about O(1) space ?

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: return
        curr = headA
        i = 0
        nodes_dict = {}
        
        while curr:
            nodes_dict[curr] = i
            i += 1
            curr = curr.next
            
        curr = headB
        while curr:
            if curr in nodes_dict: 
                return curr
            curr = curr.next
            
        return



def get_intersect(heada, headb):
    a = heada
    b = headb

    while a != b:
        a = a.next if a else headb
        b = b.next if b else heada

        # they go on until the both hit null or
        # they go on until they reach the same node
    return a



nums_dict = {3:4, 5: 10}
sorted(nums_dict.items(), key = lambda x: x[1], reverse=True)[0][0]






class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res, max_c = 0, 0
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
            if max_c < nums_dict[num]: 
                res = num
                max_c = nums_dict[num]
        
        return res




def get_majority(nums):

    res, count = nums[0], 0
    for num in nums:
        if num == res:
            count += 1
        elif count == 0:
            res = num
        else: 
            count -= 1
    return res


class NodeList:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def sort_ll(root1, root2):

    head = res_ll = NodeList(val=0)

    while root1 and root2:
        if root1.val > root2.val:
            res_ll.next = root1
            root1 = root1.next
        else: 
            res_ll.next = root2
            root2 = root2.next
    
    res_ll.next = root1 or root2
    return head.next

def find_idx(nums, target):
    s, e = 0, len(nums) - 1

    while s <= e:
        mid = s + (e-s) // 2
        mid_num = nums[mid]
        if mid_num >= target:
            e = mid_num - 1
        else: 
            s = mid_num + 1

    return s


find_idx(nums=[1, 2, 3, 4, 5, 6], target=5)