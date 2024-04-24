import unittest

from util import text_node_to_html_node, TextNodeTypes
from textnode import TextNode

class TestLeafNode(unittest.TestCase):
    def test_text_eq(self):
        node = TextNode("This is a text node", TextNodeTypes.text_type_text)
        self.assertEqual(text_node_to_html_node(node).to_html(), "This is a text node")
    def test_bold_eq(self):
        node = TextNode("This is a text node", TextNodeTypes.text_type_bold)
        self.assertEqual(text_node_to_html_node(node).to_html(), "<b>This is a text node</b>")
    def test_italic_eq(self):
        node = TextNode("This is a text node", TextNodeTypes.text_type_italic)
        self.assertEqual(text_node_to_html_node(node).to_html(), "<i>This is a text node</i>")
    def test_code_eq(self):
        node = TextNode("This is a text node", TextNodeTypes.text_type_code)
        self.assertEqual(text_node_to_html_node(node).to_html(), "<code>This is a text node</code>")
    def test_link_eq(self):
        node = TextNode("This is a text node", TextNodeTypes.text_type_link, "www.wiki.com")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<a href=www.wiki.com>This is a text node</a>")
    def test_image_eq(self):
        node = TextNode("This is a text node", TextNodeTypes.text_type_image, "www.wiki.com")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<img src=www.wiki.com alt=This is a text node></img>")
