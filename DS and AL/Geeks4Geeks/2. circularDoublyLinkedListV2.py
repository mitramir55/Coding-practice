from distutils.log import error
from logging import raiseExceptions


class Node:

    def __init__(self, data, next_node=None, prev_node=None) -> None:
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self) -> str:
        return f'Node: data = {self.data}'

class DoublyCircularLinkedList:

    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        """
        adding in the beginning
        """
        new_node = Node(data)

        if self.head == None:
            new_node.next_node = None
            new_node.prev_node = None
            self.head = new_node

        else:
            if self.__len__() == 1:
                # new node -> previous head 
                previous_head = self.head
                new_node.next_node = previous_head

                previous_head.next_node = new_node
                self.head = new_node

                # new node <- previous head
                previous_head.prev_node = new_node
                new_node.prev_node = previous_head

            else:
                # last node new head -> previous head 
                last_node = self.head.prev_node
                previous_head = self.head

                # last -> new head -> previous head
                last_node.next_node = new_node
                new_node.next_node = previous_head

                # last <- new_head <- previous head
                previous_head.prev_node = new_node
                new_node.prev_node = last_node


    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next_node
            if curr == self.head: break
        return count

    def insert_at(self, data, idx):

        if idx > self.__len__(): raiseExceptions(IndexError('Index out of range Miti!'))
        elif idx == 0: return self.add(self, data)

        new_node = Node(data)
        curr = self.head

        # position 
        position = 0

        # go up until we get to the position before the index we have in mind
        # position will be idx -1
        while position < idx-1:
            curr = curr.next_node
            position += 1 

        # previous node -> node in idx -> next_node
        previous_node = curr
        next_node = curr.next_node
        
        # previous node -> node in idx -> next_node
        previous_node.next_node = new_node
        new_node.next_node = next_node

        # previous node <- node in idx <- next_node
        new_node.prev_node = previous_node
        next_node.previous_node = new_node
            

    def delete_at(self, idx):

        if self.head==None: raiseExceptions('The list is empty')
        if idx > self.__len__() - 1: raise(IndexError('Index out of range Miti!'))

        elif self.__len__() == 1 and idx == 0:
            self.head = None
            
        else: 
            if idx == 0: 
                curr = self.head.prev_node
                self.head = self.head.next_node
            else: curr = self.head


            # idx = 1, position = 1
            # idx = 2, position = 0
            position = 0

            while position < idx - 1:
                position += 1
                curr = curr.next_node
            
            # previous node -> delete idx -> next_node
            previous_node = curr
            next_node = previous_node.next_node.next_node

            previous_node.next_node = next_node
            next_node.prev_node = previous_node

    def delete_val(self, data):

        # if not self.head: return ('List is empty Miti!')

        curr = self.head
        while curr:
            if curr.data == data:

                if curr == self.head:
                    self.head = self.head.next_node

                # previous node -> this one -> next node
                previous_node = curr.prev_node
                next_node = curr.next_node

                previous_node.next_node = next_node
                next_node.prev_node = previous_node

            curr = curr.next_node

            if curr == self.head: raiseExceptions(ValueError(f'{data} not in the list!'))


    def __repr__(self) -> str:
        
        curr = self.head
        if not curr: return 'empty list.'

        ret_str = ''
        ret_str += f'Head node: date = {curr.data}'

        while curr:
            curr = curr.next_node
            if curr == None: return ret_str
            if curr == self.head: return ret_str

            ret_str += f'\n Node: data = {curr.data}'

        return ret_str


ll_doubly = DoublyCircularLinkedList()

ll_doubly.add(1)
ll_doubly.add(10)
ll_doubly.add(5)
ll_doubly.add(6)

print(ll_doubly.__repr__())

ll_doubly.delete_at(idx=0)

ll_doubly.delete_val(data=10)