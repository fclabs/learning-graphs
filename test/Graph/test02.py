import unittest

from Graph.Graph import Graph
from Graph.Paths import Paths

class TestGraph(unittest.TestCase):
    
    def test_dpf_single_node(self):
    # Setup the graph
        g = Graph(1)

        p = Paths( graph=g )

        self.assertCountEqual( p.get_connected_verticces_dfp(0) , [0]  )

    def test_depth_path_first(self):

        # Setup the graph
        g = Graph(7)
        g.add_edge( 0 , 1 )
        g.add_edge( 0 , 2 )
        g.add_edge( 0 , 5 )
        g.add_edge( 0 , 6 )
        g.add_edge( 4 , 6 )
        g.add_edge( 4 , 5 )
        g.add_edge( 4 , 3 )
        g.add_edge( 5 , 3 )
    
        p = Paths( graph=g )

        self.assertCountEqual( p.get_connected_verticces_dfp(0) , list(range(7))  )

    def test_dpf_ignore_sep(self):
        # Setup the graph
        g = Graph(10)
        g.add_edge( 0 , 1 )
        g.add_edge( 0 , 2 )
        g.add_edge( 0 , 5 )
        g.add_edge( 0 , 6 )
        g.add_edge( 4 , 6 )
        g.add_edge( 4 , 5 )
        g.add_edge( 4 , 3 )
        g.add_edge( 5 , 3 )
        g.add_edge( 7 , 8 )
        g.add_edge( 5 , 3 )
        g.add_edge( 7 , 9 )
    
        p = Paths( graph=g )

        self.assertCountEqual( p.get_connected_verticces_dfp(0) , list(range(7))  )
        self.assertCountEqual( p.get_connected_verticces_dfp(7) , [ 7,8,9]  )
        self.assertCountEqual( p.get_connected_verticces_dfp(8) , p.get_connected_verticces_dfp(9) )

if __name__=='__main__':
    unittest.main()