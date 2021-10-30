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
        




if __name__=='__main__':
    unittest.main()