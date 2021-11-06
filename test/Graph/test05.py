import unittest, time
from random import randint

from Graph.Graph import Graph
from Graph.Paths import Paths

import sys
sys.setrecursionlimit(5000)

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3fms' % (self.id(), t*1000))    

    def test_bfp_single_node(self):
    # Setup the graph
        g = Graph(1)
        p = Paths( graph=g )

        self.assertEqual( p.get_clusters_count() , 1  )

    def test_cc_multi_edge(self):
        # Setup the graph
        g = Graph(7)
        g.add_edge( 0 , 1 )
        g.add_edge( 0 , 1 )
        g.add_edge( 0 , 1 )
        g.add_edge( 0 , 1 )
        g.add_edge( 0 , 2 )
        g.add_edge( 0 , 5 )
        g.add_edge( 0 , 5 )
        g.add_edge( 0 , 5 )
        g.add_edge( 0 , 6 )
        g.add_edge( 4 , 6 )
        g.add_edge( 4 , 5 )
        g.add_edge( 4 , 5 )
        g.add_edge( 4 , 5 )
        g.add_edge( 4 , 3 )
        g.add_edge( 5 , 3 )
    
        p = Paths( graph=g )

        self.assertEqual( p.get_clusters_count() , 1  )

    def test_cc_sep1(self):
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

        self.assertEqual( p.get_clusters_count() , 1  )

    def test_cc_sep3(self):
        # Setup the graph
        g = Graph(12)
        g.add_edge( 0 , 1 )
        g.add_edge( 0 , 2 )
        g.add_edge( 0 , 5 )
        g.add_edge( 0 , 6 )
        g.add_edge( 4 , 5 )
        g.add_edge( 4 , 3 )
        g.add_edge( 5 , 3 )
        g.add_edge( 7 , 8 )
        g.add_edge( 7 , 9 )
        g.add_edge( 8 , 9 )
        g.add_edge( 10 , 11 )
    
        p = Paths( graph=g )

        self.assertEqual( p.get_clusters_count() , 3  )

    def test_cc_no_vert(self):
        # Setup the graph
        g = Graph(12)
        p = Paths( graph=g )

        self.assertEqual( p.get_clusters_count() , 12  )

    def test_small_size(self):
        # Setup the graph
        n = 10
        g = Graph(n*n)
        for i in range(n*n*n//2):
            g.add_edge( randint(0,n*n-1), randint(0,n*n-1) )

        p = Paths( graph=g )

        c = p.get_clusters_count()
        self.assertLessEqual( c , n*n  )
        self.assertGreaterEqual( c , 1  )


    def test_mid_size(self):
        # Setup the graph
        n = 50
        g = Graph(n*n)
        for i in range(n*n*n):
            g.add_edge( randint(0,n*n-1), randint(0,n*n-1) )

        p = Paths( graph=g )

        c = p.get_clusters_count()
        self.assertLessEqual( c , n*n  )
        self.assertGreaterEqual( c , 1  )

    def test_large_size(self):
        # Setup the graph
        n = 100
        g = Graph(n*n)
        for i in range(n*n*n):
            g.add_edge( randint(0,n*n-1), randint(0,n*n-1) )

        p = Paths( graph=g )

        c = p.get_clusters_count()
        self.assertLessEqual( c , n*n  )
        self.assertGreaterEqual( c , 1  )


if __name__=='__main__':
    unittest.main()