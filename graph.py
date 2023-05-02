"""
Author: [ Mahdi Khaloei ]
Date: [ 12/04/2023 ]

for run this module please do following:
    1. python3 -m venv .venv
    2. source .venv/bin/activate
    3. pip3 install -r requiremetns.txt
    4. python graph.py
    
libraries
----------
networkx
matplotlib

    
Parameters
----------
node: list
    A list of edges to create the graph. Each edge consists of two integers representing 
    the identifiers of the two nodes connected by that edge.

Attributes
----------
graph: object
    A graph object created using the NetworkX library.

Methods
-------
get_shared_nodes():
    Finding pairs of nodes that share a common vertex
    
"""

import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, node):
        self.graph = nx.Graph()
        self.graph.add_edges_from(node)

    def get_shared_nodes(self):
        nodes = list(self.graph.nodes())
        shared_nodes = []
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                common_neighbors = set(self.graph.neighbors(nodes[i])) & set(self.graph.neighbors(nodes[j]))
                if len(common_neighbors) > 0:
                    shared_nodes.append((nodes[i], nodes[j]))
        return shared_nodes


node = [
        (1,2),(1,3),(1,4),
        (2,7),(2,8),(2,1),
        (3,5),(3,9),(3,1),
        (4,1),(4,6),(4,10),
        (5,6),(5,3),(5,8),
        (6,4),(6,5), (6,7),
        (7,6),(7,2),(7,9),
        (8,2),(8,5),(8,10),
        (9,7),(9,10),(9,3),
        (10,4),(10,9),(10,8)
        ]

my_graph = Graph(node)

shared_nodes = my_graph.get_shared_nodes()
print("Shared nodes:", shared_nodes)

nx.draw(my_graph.graph, with_labels=True)
plt.show()

