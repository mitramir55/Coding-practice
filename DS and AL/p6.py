from curses import noecho


class Node:
    def __init__(self, data, next_node = None, prev_node = None) -> None:
        self.data = data

        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self) -> str:
        return f'Node: data = {self.data}, next node = {self.next_node}, and prev node = {self.prev_node} '

class LinkedList:
    def __init__(self, head = None) -> None:
        self.head = head

    def push(self, data):
        # adding to the front
        new_head = Node(data, next_node=new_head)
        curr_head = self.head

        curr_head.prev_node = new_head
        self.head = new_head

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next_node

    def is_a_node(self, data):
        curr = self.head
        while curr:
            if curr.data == data: return True
            else: curr = curr.next_node
        return False

    def insert(self, data, previous):

        self.is_a_node(previous)

        new_node = Node(data)
        curr = self.head

        while curr:
            if curr.data == previous:
                
                # curr -> new node -> curr.next_node
                new_node.prev_node = curr
                new_node.next_node = curr.next_node
                curr.next_node = new_node
            else:
                curr = curr.next_node



    
    def append(self, data):

        new_node = Node(data)

        curr = self.head
        if self.head == None:
            self.head = new_node


        if not curr.next_node: 
            curr.next_node = new_node
            new_node.prev_node = curr
        else: curr = curr.next_node

    def delete(self, data):

        curr = self.head
        if curr.data == data:
            new_head = curr.next_node
            new_head.prev_node = None

            self.head = new_head

        while curr:
            # curr prev_node - > curr -> curr next_node
            if curr.data == data:
                previous_node = curr.prev_node
                next_node = curr.next_node

                previous_node.next_node = next_node
                next_node.prev_node = previous_node
                
                break

            else: curr = curr.next_node
