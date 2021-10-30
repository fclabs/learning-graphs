from .Graph import Graph

class Paths:
    def __init__(self, graph: Graph ) -> None:
        self.graph = graph

    def connectedNodesTo(self, v: int) -> list :
        
        ## Generate a list of visited vertices init in None
        visited = [ None for i in range( self.graph.v_cnt ) ]

        self._dfp( self.graph , visited , v , v ) 

        ## Return all the vertices who was visited
        return [ n for n in range( self.graph.v_cnt ) if visited[n] is not None ]

    def pathToNode(self, v_from: int , v_to: int ) -> list :

        # if from and to are the same, return now
        if(v_from == v_to ): return [v_from]

        result = []
        visited = [ None for i in range( self.graph.v_cnt ) ]
        if self._dfpt( self.graph , visited , v_from , v_from , v_to ):
            current = v_to
            while( current != v_from ):
                result.insert( 0 , current )
                current = visited[current]
            result.insert(0, current)
        return result

    @classmethod
    def _dfp( cls, graph: Graph, visited: list, vert: int , v_from: int):
        
        visited[vert] = v_from
        for v_next in [v for v in graph.adjacents( vert ) if visited[v] is None ]:
                cls._dfp( graph, visited, v_next, vert )

        return

    @classmethod
    def _dfpt( cls, graph: Graph, visited: list, vert: int , v_from: int, target : int):
        
        visited[vert] = v_from

        if(target == vert ): return True
        
        for v_next in [v for v in graph.adjacents( vert ) if visited[v] is None ]:
                if cls._dfpt( graph, visited, v_next, vert, target ):
                    return True

        return False