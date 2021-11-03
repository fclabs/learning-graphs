import unittest

from Graph.Graph import Graph
from Graph.Paths import Paths

class TestGraph(unittest.TestCase):
    
    def test_bfp_single_node(self):
    # Setup the graph
        g = Graph(1)
        p = Paths( graph=g )

        self.assertCountEqual( p.BreadthFirstPaths(0) , [0]  )

    def test_bfp_line_graph(self):
        # Setup the graph
        g = Graph(7)
        g.addEdge( 0 , 1 )
        g.addEdge( 0 , 2 )
        g.addEdge( 0 , 5 )
        g.addEdge( 0 , 6 )
        g.addEdge( 4 , 6 )
        g.addEdge( 4 , 5 )
        g.addEdge( 4 , 3 )
        g.addEdge( 5 , 3 )
    
        p = Paths( graph=g )

        self.assertCountEqual( p.BreadthFirstPaths(0) , list(range(7))  )

    def test_dpf_ignore_sep(self):
        # Setup the graph
        g = Graph(10)
        g.addEdge( 0 , 1 )
        g.addEdge( 0 , 2 )
        g.addEdge( 0 , 5 )
        g.addEdge( 0 , 6 )
        g.addEdge( 4 , 6 )
        g.addEdge( 4 , 5 )
        g.addEdge( 4 , 3 )
        g.addEdge( 5 , 3 )
        g.addEdge( 7 , 8 )
        g.addEdge( 5 , 3 )
        g.addEdge( 7 , 9 )
    
        p = Paths( graph=g )

        self.assertCountEqual( p.BreadthFirstPaths(0) , list(range(7))  )
        self.assertCountEqual( p.BreadthFirstPaths(7) , [ 7,8,9]  )
        self.assertCountEqual( p.BreadthFirstPaths(8) , p.connectedNodesTo(9) )

if __name__=='__main__':
    unittest.main()