def cal_steps(n):
    memo = {1: 1, 2: 2}
    if n in memo: return memo[n]
    else: 
        memo[n] = cal_steps(n-1) + cal_steps(n-2)
        return memo[n]

def in_order(root):
    ret_list = []
    if root:
        ret_list += in_order(root.left)
        ret_list += [root.val]
        ret_list += in_order(root.right)
    else: return []
    return ret_list


def get_len(root):
    if root:
        return 1 + get_len(root)
    return 0



def get_diameter(root):
    l_right = get_len(root)
    l_left = get_len(root)

    while root.right:
        other_rights = get_diameter(root.right)

    while root.left:
        other_lefts = get_diameter(root.left)

    return max(l_right, l_left, other_rights, other_lefts)





def get_diameter(root):
    """
    create an in order visit of the nodes 
    """

    if root:
        return get_diameter(root.left) + get_diameter(root.right) + 1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        str1 = ''
        str2 = ''
        
        while curr1:
            str1 = str(curr1.val) + str1
            curr1 = curr1.next
            
        while curr2:
            str2 = str(curr2.val) + str2
            curr2 = curr2.next
        sum_int = int(str1) + int(str2)
        str_sum = str(sum_int)
        head = new_l = ListNode(val=int(str_sum[-1]))
        
        for i in str_sum[:-1][::-1]:
            new_l.next = ListNode(val=int(i))
            new_l = new_l.next
            
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, root1: Optional[ListNode], root2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = new_l = ListNode(val=0)
        carry = 0
        while root1 or root2 or carry:
            val1, val2 = 0, 0
            if root1:
                val1 = root1.val
                root1 = root1.next

            if root2:
                val2 = root2.val
                root2 = root2.next

            carry, val = divmod(carry+val1+val2, 10)
            new_l.next = ListNode(val=val)
            new_l = new_l.next
            
        return head.next

# aabc
def lengthOfLongestSubstring(s: str):
    ret_str = ''
    res = 0
    for l in s:
        res ^= ord(l)
        print(res)
        if res==0: break
        ret_str += s
    return ret_str

