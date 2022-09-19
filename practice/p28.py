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