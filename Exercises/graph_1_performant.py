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

class Cluster():
    def __init__(self,id) -> None:
        self.id = id
    def __str__(self):
        return str(self.id)


def count_clusters( A : list ) -> int:

    len_x = len(A[0])
    len_y = len(A)

    cluster_id = 0
    ClusterMap = [None]*(len_x*len_y)

    for y in range(len_y):
        for x in range(len_x):

            left_cluster_id=None
            left_color=None
            my_color = A[y][x]

            ## Check left
            if (x>0) and (my_color == A[y][x-1]):
                ## Left with same color. Copy his Organization
                ClusterMap[len_x*y+x] = ClusterMap[len_x*y+x-1]
                left_cluster_id = ClusterMap[len_x*y+x].id
                left_color=my_color
            
            if (y>0):
                ## Check top
                if((my_color == A[y-1][x])):
                    ## top cell has the same color.
                    ## Check if the left color is the same
                    if(left_color is not None):
                        if(left_color == A[y-1][x]):
                            ## Check if the cluster_id is the same
                            ## Left, Top and current have the same color
                            ## Let's check the cluster_id
                            ClusterMap[len_x*(y-1)+x].id = left_cluster_id
                    else:
                        ## Left didn't match my color            
                        ## Share the same cluster with the top row
                        ClusterMap[len_x*y+x] = ClusterMap[len_x*(y-1)+x]

            ## If we reach here with ClusterMap[len_x*y+x] == None
            ## Create new cluster with new id
            if ClusterMap[len_x*y+x] is None:
                cluster_id += 1
                ClusterMap[len_x*y+x] = Cluster( cluster_id )
                    
    ## Get all the IDs in a list
    return len(list(dict.fromkeys( [ clu.id for clu in ClusterMap ] )))



if __name__=='__main__':

    # case1 = [ [ 1,2,3 ], [1,2,1], [3,4,1], [3,3,4], [3,4,4], [1,2,1],[1,1,1],[3,3,1] ]
    # pprint(case1)
    
    case2 = [ [1,1,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,2,2,1],[1,1,1,1,3]  ]
    pprint(case2)

    # case3 = []
    # for i in range(20):
    #     l = [1,2]*10
    #     if(i%2==0):
    #         l.append(l.pop(0))
    #     case3.append(l)
    # pprint(case3)
    
    case4 = []
    for i in range(7):
        l = []
        for j in range(5):
            l.append( randint(1,4) )
        case4.append(l)
    pprint(case4)
            
    # case5 = []
    # for i in range(100):
    #     l = []
    #     for j in range(100):
    #         l.append( randint(1,6) )
    #     case5.append(l)

    # case6 = []
    # for i in range(1000):
    #     l = []
    #     for j in range(1000):
    #         l.append( randint(1,20) )
    #     case6.append(l)

    case7 = [ [1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,2,2,1,1,1,1,3]  ]
    pprint(case7)

    case8 = [ [1,1],[1,1],[1,1],[2,1],[2,1],[2,1],[2,1],[2,2],[2,1],[1,1],[1,3]  ]
    pprint(case8)

    # print('Case 1')
    # start=perf_counter()
    # res=count_clusters( case1 )
    # stop=perf_counter()
    # print(f'Clusters: {res}')
    # print(f'Execution took: {(stop-start)*1000} ms\n')


    print('Case 2')
    start=perf_counter()
    res=count_clusters( case2 )
    stop=perf_counter()
    print(f'Clusters: {res}')
    print(f'Execution took: {(stop-start)*1000} ms\n')

    # print('Case 3')
    # start=perf_counter()
    # res=count_clusters( case3 )
    # stop=perf_counter()
    # print(f'Clusters: {res}')
    # print(f'Execution took: {(stop-start)*1000} ms\n')

    print('Case 4')
    start=perf_counter()
    res=count_clusters( case4 )
    stop=perf_counter()
    print(f'Clusters: {res}')
    print(f'Execution took: {(stop-start)*1000} ms\n')

    # print('Case 5')
    # start=perf_counter()
    # res=count_clusters( case5 )
    # stop=perf_counter()
    # print(f'Clusters: {res}')
    # print(f'Execution took: {(stop-start)*1000} ms\n')

    # print('Case 6')
    # start=perf_counter()
    # res=count_clusters( case6 )
    # stop=perf_counter()
    # print(f'Clusters: {res}')
    # print(f'Execution took: {(stop-start)*1000} ms\n')

    print('Case 7')
    start=perf_counter()
    res=count_clusters( case7 )
    stop=perf_counter()
    print(f'Clusters: {res}')
    print(f'Execution took: {(stop-start)*1000} ms\n')

    print('Case 8')
    start=perf_counter()
    res=count_clusters( case8 )
    stop=perf_counter()
    print(f'Clusters: {res}')
    print(f'Execution took: {(stop-start)*1000} ms\n')