"""
An Euler cycle is a cycle that uses every edge in the graph exactly one. 

Wrote a program to find if exist, and Euler cycle for a given Graph G. 
"""

from Models.Graph.Graph import Graph
from Models.Graph.Paths import Paths


class edge_item:
    def __init__(self) -> None:
        

def get_euler_cycle( G: Graph )-> int:
    """
    A vertex in the graph without an even number of edges cannot be in an Euler cycle.
    Because it is a cycle, walking the graph must enter and go out of each vertex,so it requires a pair 
    of edges or n*2 edges to be a Euler cycle candidate.
    Any vertice is equal as good to start a search because all must be part
    """



    ## First, check that each vertix has an even number of edges
    check=True
    for i in range(G.v_cnt):
        if len(G.vertices[i]) % 2 == 1:
            check=False
            break
    
    if not check : return None

    ## Setup a structure to keep track of edge
    edges = set()

    
    




