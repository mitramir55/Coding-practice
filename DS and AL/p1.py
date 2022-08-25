from dataclasses import dataclass
from platform import node


class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next

    def define_data(self, data):
        self.data = data

node_a = Node(data=6, next=3)
node_b = Node(data=3, next=4)
node_c = Node(data=4, next=2)
node_c = Node(data=2, next=1)

node_a.define_data(data=5)

node_a.data

class LinkedList:
    def __init__(self) -> None:
        self.nodes = []

    def create_node(self, data, next):
        node = Node(data, next)
        self.nodes.append(node)

    def count_nodes(self):
        return len(self.nodes)


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def count_nodes(head):
    
    count = 1
    node_ = head
    while node_.next is not None:
        count+=1
        node_ = node_.next
    return count

nodeA = Node(6)
nodeB = Node(4)
nodeC = Node(2)
nodeD = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD

count_nodes(head=nodeA)


