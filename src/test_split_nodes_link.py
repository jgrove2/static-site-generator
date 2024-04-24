import unittest

from util import split_nodes_image
from textnode import TextNode
from util import TextNodeTypes


class TestLeafNode(unittest.TestCase):
    def test_text_eq(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextNodeTypes.text_type_text,
        )
        new_nodes = split_nodes_image([node])
        expected = [
                TextNode("This is text with an ", TextNodeTypes.text_type_text),
                TextNode("image", TextNodeTypes.text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", TextNodeTypes.text_type_text),
                TextNode(
                    "second image", TextNodeTypes.text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                ),
            ]
        self.assertListEqual(new_nodes, expected)