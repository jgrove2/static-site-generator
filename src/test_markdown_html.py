import unittest

from markdown_to_html import markdown_to_html

class TestLeafNode(unittest.TestCase):
    def test_markdown_to_html(self):
        text = "1. test\n2. test **test**\n\n* tes\n* ches\n\n### test\n\n```\ndef test():\n\tprint(\"hello world!\")\n```\n\n> test\n> testing *testing* test\n> testing\n\nThis is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items\n"
        print(markdown_to_html(text))