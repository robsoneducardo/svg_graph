import xml.etree.ElementTree as ET
import numpy as np
from typing import List



class Edge:


    @classmethod
    def find_edges(cls, filename, nodes):
        root = ET.parse(filename)
        edges = []

        for el in root.iter():
            if 'path' in el.tag:
                points = el.attrib['d'].split(sep=' ')[1:]
                p_initial = points[0].split(sep=',')
                p_final = points[-1].split(sep=',')
                inicio =(float(p_initial[0]), float(p_initial[1]))
                final = (float(p_final[0]), float(p_final[1]))
                for node in nodes:
                    pass # verifica a distancia e atualiza.


        return edges

