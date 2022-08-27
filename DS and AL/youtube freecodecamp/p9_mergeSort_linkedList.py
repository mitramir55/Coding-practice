
import os
os.getcwd()
os.chdir(os.getcwd() + r'\\DS and AL\\youtube freecodecamp')
os.getcwd()
from p6_SinglyLinkedList import SinglyLinkedList




def merge_sort_ll(linked_list):
    if linked_list.__len__() == 1 or linked_list == None: return linked_list

    left_side, right_side = split_ll(linked_list)

    left_sorted = merge_sort_ll(left_side)
    right_sorted = merge_sort_ll(right_side)
    
    return compare_and_merge_ll(left_sorted, right_sorted)

def compare_and_merge_ll(left_side, right_side):

    new_ll = SinglyLinkedList()
    new_ll.head = 0
    curr = new_ll.head

    left_head = left_side.head
    right_head = right_side.head

    while right_head or left_head:

        # in here, if we say add_node 
        # it will be added to the beginning
        # if we say curr.next_node = ... it will be added at the end

        if left_head is None:
            curr.next_node = right_head
            right_head = right_head.next_node

        elif right_head is None:
            curr.next_node = left_head
            left_head = left_head.next_node

        else:
            if right_head.data > left_head.data:
                curr.next_node = right_head.data
                right_head = right_head.next_node

            else: 
                curr.next_node = left_head.data
                left_head = left_head.next_node

        curr = curr.next_node

    new_ll.head = new_ll.head.next_node

    return new_ll

def split_ll(linked_list):

    if linked_list == None or linked_list.head == None:
        return linked_list, None

    # what if the len(linked_list) was 1? 
    # would we just add the head?

    ll_len = linked_list.__len__()
    mid_idx = ll_len // 2
    mid_node = linked_list.get_node_at_idx(mid_idx)

    right_side = SinglyLinkedList()
    right_side.head = mid_node.next_node

    left_side = linked_list
    mid_node.next_node = None


    return left_side, right_side

import random

linked_list = SinglyLinkedList()
arr = list(range(10))
random.shuffle(arr)
for i in arr: 
    linked_list.add_node(i)

merge_sort_ll(linked_list)