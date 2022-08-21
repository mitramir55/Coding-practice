from csv import Dialect


class Node:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name
    def __str__(self) -> str:
        return self.name

class Edge:
    def __init__(self, scr, dest) -> None:
        self.scr = scr
        self.dest = dest

    def __str__(self) -> str:
        return f'from {self.scr} to {self.dest}'

    def get_source(self):
        return self. scr

    def get_dest(self):
        return self.dest

class Digraph:
    def __init__(self) -> None:
        self.edges = {}

    def add_node(self, node):

        # find duplicate!
        if node in self.edges:
            raise ValueError('duplicate node! Already have this!')

        else:
            self.edges[node] = []
        
    def add_edge(self, edge):

        src = edge.get_source()
        dest = edge.get_dest()

        # both target and source have to be in the edges dictionary
        if not src in self.edges:
            raise ValueError('Source node not in graph.')
        if not dest in self.edges:
            raise ValueError('Destination node not in graph.')

        self.edges[src].append(dest)

    def get_children(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.edges

    def get_node(self, name):
        for node in self.edges:
            if node.get_name()==name:
                return node
        raise ValueError(f'node {name} not in edges dict!')

    def __str__(self) -> str:
        result = ' '

        for node in self.edges:
            for target in self.edges[node]:
                result += node.get_name() + ' -> ' + target.get_name() + '\n'

            return result


class Graph(Digraph):
    def add_edge(self, edge):

        Digraph.add_edge(self, edge)

        reversed_edge = Edge(scr=edge.get_source(), dest=edge.get_dest())
        Digraph.add_edge(self, reversed_edge)

def build_city_graph(graph_type):

    cities = ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles')

    g = graph_type()

    # add the nodes
    for name in cities:
        g.add_node(Node(name))

    g.add_edge(Edge(g.get_node('Boston'), g.get_node('Providence')))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('Boston')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('New York'), g.get_node('Chicago')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Denver')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))
    return g


def print_path(path):

    result = ' '
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path)-1:
            result += ' -> '
    return result


### ==================== SHORTEST PATH? ======================

# depth first search
def DFS(graph, start, end, path, shortest):

    path = path + [start]
    print('current path = ', print_path(path))

    if end == start: return path
    
    for node in graph.get_children(start):
        # avoid cycles
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest=None)
                if new_path != None: shortest = new_path

        else: print('Already visited!')

    return shortest

def get_shortest_path(graph, start, end):
    return DFS(graph, start, end, path=[], shortest=None)

def test_shortest_path(source, dest):

    graph = build_city_graph(Digraph)
    shortest_path = get_shortest_path(
        graph,
        start=graph.get_node(source),
        end=graph.get_node(dest)
        )

    if shortest_path:
        print(f'shortest path from {source} to {dest} is ')
        print(print_path(shortest_path))

    else: print(f'No path from {source} to {dest}!')


test_shortest_path('Boston', 'Phoenix')



# Breadth first search

def BFS(graph, start, end, print_queue=True):

    init_path = [start]
    path_queue = [init_path]

    while path_queue != []:

        # print current queue
        if print_queue:
            print('length of queue = ', len(path_queue))

            for path in path_queue: 
                print(print_path(path))

        # get the last one
        temp_path = path_queue.pop(0)
        end_node = temp_path[-1]
        if end_node == end:
            return temp_path

        for next_node in graph.get_children(end_node):
            print(type(next_node))
            if next_node not in temp_path:
                new_path = temp_path + [next_node]
                path_queue.append(new_path)
            else: print('already visited!')

    return None

def get_shortest_path(graph, start, end):
    return BFS(graph, start, end, print_queue=True)



test_shortest_path(source='Boston', dest='Phoenix')

# listt = [['boston']]
# f = listt.pop(0)
# f
# listt



