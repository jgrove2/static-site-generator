import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_neq_f(self):
        node = TextNode("This is a text node", "bold", "http")
        node2 = TextNode("This is a text node1", "bold", "http")
        self.assertNotEqual(node, node2)
    def test_neq_m(self):
        node = TextNode("This is a text node", "bold", "http")
        node2 = TextNode("This is a text node", "bold1", "http")
        self.assertNotEqual(node, node2)
    def test_neq_e(self):
        node = TextNode("This is a text node", "bold", "http")
        node2 = TextNode("This is a text node", "bold", "http1")
        self.assertNotEqual(node, node2)
    def test_neq_nonef(self):
        node = TextNode(None, "bold", "http")
        node2 = TextNode("This is a text node", "bold", "http")
        self.assertNotEqual(node, node2)
    def test_neq_nonef(self):
        node = TextNode("This is a text node", None, "http")
        node2 = TextNode("This is a text node", "bold", "http")
        self.assertNotEqual(node, node2)
    def test_neq_nonef(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", "http")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()