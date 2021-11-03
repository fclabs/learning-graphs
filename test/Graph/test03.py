import unittest

from Graph.Graph import Graph
from Graph.Paths import Paths

class TestGraph(unittest.TestCase):
    
    def test_path_single_node(self):
    # Setup the graph
        g = Graph(1)
        p = Paths( graph=g )

        self.assertCountEqual( p.get_path_to_vertix_dfp(0, 0) , [0]  )

    def test_path_line_graph(self):
    # Setup the graph
        g = Graph(5)
        g.add_edge(0,1)
        g.add_edge(1,2)
        g.add_edge(2,3)
        g.add_edge(4,3)

        p = Paths( graph=g )

        self.assertListEqual( p.get_path_to_vertix_dfp(0, 4) , [0,1,2,3,4]  )

    def test_path_simple_graph(self):
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

        p = Paths( graph=g )

        self.assertListEqual( p.get_path_to_vertix_dfp(0, 4) , [0,5,4]  )

    def test_path_no_path(self):
        # Setup the graph

        g = Graph(10)
        g.add_edge( 0 , 1 )
        g.add_edge( 1 , 2 )
        g.add_edge( 0 , 2 )
        g.add_edge( 3 , 6 )
        g.add_edge( 4 , 6 )
        g.add_edge( 4 , 5 )
        g.add_edge( 4 , 3 )
        g.add_edge( 5 , 3 )

        p = Paths( graph=g )

        self.assertListEqual( p.get_path_to_vertix_dfp(0, 4) , []  )


    def test_path_adj(self):
        # Setup the graph

        g = Graph(10)
        g.add_edge( 0 , 1 )
        g.add_edge( 1 , 2 )
        g.add_edge( 0 , 2 )


        p = Paths( graph=g )

        self.assertListEqual( p.get_path_to_vertix_dfp(0, 1) , [0,1]  )

    def test_path_middle(self):
        # Setup the graph

        g = Graph(3)
        g.add_edge( 0 , 1 )
        g.add_edge( 1 , 2 )


        p = Paths( graph=g )

        self.assertListEqual( p.get_path_to_vertix_dfp(0, 1) , [0,1]  )
        self.assertListEqual( p.get_path_to_vertix_dfp(1, 0) , [1,0]  )
        self.assertListEqual( p.get_path_to_vertix_dfp(1, 2) , [1,2]  )
        self.assertListEqual( p.get_path_to_vertix_dfp(2, 1) , [2,1]  )

if __name__=='__main__':
    unittest.main()