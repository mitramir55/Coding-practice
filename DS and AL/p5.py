
# merge sort on a linked list ------------------------------------------------
import os

os.chdir(os.getcwd() + r'\\DS and AL\\youtube freecodecamp')

os.getcwd()

from p6_SinglyLinkedList import SinglyLinkedList

def merge_sort_ll(linked_list):

    if linked_list.head == None: return linked_list
    elif linked_list.__len__() == 1: return linked_list

    left_side, right_side = split_ll(linked_list)

    print('len of left_side = ', left_side.__len__())
    print('len of right_side = ', right_side.__len__())


    left_side_sorted = merge_sort_ll(left_side)
    right_side_sorted = merge_sort_ll(right_side)

    return compare_and_merge_ll(left_side_sorted, right_side_sorted)


def split_ll(linked_list):

    len_ = linked_list.__len__()
    mid_idx = len_ // 2 - 1
    print(f'mid_idx = {mid_idx}')

    mid_node = linked_list.get_node_at_idx(mid_idx)
    print(f'mid_node.data = {mid_node.data}')

    # the right side split will start with 
    right_list = SinglyLinkedList()
    right_list.head = mid_node.next_node

    # left side will be the current list but without the attachment to the rest
    left_list = linked_list
    mid_node.next_node = None

    print()
    return left_list, right_list


def compare_and_merge_ll(left_side_l, right_side_l):

    print('inside compare and merge')
    new_l = SinglyLinkedList()

    left_len = left_side_l.__len__()
    right_len = right_side_l.__len__()

    i, j = 0, 0
    while i < left_len and j < right_len:

        left_i = left_side_l.get_node_at(i)
        right_j = right_side_l.get_node_at(j)

        if left_i > right_j: 
            new_l.add_node(left_i)
            i += 1

        else:
            new_l.add_node(right_j)
            j+=1
    
    # anything left to add?
    while i < left_len: 
        left_i = left_side_l.get_node_at(i)
        new_l.add_node(left_i)
        i += 1

    while j < right_len: 
        right_j = right_side_l.get_node_at(j)
        new_l.add_node(right_j)
        j += 1
    print('new l = ', new_l)
    
    return new_l


import random

arr = list(range(0, 10))
random.shuffle(arr)
print(arr)

singlylist = SinglyLinkedList()

for i in arr:
    singlylist.add_node(i)
print(singlylist)

sorted_ll = merge_sort_ll(linked_list=singlylist)


print(sorted_ll)
