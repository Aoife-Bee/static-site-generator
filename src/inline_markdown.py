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