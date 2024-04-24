import unittest

from util import split_nodes_delimiter
from textnode import TextNode


class TestLeafNode(unittest.TestCase):
    def test_text_eq(self):
        node = TextNode("This is text with a `code block` word", "text")
        self.assertListEqual(
            split_nodes_delimiter(node, "`", "code"),
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ],
        )
