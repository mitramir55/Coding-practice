from typing import Optional

# defining the class for nodes
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head:Optional[ListNode], n: int) -> Optional[ListNode]:
    fast, slow = head, head

    for _ in range(n): fast = fast.next

    # [1], n = 1 -> fast == None
    if not fast: return None

    # slow = one before nth from the end, so we check for fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return head








def generate_pars(n:int) -> list:
    open = 0
    close = 0
    stack = []
    all_pars = []

    def generate(open, close):

        if open == close == n:
            print('finished! : ', "".join(stack))
            print()
            all_pars.append("".join(stack))


        if open < n:
            stack.append("(")
            print('Opening: ', stack)

            generate(open + 1, close)
            stack.pop()

        if close < open:
            stack.append(")")
            print('Closing: ', stack)
            generate(open, close + 1)
            stack.pop()
    generate(open, close)

    return all_pars


generate_pars(3)



import numpy as np
np.random.randn(20, 3)




def generateParenthesis(n: int):
    
    stack = []
    res = []

    def generate(open, closed):

        if n == open == closed:
            res.append("".join(stack))
            return 

        if open < n:
            stack.append('(')
            generate(open+1, closed)
            stack.pop()
        if closed < open:
            stack.append(')')
            generate(open, closed+1)
            stack.pop()

    generate(open=0, closed=0)
    
    return res




class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def convert_list(head: ListNode) -> int:
    """
    1 -> 2 -> 3 : 321
    """
    curr = head
    i = 0
    num = 0
    while curr:
        num += curr.val * 10 ** i
        i += 1
        curr = curr.next 
    return num


def convert_num(num: int) -> ListNode:

    head = curr = ListNode(val=0)

    while num:
        curr.next = ListNode(val = num%10)
        num //= 10
        curr = curr.next

    return head.next

def sum_lists(head1: ListNode, head2:ListNode) -> ListNode:

    num1 = convert_list(head1)
    num2 = convert_list(head2)

    sum_ = num1 + num2
    sum_list_head = convert_num(sum_)

    return sum_list_head



# other way around

def convert_list2(head: ListNode) -> int:
    """
    1 -> 2 -> 3 : 123
    go through the list and create a string of all the values joined together
    then, convert this to an int
    """
    curr = head
    str_ = ''
    while curr:
        str_ += str(curr.val)
        curr = curr.next
    return int(str_)


def convert_num(num: int) -> ListNode:

    """
    go through the string version of digits and add the digits one at a time
    """
    head = curr = ListNode(0)
    for digit in str(num):
        curr.next = ListNode(val = int(digit))
        curr = curr.next

    return head.next


def sum_lists_2(head1: ListNode, head2:ListNode) -> ListNode:

    sum_ = convert_list2(head1) + convert_list2(head2)
    list_ = convert_num(sum_)
    return list_




from typing import Optional
def is_palindrom(head: Optional[ListNode]) -> bool:
    """
    get the head. create two pointers. when fast or fast.next is null, slow is
    in the middle. Therefore, we compare two lists, one starting at head, another
    starting at slow.
    """
    slow, fast = head, head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        fast = fast.next.next
        slow = slow.next

    if fast: curr = slow.next
    else: curr = slow

    while stack and curr:
        if not curr.val == stack.pop(): return False
        curr = curr.next
    return True
