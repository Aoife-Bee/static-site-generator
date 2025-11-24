import re
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        child = block_to_html_node(block, block_type)
        children.append(child)

    return ParentNode("div", children)

def block_to_html_node(block, block_type):
    func = block_type_to_func.get(block_type)
    if func:
        return func(block)
    raise ValueError(f"Unsupported block type: {block_type}")


def heading_to_html_node(block):
    match = re.match(r"^(#{1,6})\s+(.*)$", block)
    if match:
        level = len(match.group(1))
        text = match.group(2).strip()
        text_nodes = text_to_textnodes(text)
        children = [text_node_to_html_node(tn) for tn in text_nodes]
        return ParentNode(f"h{level}", children)
        

def code_to_html_node(block):
    lines = block.split("\n")
    text = "\n".join(lines[1:-1]) + "\n"
    text_node = TextNode(text, TextType.TEXT)
    child_node = text_node_to_html_node(text_node)
    code_node = ParentNode("code", [child_node])
    return ParentNode("pre", [code_node])

def quote_to_html_node(block):
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        cleaned.append(line[1:].lstrip())
    text = " ".join(cleaned)
    text_nodes = text_to_textnodes(text)
    children = [text_node_to_html_node(tn) for tn in text_nodes]
    return ParentNode("blockquote", children)
    

def ulist_to_html_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        text = line[2:].strip()
        text_nodes = text_to_textnodes(text)
        children = [text_node_to_html_node(tn) for tn in text_nodes]
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)

def olist_to_html_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        text = re.sub(r"^\d+\.\s+", "", line).strip()
        text_nodes = text_to_textnodes(text)
        children = [text_node_to_html_node(tn) for tn in text_nodes]
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    text_nodes = text_to_textnodes(paragraph)
    children = [text_node_to_html_node(tn) for tn in text_nodes]
    return ParentNode("p", children)

block_type_to_func = {
    BlockType.HEADING: heading_to_html_node,
    BlockType.CODE: code_to_html_node,
    BlockType.QUOTE: quote_to_html_node,
    BlockType.ULIST: ulist_to_html_node,
    BlockType.OLIST: olist_to_html_node,
    BlockType.PARAGRAPH: paragraph_to_html_node
}