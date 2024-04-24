import unittest

from htmlnode import ParentNode
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    def test_eq(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            node.to_html()