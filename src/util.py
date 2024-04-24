from enum import Enum
from textnode import TextNode
from htmlnode import LeafNode
import re

class TextNodeTypes(Enum):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

class HTMLNodeTypes(Enum):
    text_type_text = None
    text_type_bold = "b"
    text_type_italic = "i"
    text_type_code = "code"
    text_type_link = "a"
    text_type_image = "img"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextNodeTypes.text_type_text:
        return LeafNode(tag=HTMLNodeTypes.text_type_text.value, value=text_node.text)
    elif text_node.text_type == TextNodeTypes.text_type_bold:
        return LeafNode(tag=HTMLNodeTypes.text_type_bold.value, value=text_node.text)
    elif text_node.text_type == TextNodeTypes.text_type_italic:
        return LeafNode(tag=HTMLNodeTypes.text_type_italic.value, value=text_node.text)
    elif text_node.text_type == TextNodeTypes.text_type_code:
        return LeafNode(tag=HTMLNodeTypes.text_type_code.value, value=text_node.text)
    elif text_node.text_type == TextNodeTypes.text_type_link:
        return LeafNode(tag=HTMLNodeTypes.text_type_link.value, value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextNodeTypes.text_type_image:
        return LeafNode(tag=HTMLNodeTypes.text_type_image.value, value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise TypeError
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    old_text = old_nodes.text
    split_text = old_text.split(delimiter)
    nt = [
        TextNode(split_text[0], old_nodes.text_type, old_nodes.url),
        TextNode(split_text[1], text_type), 
        TextNode(split_text[2], old_nodes.text_type, old_nodes.url)
    ]
    return nt

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
def extract_markdown_links(text):
    return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(node_list):
    ret_nodes = []
    for node in node_list:
        if node.text_type == TextNodeTypes.text_type_image:
            ret_nodes.append(node)
        else:
            image_tags = extract_markdown_images(node.text)
            ret_nodes += create_img_node_list([node], image_tags, "!", TextNodeTypes.text_type_image)
    return ret_nodes

def split_nodes_link(node_list):
    ret_nodes = []
    for node in node_list:
        if node.text_type == TextNodeTypes.text_type_image:
            ret_nodes.append(node)
        else:
            image_tags = extract_markdown_links(node.text)
            ret_nodes += create_img_node_list([node], image_tags, "", TextNodeTypes.text_type_link)
    return ret_nodes               

def create_img_node_list(node_list, image_tag, startchar, node_type):
    nodes = []
    if len(image_tag) == 0:
        return node_list
    for i_node in node_list:
        if i_node.text_type == TextNodeTypes.text_type_image or i_node.text_type == TextNodeTypes.text_type_link:
            nodes.append(i_node)
            continue
        img_md = f"{startchar}[{image_tag[0][0]}]({image_tag[0][1]})"
        if img_md in i_node.text:
            img_loc = i_node.text.index(img_md)
        else:
            nodes.append(i_node)
            continue
        if img_loc != 0:
            nodes.append(TextNode(i_node.text[:img_loc], TextNodeTypes.text_type_text))
        nodes.append(TextNode(image_tag[0][0], node_type, image_tag[0][1]))
        if img_loc + len(img_md) != len(i_node.text):
            nodes.append(TextNode(i_node.text[img_loc + len(img_md):], TextNodeTypes.text_type_text))
    return create_img_node_list(nodes, image_tag[1:], startchar, node_type)

def selectDelimeters(delimeter, types, nodes):
    returnedNodes = []
    if len(delimeter) == 0:
        return nodes
    for i in nodes:
        if delimeter[0] in i.text:
            returnedNodes += split_nodes_delimiter(i, delimeter[0], types[0])
        else:
            returnedNodes.append(i)
    return selectDelimeters(delimeter[1:], types[1:], returnedNodes)

def text_to_nodes(text):
    delimeters = ["**", "*", "`"]
    types = [TextNodeTypes.text_type_bold, TextNodeTypes.text_type_italic, TextNodeTypes.text_type_code]
    start = TextNode(text, TextNodeTypes.text_type_text)
    nodes = selectDelimeters(delimeters, types, [start])
    img_split = split_nodes_image(nodes)
    link_split = split_nodes_link(img_split)
    return link_split

def markdown_to_blocks(markdown):
    split_blocks = markdown.split('\n\n')
    striped_blocks = []
    for block in split_blocks:
        if block == "":
            continue
        block = block.strip()
        block = block.lstrip()
        striped_blocks.append(block)
    return striped_blocks

def block_to_block_type(block):
    if re.match('^#{1,6} ', block):
        return "heading"
    if re.match("^```[\s\S]*```$", block):
        return "code"
    if re.match("^>", block):
        return "quote"
    if re.match("^\*\s.*", block):
        return "unordered_list"
    if re.match("^\d+\.\s.*", block):
        return "ordered_list"
    return "paragraph"

def extract_title(text):
    return re.findall(r'# (.*)\s*', text)[0]