from util import block_to_block_type, markdown_to_blocks, TextNodeTypes, text_to_nodes, text_node_to_html_node
from textnode import TextNode
from htmlnode import ParentNode, LeafNode
import re

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    top_level_textNodes = []
    for block in blocks:
        nodeType = block_to_block_type(block)
        top_level_textNodes.append(TextNode(block, nodeType))

    html_nodes = []
    for node in top_level_textNodes:
        if node.text_type == "quote":
            html_nodes.append(create_blockquote(node))
        if node.text_type == "paragraph":
            html_nodes.append(create_paragraph(node))
        if node.text_type == "code":
            html_nodes.append(create_code(node))
        if node.text_type == "heading":
            html_nodes.append(create_header(node))
        if node.text_type == "ordered_list":
            html_nodes.append(create_ordered_list(node))
        if node.text_type == "unordered_list":
            html_nodes.append(create_unordered_list(node))
        
    return ParentNode("div", html_nodes).to_html()

def create_paragraph(node):
    text_nodes = text_to_nodes(node.text)
    html_nodes = []
    for txt in text_nodes:
        html_nodes.append(text_node_to_html_node(txt))
    return ParentNode("p", html_nodes)

def create_code(node):
    txt = node.text.strip("```").lstrip("```")
    text_nodes = text_to_nodes(txt)
    html_nodes = []
    for txt in text_nodes:
        html_nodes.append(text_node_to_html_node(txt))
    return ParentNode("pre", [ParentNode("code", html_nodes)])

def create_blockquote(node):
    split_blocks = node.text.split("\n")
    child_nodes = []
    for block in split_blocks:
        child_nodes.append(text_to_nodes(block.lstrip("> ")))
    html_nodes = []
    for txt_nodes in child_nodes:
        leaf_nodes = []
        for lf in txt_nodes:
            leaf_nodes.append(text_node_to_html_node(lf))
        html_nodes.append(ParentNode("p", leaf_nodes))
    return ParentNode("blockquote", html_nodes)

def create_header(node):
    txt = node.text.lstrip("# ")
    level = len(node.text) - len(txt) - 1
    text_nodes = text_to_nodes(txt)
    html_nodes = []
    for txt in text_nodes:
        html_nodes.append(text_node_to_html_node(txt))
    return ParentNode(f"h{str(level)}", html_nodes)

def create_ordered_list(node):
    split_blocks = node.text.split("\n")
    child_nodes = []
    for block in split_blocks:
        child_nodes.append(text_to_nodes(re.sub(r'^\d+\.\s*', '', block)))
    html_nodes = []
    for txt_nodes in child_nodes:
        leaf_nodes = []
        for lf in txt_nodes:
            leaf_nodes.append(text_node_to_html_node(lf))
        html_nodes.append(ParentNode("li", leaf_nodes))
    return ParentNode("ol", html_nodes)

def create_unordered_list(node):
    split_blocks = node.text.split("\n")
    child_nodes = []
    for block in split_blocks:
        child_nodes.append(text_to_nodes(re.sub(r'^\*\s*', '', block)))
    html_nodes = []
    for txt_nodes in child_nodes:
        leaf_nodes = []
        for lf in txt_nodes:
            leaf_nodes.append(text_node_to_html_node(lf))
        html_nodes.append(ParentNode("li", leaf_nodes))
    return ParentNode("ul", html_nodes)


