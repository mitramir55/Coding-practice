
class Node:
    def __init__(self, data, next_node=None, prev_node=None) -> None:
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return f'Node with data = {self.data}, previous node = {self.next_node}, next_node = {self.prev_node}'


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.__count = 0

    def size(self):
        return self.__count

    def add_node(self, data):

        last_head = self.head
        new_head = Node(data=data)

        # new node will be the previous of the last head node
        if last_head:
            new_head.next_node = last_head
            last_head.prev_node = new_head

        self.head = new_head
        self.__count += 1
    
    def search_value(self, goal):

        curr = self.head
        for i in range(self.__count):
            if goal == curr.data:
                return f'Found it! it is element in position {i+1}.'
            curr = curr.next_node

        return None
    def insert_at(self, data, idx):

        if idx > self.__count:
            raise IndexError('Index out of range!!!')
        
        elif idx == 0: 
            self.add_node(data)

        elif idx > 0:
            
            position = idx
            curr = self.head

            while position > 0:
                curr = curr.next_node
                position -= 1

            # previous_node(curr) -> next_node (curr.next_node)
            # previous_node(curr) -> new_node -> next_node (curr.next_node)
            previous_node = curr
            next_node = curr.next_node

            new_node = Node(data, next_node=next_node, prev_node=previous_node)
            
            previous_node.next_node = new_node
            next_node.prev_node = new_node

            self.__count += 1

        else: raise IndexError(' format of the index is not accepted')



    def remove(self, goal):

        curr = self.head

        if goal == curr.data:

            new_head = curr.next_node
            new_head.prev_node = None
            self.head = new_head

            self.__count -= 1

        elif self.search_value(goal=goal):
            
            while curr:
                
                if curr.next_node.data == goal:

                    print('next node is the one!')

                    # previous_node (curr) -> goal -> next_node
                    previous_node = curr
                    next_node = curr.next_node.next_node

                    # previous_node -> next_node
                    previous_node.next_node = next_node
                    next_node.prev_node = previous_node

                    self.__count -= 1

                curr = curr.next_node

        else:
            return 'we do not have any value like this!'

    def remove_idx(self, idx):
        
        if idx == 0: 
            new_head = self.head.next_node
            new_head.prev_node = None
            self.head = new_head
            self.__count -= 1

        elif idx >= self.__count:
            raise IndexError('Specified index is out of range!')

        elif idx > 0:

            curr = self.head
            position = idx

            while position > 1:
                curr = curr.next_node
                position -= 1

            # previous_node (curr) -> goal -> next_node
            previous_node = curr
            next_node =  curr.next_node.next_node
            

            previous_node.next_node = next_node
            if next_node: next_node.prev_node = previous_node
            self.__count -= 1


        else: raise IndexError('Format of index not accepted!')

    def __repr__(self):
        
        ret_l = []
        curr = self.head

        while curr:
            # why does it blow up?
            # print(curr)
            if curr == self.head:
                ret_l.append(f'Head is {curr.data}')

            elif curr.next_node == None:
                ret_l.append(f'Tail is {curr.data}')

            else: 
                ret_l.append(f'Node = {curr.data}')

            curr = curr.next_node

        return '\n -> '.join(ret_l)



doubly_linked = DoublyLinkedList()

print(Node(5))
for i in range(6):
    doubly_linked.add_node(i)

print(doubly_linked)
doubly_linked.size()

doubly_linked.remove_idx(3)

