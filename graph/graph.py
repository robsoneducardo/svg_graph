# import xml.etree.ElementTree as ET

from graph.node import Node
from graph.edge import Edge

Node()


class Graph:

    nodes = []
    edges = []


    def __init__(self, filename: str):
        self.nodes = Node.find_nodes(filename)
        self.edges = Edge.find_edges(filename, nodes=self.nodes)


    def __str__(self):
        repr = 'Nodes:'
        for n in self.nodes:
            repr += '\n'
            repr += str(n)
        repr += '\n\nEdges:'
        for e in self.edges:
            repr += '\n'
            repr += str(e)
        repr += '\n'
        return repr
