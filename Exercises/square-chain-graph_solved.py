
from typing import Optional

class Node:
    pass

class Node:
    def __init__(self, from_node: Node , end_in : int ) -> None:
        self.next = [None]*10 ## Ref to leaves
        self.end_in = end_in
        self.parent = from_node
        self.mark = None

        self.set_next( 0 , self ) ## Next digit cero 

    def set_next( self, num, node: Node ):
        self.next[num] = node

    def mark_as(self, mark:int ) -> None :
        self.mark = mark

def get_digits( n : int ) -> list :
    res = []
    while n > 0:
        res += [n%10]
        n = n // 10
    res.sort()
    return res

def get_node_n( root : Node, num:int ) -> Node :
    start = root
    digits = get_digits(num)

    for d in digits:
        if(start.next[d] is None):
            start.next[d] = Node(from_node=start, end_in=start.end_in+ d*d )
        start = start.next[d]

    return start

def calc_89( n: int ) -> int :
    count = 0 
    node:Node = None
    ## Setup graph root and end nodes
    root = Node( from_node=None, end_in=0)

    for i in range(1,n+1):
        print("i", i)
        node = get_node_n( root,  i )
        explored = [ node ]
        cont = True

        while cont :
            ## Check if this value was already explored 
            #print( "Node", node.end_in , "node.mark", node.mark,  "explored:", len(explored) ) 
            if node.mark is not None:
                ## Already explored
                cont = False
            elif node.end_in == 89 or node.end_in == 1:
                node.mark_as( node.end_in )
                cont = False
            else:
                node = get_node_n( root, node.end_in )
                explored += [ node ]

        ## Mark the explored
        for n in explored:
            n.mark_as( node.mark )

        if(node.mark == 89):
            count += 1

    return count

print( "counted", calc_89(10000000) )

