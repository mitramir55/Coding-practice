class Node:
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    def __str__(self) -> str:
        return f'this node has {self.data} as its data. Its next node is {self.next_node}'

class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.__count = 0

    def is_empty(self):
        return self.head is None


    def get_node_at_idx(self, idx):

        position = 0
        curr = self.head
        if idx == 0: return curr
        while position < idx:
            curr = curr.next_node
            position += 1

        return curr

    def add_node(self, data):
        # we don't check for duplicates
        # if self.search(): return 'We already have this!'
        new_node = Node(data=data, next_node=self.head)
        self.head = new_node
        self.__count += 1

    def search(self, goal):
        curr = self.head
        i = 0
        for i in range(self.__count):
            if curr.data == goal:
                return (f'found it! it is element {i+1}')
            curr = curr.next_node
        return None
        
    def insert(self, data, idx):

        # if it was out of range
        if idx > self.__count:
            raise IndexError(' Index out of range !!!')

        # if we want to insert in the beginning
        if idx == 0: self.add_node(data)
        elif idx >= 0:    
            curr = self.head
            new_node = Node(data)
            position = idx

            # trying to find the previous node  to 
            # our new node
            while position > 1:
                curr = curr.next_node
                position -= 1

            previous_node = curr
            next_node = curr.next_node

            previous_node.next_node = new_node
            new_node.next_node = next_node
            self.__count += 1
        else: raise IndexError('Nope! this is not an accepted format for index!') 


    def remove(self, key):

        if self.head.data == key: 
            self.head = self.head.next_node
            self.__count -= 1

        elif self.search(goal=key):
            curr = self.head

            while curr:
                next_node = curr.next_node

                if key == next_node.data:
                    curr.next_node = next_node.next_node
                    self.__count -= 1
                    break

                curr = curr.next_node

        else: raise ValueError('No value like this exists!')
    
    def remove_idx(self, idx):
        if idx == 0:
            self.head = self.head.next_node
            self.__count -= 1

        elif idx >= self.__count: raise IndexError('Index out of range!')

        elif idx > 0:

            position = idx
            curr = self.head

            while position > 1:
                curr = curr.next_node
                position -= 1

            previous_node = curr
            previous_node.next_node = previous_node.next_node.next_node

            self.__count -= 1

        else: raise IndexError('Index not in a correct format!')

    def __iter__(self):
        curr = self.head

        while curr:
            yield curr
            curr = curr.next_node

    def __repr__(self) -> str:
        
        ret_l = []

        curr = self.head
        while curr:
            if curr is self.head:
                ret_l.append(f'The head is {curr.data}')
            elif curr.next_node is None:
                ret_l.append(f'The tail is {curr.data}')
            else:
                ret_l.append(f'Node: {curr.data}')
            curr = curr.next_node

        return '\n ->'.join(ret_l)
    def __len__(self):
        count = 0 
        curr = self.head
        while curr:
            count +=1
            curr = curr.next_node
        return count

singly_list = SinglyLinkedList()

for i in range(10):
    singly_list.add_node(i)

singly_list.__len__()
singly_list.search(5)

print(singly_list)

singly_list.remove(5)
singly_list.remove_idx(5)

singly_list.insert(10, 8)


