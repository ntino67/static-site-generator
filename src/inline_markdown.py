import re

from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) < 3 or len(parts) % 2 == 0:
            new_nodes.append(node)
            continue

        for i, part in enumerate(parts):
            if part == "":
                pass
            tt = text_type if i % 2 != 0 else TextType.TEXT
            new_nodes.append(TextNode(part, tt))
    return new_nodes


def _split_nodes_by_extractions(old_nodes, extractor, builder, formatter):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        pairs = extractor(node.text)
        if not pairs:
            new_nodes.append(node)
            continue

        curr = node.text
        for a, b in pairs:
            before, sep, after = curr.partition(formatter(a, b))
            if sep == "":
                break
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(builder(a, b))
            curr = after
        if curr:
            new_nodes.append(TextNode(curr, TextType.TEXT))
    return new_nodes


def split_nodes_image(old_nodes):
    return _split_nodes_by_extractions(
        old_nodes,
        extractor=extract_markdown_images,
        builder=lambda alt, url: TextNode(alt, TextType.IMAGE, url),
        formatter=lambda alt, url: f"![{alt}]({url})",
    )


def split_nodes_link(old_nodes):
    return _split_nodes_by_extractions(
        old_nodes,
        extractor=extract_markdown_links,
        builder=lambda text, url: TextNode(text, TextType.LINK, url),
        formatter=lambda text, url: f"[{text}]({url})",
    )


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes
