


from typing import Iterator


class Graph:
    def __init__(self, v_cnt: int) -> None:

        if v_cnt < 0 : raise ValueError('Graph init only accepts integer bigger or equal than zero')

        self.vertices=list()
        self.v_cnt = v_cnt
        for i in range(v_cnt):
            self.vertices.append( list() )
    
    def add_edge(self, v: int , w: int ) -> None:
        
        self.vertices[v].append( w )
        self.vertices[w].append( v )
    
    def adjacents(self, v: int ) -> Iterator :
        
        if self.v_cnt == 0 : raise ValueError('Empty Graph has no vertices')

        return iter(self.vertices[v])       