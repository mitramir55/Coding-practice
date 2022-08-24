def binary_search(arr, upper_idx, lower_idx, goal):

    mid_idx = (upper_idx - lower_idx) // 2 + lower_idx

    
    if goal == arr[mid_idx]:
        
        print('got it ')
        return mid_idx
    if goal > arr[mid_idx]:
        print('look up!')
        return binary_search(arr, upper_idx=upper_idx, lower_idx=mid_idx, goal=goal)
    else:
        print('look down!')
        return binary_search(arr, upper_idx=mid_idx, lower_idx=lower_idx, goal=goal)
binary_search(arr = list(range(0, 100)), upper_idx = 100, lower_idx = 0, goal=55)


class Node:

    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node
    

class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.__count = 0

    def __repr__(self) -> str:
        return f"this is a singly linked list with the head {self.head}"
    def is_empty(self):
        return self.head is None

    def get_size(self):
        return self.__count

    def add_node(self, node):

        node.next_node = self.head
        self.head = node
        self.__count += 1

    def search(self, num):
        curr = self.head
        while curr:
            if curr==num: 
                return ('found curr! ', curr)
            else: curr = curr.next_node
        return 'no value like this exists...'

    def insert(self, node, idx):

        if idx == 1: self.add_node(node)
        elif idx > self.__count: raise IndexError('index out of range')
        elif idx > 0:

            # start from the top
            curr = self.head
            position = 1
            while position < idx:
                position += 1
                curr = curr.next_node
                 
            return curr

    def remove(self, data):

        curr = self.head
        if curr.data == data:
            self.head = self.head.next_node
        else:
            while curr:
                if curr.data == data:
                    curr.data = curr.next
        else: curr = curr.next_node
import string
import regex as re
list_ = re.sub('[-_]', ' ', 'The_Stealth_Warrior').split()
list_[0] + [word.capitalize() for word in list_[1:]]


txt = 'the_stealth_Warrior'
txt.title().translate(None, '-_')

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

ret = txt[0] + re.sub('[-_]', '', txt.title())[1:] if txt else txt
ret