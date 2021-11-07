"""
Defining a tree as a connected graph with no cycles. Where 
    Diameter: is longest simple path in the graph.
    Center: Is vertex such that its maximum distance from any other vertex is minimized.

Wrote a program to find to find the diameter and center of a tree. 
"""

from Models.Graph.Graph import Graph
from Models.Graph.Paths import Paths
from copy import deepcopy
from random import randint
from time import perf_counter

def get_center( G: Graph )-> int:

    if(G.v_cnt == 1): return [0]

    ## Process G.vertices
    g=deepcopy(G)
    verts = { i: len(G.vertices[i]) for i in range(G.v_cnt) if len(G.vertices[i])>0 }  
    
    ## While the dict has something
    to_delete = list()
    last = []
    cont = True
    while(cont):
        ## Search for nodes to delete and candidates
        to_delete.clear()
        last.clear()
        for k,v in verts.items():
            if v==1:
                to_delete.append(k)
            elif v>1:
                last.append(k)
        
        if len(last)<2:
            cont = False
            if len(last)==0:
                last = to_delete

        ## Remove edges
        for i in to_delete:
            ## Check last removed adj to avoid try to delete it again
            ## This will happen only if len(to_delete)==2
            if(len(g.vertices[i])>0):
                adj = list(g.adjacents(i))[0]
                g.remove_edge( i , adj )  
                del(verts[i])
                verts[adj] -= 1

    return last


def get_diameter( G: Graph )-> list:
    """
    The diameter must start and end on a leaf. This can be demostrated by:

    - n is the start of the diameter path,
    - n is not a leaf, so it has more than one adjacency
    
    then if it is the start or termination of the diameter path, one of the adjacencies
    must be part of the diameter. the other adjacency is not part of the diameter but it can be 
    added to it what revoke the assuption of n being the start of end of the diameter path.

    Based on the algorith used to calculate the center, the diameter will always must contain the 
    centers of the tree. 

    """

    ## if G has less than three nodes, return all the vertices
    if(G.v_cnt<3): return list(range(G.v_cnt))

    ## Get the centers of the graph
    c = get_center(G)

    ## Search a list of leafs
    leafs = [i for i in range(G.v_cnt) if len(G.vertices[i])==1 ]
    p = Paths(G)

    max = ( -1 , None )
    sec = max
    ## Find the two longest different paths
    i=0
    while(i<len(leafs)):

        ## MEasure path length from one of the centers to all the leafs        
        path = p.get_path_to_vertix_dfp( c[0], leafs[i] )
        if(len(path)>max[0]):
            sec=max
            max = ( len(path) , path )
        elif (len(path)>sec[0]):
            sec = ( len(path) , path )
        i += 1

    ## Reverse sec and concatenate max, except the repited center
    print(max)
    print(sec)
    return [ x for x in range(len(sec[1])-1, 0,-1)] + max[1]

if __name__=='__main__':

    g = Graph(12)

    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(1,4)
    g.add_edge(5,2)
    g.add_edge(6,2)
    g.add_edge(6,7)
    g.add_edge(8,7)
    g.add_edge(8,9)
    g.add_edge(10,9)
    g.add_edge(11,9)

    print(g.vertices)
    print('Center:',get_center(g))
    print('Diameter:',get_diameter(g)) 
    ## Single Node
    g = Graph(1)
    print(g.vertices)
    print('Center:',get_center(g)) 
    print('Diameter:',get_diameter(g)) 

    # Two nodes
    g = Graph(2)
    g.add_edge(0,1)
    print(g.vertices)
    print('Center:',get_center(g))
    print('Diameter:',get_diameter(g)) 
 
    ## small tree
    n=100
    g = Graph(n)
    for i in range(1,n):
        node=randint(0,i)
        g.add_edge(randint(0,i-1),i)
    print(g.vertices)
    t0 = perf_counter()
    print('Center ',n,' nodes:',get_center(g))
    print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')
    t0 = perf_counter()
    print('Diameter:',get_diameter(g)) 
    print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')

    ## mid tree
    n=1000
    g = Graph(n)
    for i in range(1,n):
        node=randint(0,i)
        g.add_edge(randint(0,i-1),i)
    t0 = perf_counter()
    print('Center ',n,' nodes:',get_center(g))
    print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')
    t0 = perf_counter()
    print('Diameter:',get_diameter(g)) 
    print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')

    ## large tree
    n=50000
    g = Graph(n)
    for i in range(1,n):
        node=randint(0,i)
        g.add_edge(randint(0,i-1),i)
    t0 = perf_counter()
    print('Center ',n,' nodes:',get_center(g))
    print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')
    t0 = perf_counter()
    print('Diameter:',get_diameter(g)) 
    print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')

    # ## xlarge tree
    # n=1000000
    # g = Graph(n)
    # for i in range(1,n):
    #     node=randint(0,i)
    #     g.add_edge(randint(0,i-1),i)
    # t0 = perf_counter()
    # print('Center ',n,' nodes:',get_center(g))
    # print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')
    # t0 = perf_counter()
    # print('Diameter:',get_diameter(g)) 
    # print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')

    # # ## xxlarge tree
    # n=10000000
    # g = Graph(n)
    # for i in range(1,n):
    #     node=randint(0,i)
    #     g.add_edge(randint(0,i-1),i)
    # t0 = perf_counter()
    # print('Center ',n,' nodes:',get_center(g))
    # print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')
    # t0 = perf_counter()
    # print('Diameter:',get_diameter(g)) 
    # print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')

    ## large tree depth=1
    n=50000
    g = Graph(n)
    for i in range(1,n):
        g.add_edge(0,i)
    t0 = perf_counter()
    print('Center ',n,'nodes d=1:',get_center(g))
    print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')

    ## large tree depth=n-1
    n=50000
    g = Graph(n)
    for i in range(1,n):
        g.add_edge(i-1,i)
    t0 = perf_counter()
    print('Center ',n,'nodes d=n-1:',get_center(g))
    print('Elapsed: ', (perf_counter()-t0)*1000, 'ms')