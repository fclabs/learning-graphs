from Graph.Graph import Graph
import unittest

class TestEmptyGraph(unittest.TestCase):
    
    def test_invalid_init(self):
        with self.assertRaises(ValueError):
            Graph(-1)

    def test_empty_graph_v_cnt(self):
        self.assertEqual( Graph(0).v_cnt , 0 )

    def test_empty_adj(self):
        with self.assertRaises(ValueError):
            Graph(0).adjacents(1)
        
    def test_v_cnt(self):
        self.assertEqual( Graph(5).v_cnt , 5 )
        self.assertEqual( len(Graph(5).vertices) , 5 )

    def test_add_edges_index_error(self):
        g = Graph(3)
        with self.assertRaises(IndexError):
            g.add_edge(0,4)
        with self.assertRaises(IndexError):
            g.add_edge(4,0)
        
    def test_add_edges_consitency(self):
        g = Graph(3)
        g.add_edge(0,1)
        g.add_edge(0,2)
        self.assertEqual( len(list(g.adjacents(0))) , 2 )
        self.assertEqual( len(list(g.adjacents(1))) , 1 )
        self.assertEqual( len(list(g.adjacents(2))) , 1 )

    def test_add_edges_multi_edge(self):
        g = Graph(3)
        g.add_edge(0,1)
        g.add_edge(0,1)
        self.assertEqual( len(list(g.adjacents(0))) , 2 )
        self.assertEqual( len(list(g.adjacents(1))) , 2 )

    def test_add_edges_loop(self):
        g = Graph(1)
        g.add_edge(0,0)
        self.assertEqual( len(list(g.adjacents(0))) , 2 )



if __name__=='__main__':
    unittest.main()