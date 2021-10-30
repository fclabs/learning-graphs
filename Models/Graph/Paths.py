from .Graph import Graph

class Paths:
    def __init__(self, graph: Graph ) -> None:
        self.graph = graph

    def DepthFirstPath(self, v: int) -> list :
        
        ## Generate a list of visited vertices init in None
        visited = [ None for i in range( self.graph.v_cnt ) ]

        self._dfp( self.graph , visited , v , v ) 

        ## Return all the vertices who was visited
        return [ n for n in range( self.graph.v_cnt ) if visited[n] is not None ]

    @classmethod
    def _dfp( cls, graph: Graph, visited: list, vert: int , v_from: int):
        
        # Check if the node was visited
        if(visited[vert] is None):
            ## Node not visited in the past
            # Mark node as visited
            visited[vert] = v_from

            # get list of adjacencies
            for v_next in graph.adjacents( vert ):
                cls._dfp( graph, visited, v_next, vert )

        return
