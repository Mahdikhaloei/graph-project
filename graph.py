"""
Author: [ Mahdi Khaloei ]
Date: [ 12/04/2023 ]

for run this module please do following:
    1. python3 -m venv .venv
    2. source .venv/bin/activate
    3. pip3 install -r requiremetns.txt
    4. python graph.py
    
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


node = [(0,2),(0,3),(8,5),(5,6),(1,2),(5,1),(1,0),(0,4),(4,8),(4,3),(8,7),(7,3),(6,2),(7,6)]

my_graph = Graph(node)

shared_nodes = my_graph.get_shared_nodes()
print("Shared nodes:", shared_nodes)

nx.draw(my_graph.graph, with_labels=True)
plt.show()

