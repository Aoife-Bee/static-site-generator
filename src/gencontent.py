import os
import shutil
from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    raise Exception("no title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        contents = f.read()
    with open(template_path, "r") as t:
        template = t.read()
    html_node = markdown_to_html_node(contents)
    html_string = html_node.to_html()
    title = extract_title(contents)
    output = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as d:
        d.write(output)