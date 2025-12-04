import os

from block_markdown import markdown_to_html_node
from extract_title import extract_title
from htmlnode import *


def generate_page(src, template, dest):
    print(f"Generating page from {src} to {dest} using {template}")
    with open(src, "r") as f:
        md = f.read()
        title = extract_title(md)
        print("MD length:", len(md))
        node = markdown_to_html_node(md)
        print("NODE:", node)
        content = node.to_html()
        print("CONTENT length:", len(content))
        with open(template, "r") as f1:
            html = f1.read()
            html = html.replace("{{ Title }}", title)
            html = html.replace("{{ Content }}", content)

    if not os.path.exists(os.path.dirname(dest)):
        os.mkdir(os.path.dirname(dest))
    with open(dest, "w") as f:
        f.write(html)
