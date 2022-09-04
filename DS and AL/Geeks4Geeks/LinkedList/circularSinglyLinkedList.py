class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class CircularLinkedList:
    def __init__(self, head=None, last_node=None) -> None:
        self.head = head
        self.last_node = last_node

    def add(self, data):

        new_head = Node(data, next_node=self.head)

        # no head or last node
        if self.head == None:
            self.head = new_head

        # only one head and no last node
        if self.head and not self.last_node:

            # new head -> previous head = last node
            self.last_node = self.head
            self.head = new_head

            # new head -> last node
            self.head.next_node = self.last_node

            # last node -> new head
            self.last_node.next_node = self.head
        
        else:
            # last node -> new head
            self.last_node.next_node = new_head

            # head -> previous head
            previous_head = self.head
            self.head = new_head
            self.head.next_node = previous_head


    def append(self, data):

        new_node = Node(data)
        curr = self.head

        # no head
        if curr==None: 
            self.add(data)

        # head -> None : head -> new_node=last node
        elif curr and not self.last_node:
            self.last_node = new_node
            self.last_node.next_node = curr

        else:
            # previous last node -> new last node -> head
            prev_last = self.last_node
            prev_last.next_node = new_node

            self.last_node = new_node
            self.last_node.next_node = self.head
    
    def __repr__(self) -> str:

        curr = self.head
        ret_str = ''

        if not curr: return 'empty list!'

        ret_str = f'head is {curr.data}'

        while curr:
            curr = curr.next_node

            if curr == self.last_node:
                ret_str += f'\nLast Node: data = {curr.data}'
                break
                
            ret_str += f'\n Node: data = {curr.data}'

        return ret_str



cll = CircularLinkedList()
cll.add(1)
cll.add(data=89)
cll.append(94)
print(cll.__repr__())