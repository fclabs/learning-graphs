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



def count_clusters( A : list ) -> int:
    pass

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
