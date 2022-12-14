from logging import raiseExceptions


class Node:

    def __init__(self, data, next_node=None, prev_node=None) -> None:
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self) -> str:
        return f'Node: data = {self.data}'

class DoublyCircularLinkedList:

    def __init__(self, head=None, last_node=None):
        self.head = head
        self.last_node = last_node

    def add(self, data):

        new_node = Node(data)

        if self.head == None:
            self.head = new_node

        elif self.head and self.last_node==None:
            
            # define the nodes
            self.last_node = self.head
            self.head = new_node

            # head -> last and last -> head
            self.last_node.next_node = self.head
            self.head.next_node = self.last_node

            self.last_node.prev_node = self.head
            self.head.prev_node = self.last_node


        else:
            # new_head=new_node -> prev head
            previous_head = self.head
            previous_head.prev_node = new_node

            # new_node props
            self.head = new_node
            new_node.next_node = previous_head

            # last head ->  new_head
            self.last_node.next_node = new_node
            new_node.prev_node = self.last_node

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next_node
            if curr == self.head: break
        return count

    def insert(self, data, idx):

        if idx > self.__len__(): raiseExceptions(IndexError('Index out of range Miti!'))
        new_node = Node(data)
        curr = self.head

        # position 
        position = 0

        # go up until we get to the position before the index we have in mind
        while position < idx-1:
            curr = curr.next_node
            position += 1 

        # previous node -> node in idx -> previous.next_node
        previous_node = curr
        next_node = curr.next_node
        
        # previous node -> node in idx
        previous_node.next_node = new_node
        new_node.prev_node = previous_node
            
        new_node.next_node = next_node
        next_node.previous_node = new_node

    def delete(self, idx):

        if self.head==None: raiseExceptions('The list is empty')
        if idx > self.__len__() - 1: raise(IndexError('Index out of range Miti!'))

        elif self.__len__() == 1:
            self.head = None

        elif self.__len__() == 2:
            # if we only had head and last nodes
            if idx == 0:
                self.last_node = self.head
                self.last_node.next_node = None
                self.last_node.prev_node = None
            # i have to rewrite it cause we don't want the head
            # to be the last too
            elif idx == 1:
                self.head.next_node = None
                self.head.prev_node = None
                self.last_node = None

        elif idx == self.__len__() - 1:
            self.last_node = self.last_node.prev_node
            self.last_node.next_node = self.head

            self.head.prev_node = self.last_node
            
        else: 
            curr = self.head

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

        if self.head == None: raiseExceptions('List is empty Miti!')
        curr = self.head
        while curr:
            if curr.data == data:
                # previous node -> this one -> next node
                previous_node = curr.prev_node
                next_node = curr.next_node

                previous_node.next_node = next_node
                next_node.prev_node = previous_node

    def __repr__(self) -> str:
        
        curr = self.head
        if self.head == None: return 'empty list.'
        ret_str = ''

        while curr:

            if curr == self.head: 
                ret_str += f'Head node: date = {curr.data}'
            
            elif curr == self.last_node: 
                ret_str += f'\nLast node: data = {curr.data}'
                break

            else: ret_str += f'\n Node: data = {curr.data}'

            curr = curr.next_node

        return ret_str


ll_doubly = DoublyCircularLinkedList()

ll_doubly.add(1)
ll_doubly.add(10)
ll_doubly.add(5)
ll_doubly.add(6)

print(ll_doubly.__repr__())

ll_doubly.delete(idx=0)
