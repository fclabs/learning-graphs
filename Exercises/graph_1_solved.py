"""
Exercise 1:

There is a matrix M with N rows and M columns where each cell represent a color (any int value). 
Lets define a color cluster as a group of cells that touch each other (top,bottom,left,right) and 
share the same color. Color are represented b
If two clusters share the same color but they are not touching between them, must be considered a different 
cluster.

Objective:
Write a funtion that count how many clusters you have defined in the matrix.
"""

from pprint import pprint
from random import randint
from time import perf_counter

from Models.Graph.Graph import Graph
from Models.Graph.Paths import Paths

class ClusterCounter:
    def __init__(self, A : list ) -> None:
        ## Setup vars
        self.A = A
        self.len_x = len(A[0])
        self.len_y = len(A)
        self.G = Graph( self.len_x * self.len_y )
        self.P = Paths( self.G )
        self.vert_cluster = [None]*(self.len_x*self.len_y)
        self._make_graph()

    def _get_vertix(self,x,y):
        return self.len_x*y+x
    
    def _get_color(self, x , y):
        return self.A[y][x]

    def _make_graph(self) -> None:
        ## Explore all the matrix
        for y in range(self.len_y):
            for x in range(self.len_x):
                current_color = self.A[y][x]

                ## Check adjacencies
                # down
                if (y < (self.len_y-1)) and current_color == self.A[y+1][x]:    
                    self.G.add_edge( self._get_vertix(x,y), self._get_vertix(x,y+1) ) 
                if (x < (self.len_x-1)) and current_color == self.A[y][x+1]:    
                    self.G.add_edge( self._get_vertix(x,y), self._get_vertix(x+1,y) ) 

    def count(self) -> int:
        i=0
        cluster=0
        while i<len(self.vert_cluster):
            if(self.vert_cluster[i] is None):
                cluster += 1
                ## Find cluster verts
                for v in self.P.get_connected_vertices_bfp(i):
                    self.vert_cluster[v] = cluster
            i += 1
        return cluster


def count_clusters( A : list ) -> int:

    cc = ClusterCounter(A)
    return cc.count()


if __name__=='__main__':

    case1 = [ [ 1,2,3 ], [1,2,1], [3,4,1], [3,3,4], [3,4,4], [1,2,1],[1,1,1],[3,3,1] ]
    pprint(case1)
    
    case2 = [ [1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]  ]
    pprint(case2)

    case3 = []
    for i in range(20):
        l = [1,2]*10
        if(i%2==0):
            l.append(l.pop(0))
        case3.append(l)
    pprint(case3)
    
    case4 = []
    for i in range(10):
        l = []
        for j in range(10):
            l.append( randint(1,4) )
        case4.append(l)
    pprint(case4)
            
    case5 = []
    for i in range(100):
        l = []
        for j in range(100):
            l.append( randint(1,6) )
        case5.append(l)

    case6 = []
    for i in range(1000):
        l = []
        for j in range(1000):
            l.append( randint(1,20) )
        case6.append(l)


    print('Case 1')
    start=perf_counter()
    res=count_clusters( case1 )
    stop=perf_counter()
    print(f'Clusters: {res}')
    print(f'Execution took: {(stop-start)*1000} ms\n')

    print('Case 2')
    start=perf_counter()
    res=count_clusters( case2 )
    stop=perf_counter()
    print(f'Clusters: {res}')
    print(f'Execution took: {(stop-start)*1000} ms\n')

    print('Case 3')
    start=perf_counter()
    res=count_clusters( case3 )
    stop=perf_counter()
    print(f'Clusters: {res}')
    print(f'Execution took: {(stop-start)*1000} ms\n')

    print('Case 4')
    start=perf_counter()
    res=count_clusters( case4 )
    stop=perf_counter()
    print(f'Clusters: {res}')
    print(f'Execution took: {(stop-start)*1000} ms\n')

    print('Case 5')
    start=perf_counter()
    res=count_clusters( case5 )
    stop=perf_counter()
    print(f'Clusters: {res}')
    print(f'Execution took: {(stop-start)*1000} ms\n')

    print('Case 6')
    start=perf_counter()
    res=count_clusters( case6 )
    stop=perf_counter()
    print(f'Clusters: {res}')
    print(f'Execution took: {(stop-start)*1000} ms\n')
