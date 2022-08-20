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

        else:
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
        Digraph.add_edge(edge)
        reversed_edge = Edge(scr=edge.scr, dest=edge.dest)
        Digraph.add_edge(reversed_edge)

def build_city_graph(graph_type):

    cities = ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles')

    g = graph_type()

    # add the nodes
    for name in cities:
        g.add_node(Node(name))

    g.add_edge(g.get_node('Boston'), g.get_node('Providence'))
    g.add_edge(g.get_node('Boston'), g.get_node('New York'))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g