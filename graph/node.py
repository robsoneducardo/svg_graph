import xml.etree.ElementTree as ET
from typing import List
import numpy as np


class Node:
    x: float  # deprecated
    y: float  # deprecated
    r: float
    name: str

    def __init__(self, x: float = 0.0, y: float = 0.0, r: float = 10.0, name: str = "Node"):
        self.x = x
        self.y = y
        self.pos = np.array((float(x), float(y)))
        self.r = r
        self.name = name

    def __str__(self):
        return f'{self.name}({self.pos[0]:.2f}, {self.pos[1]:.2f})<{self.r:.2f}>'

    @classmethod
    def find_nodes(cls, filename) -> List:
        tree = ET.parse(filename)
        nodes = []
        # find_edges(cls, nodes, filename)

        for el in tree.iter():
            if 'ellipse' in el.tag:
                nodes.append(Node(x=float(el.attrib['cx']), y=float(el.attrib['cy']),
                                  r=(float(el.attrib['rx']) + float(el.attrib['ry'])) / 2))
            if 'circle' in el.tag:
                nodes.append(Node(x=float(el.attrib['cx']), y=float(el.attrib['cy']),
                                  r=float(el.attrib['r'])))

        for el in tree.iter():
            if 'tspan' in el.tag:
                el_pos = np.array((float(el.attrib['x']), float(el.attrib['y'])))
                for node in nodes:
                    print(el.text, " - ", np.linalg.norm(el_pos - node.pos), " - ", node.r)
                    if np.linalg.norm(el_pos - node.pos) < node.r:
                        node.name = el.text
                        break

        return nodes
