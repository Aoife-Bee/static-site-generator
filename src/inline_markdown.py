import re
from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode):
            new_node_list.append(old_node)
            continue
        if delimiter not in old_node.text:
            new_node_list.append(old_node)
            continue

        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown syntax, are you missing a delimiter?")
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_node_list.append(TextNode(part, TextType.TEXT))
            else:
                new_node_list.append(TextNode(part, text_type))

    return new_node_list


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_node_list = []
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode):
            new_node_list.append(old_node)
            continue

        if old_node.text_type == TextType.TEXT:
            images = extract_markdown_images(old_node.text)
            if images:
                current_text = old_node.text
                for alt, url in images:
                    markdown = f"![{alt}]({url})"
                    before, after = current_text.split(markdown, 1)
                    if before != "":
                        new_node_list.append(TextNode(before, TextType.TEXT))
                    new_node_list.append(TextNode(alt, TextType.IMAGE, url))
                    current_text = after

                if current_text != "":
                    new_node_list.append(TextNode(current_text, TextType.TEXT))
            else:
                new_node_list.append(old_node)
        else:
            new_node_list.append(old_node)

    return new_node_list

def split_nodes_link(old_nodes):
    new_node_list = []
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode):
            new_node_list.append(old_node)
            continue

        if old_node.text_type == TextType.TEXT:
            links = extract_markdown_links(old_node.text)
            if links:
                current_text = old_node.text
                for alt, url in links:
                    markdown = f"[{alt}]({url})"
                    before, after = current_text.split(markdown, 1)
                    if before != "":
                        new_node_list.append(TextNode(before, TextType.TEXT))
                    new_node_list.append(TextNode(alt, TextType.LINK, url))
                    current_text = after

                if current_text != "":
                    new_node_list.append(TextNode(current_text, TextType.TEXT))
            else:
                new_node_list.append(old_node)
        else:
            new_node_list.append(old_node)

    return new_node_list
