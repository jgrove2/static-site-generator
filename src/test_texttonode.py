import unittest

from util import text_to_nodes
from textnode import TextNode
from util import TextNodeTypes


class TestLeafNode(unittest.TestCase):
    def test_text_eq(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected = [
    TextNode("This is ", TextNodeTypes.text_type_text),
    TextNode("text", TextNodeTypes.text_type_bold),
    TextNode(" with an ", TextNodeTypes.text_type_text),
    TextNode("italic", TextNodeTypes.text_type_italic),
    TextNode(" word and a ", TextNodeTypes.text_type_text),
    TextNode("code block", TextNodeTypes.text_type_code),
    TextNode(" and an ", TextNodeTypes.text_type_text),
    TextNode("image", TextNodeTypes.text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and a ", TextNodeTypes.text_type_text),
    TextNode("link", TextNodeTypes.text_type_link, "https://boot.dev"),
]
        nodes = text_to_nodes(text)

        self.assertListEqual(nodes, expected)