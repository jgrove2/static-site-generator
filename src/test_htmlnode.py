import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="a", value="Test", children=[], props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), " href=https://google.com")

if __name__ == "__main__":
    unittest.main()