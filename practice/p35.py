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
            all_pars.append("".join(stack))
        if open < n:
            stack.append("(")
            generate(open + 1, close)
            stack.pop()
        if close < open:
            stack.append(")")
            generate(open, close + 1)
            stack.pop()
    generate(open, close)

    return all_pars


generate_pars(3)