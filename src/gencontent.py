import os

from block_markdown import markdown_to_html_node
from extract_title import extract_title
from htmlnode import *


def generate_page(src, template, dest):
    print(f"Generating page from {src} to {dest} using {template}")
    with open(src, "r") as f:
        md = f.read()
        title = extract_title(md)
        node = markdown_to_html_node(md)
        content = node.to_html()
        with open(template, "r") as f1:
            html = f1.read()
            html = html.replace("{{ Title }}", title)
            html = html.replace("{{ Content }}", content)

    if not os.path.exists(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))
    with open(dest, "w") as f:
        f.write(html)


def generate_pages_recursive(src_path, template_path, dest_path):
    dir = os.listdir(src_path)
    for item in dir:
        item_path = os.path.join(src_path, item)
        if os.path.isfile(item_path):
            if not item_path.endswith(".md"):
                continue
            file_path = os.path.join(dest_path, item.replace(".md", ".html"))
            generate_page(item_path, template_path, file_path)
        else:
            dir_path = os.path.join(dest_path, item)
            generate_pages_recursive(item_path, template_path, dir_path)
