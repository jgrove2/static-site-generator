import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leaf = LeafNode(tag="a", value="testing", props={"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), "<a href=https://www.google.com>testing</a>")
    def test2_eq(self):
        leaf = LeafNode(value="testing")
        self.assertEqual(leaf.to_html(), "testing")