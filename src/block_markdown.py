from enum import Enum

from htmlnode import ParentNode
from inline_markdown import TextNode, text_node_to_html_node, text_to_textnodes
from textnode import TextType


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered list"
    OL = "ordered list"


def markdown_to_blocks(md):
    blocks = []
    parts = md.split("\n\n")
    for part in parts:
        if part == "":
            continue
        stripped = part.strip()
        blocks.append(stripped)
    return blocks


def block_to_block_type(md):
    if md.startswith("```") and md.endswith("```"):
        return BlockType.CODE
    elif md.startswith("#"):
        count = 0
        for ch in md:
            if ch == "#" and count < 6:
                count += 1
            elif ch == " " and 1 <= count <= 6:
                return BlockType.HEADING
            else:
                return BlockType.PARAGRAPH
    elif all(line.startswith(">") for line in md.splitlines()):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in md.splitlines()):
        return BlockType.UL
    elif md.startswith("1. "):
        lines = md.splitlines()
        count = 0
        for line in lines:
            count += 1
            if not line.startswith(f"{count}. "):
                return BlockType.PARAGRAPH
        return BlockType.OL
    else:
        return BlockType.PARAGRAPH


def markdown_to_html_node(md):
    children = []
    blocks = markdown_to_blocks(md)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                children.append(parse_paragraph(block))
            case BlockType.HEADING:
                children.append(parse_heading(block))
            case BlockType.QUOTE:
                children.append(parse_quote(block))
            case BlockType.CODE:
                children.append(parse_code(block))
            case BlockType.UL:
                children.append(parse_ul(block))
            case BlockType.OL:
                children.append(parse_ol(block))
            case _:
                pass
    wrapper = ParentNode("div", children)
    return wrapper


def parse_paragraph(md):
    child = []
    nodes = text_to_textnodes(md)
    for node in nodes:
        child.append(text_node_to_html_node(node))
    return ParentNode("p", children=child)


def parse_heading(md):
    level = 0
    child = []
    while md[level] == "#":
        level += 1
    text = md[level + 1 :]
    nodes = text_to_textnodes(text)
    for node in nodes:
        child.append(text_node_to_html_node(node))
    return ParentNode(f"h{level}", children=child)


def parse_quote(md):
    stripped = []
    child = []
    lines = md.split("\n")
    for line in lines:
        item_text = line[2:]
        stripped.append(item_text)
    text = "\n".join(stripped)
    nodes = text_to_textnodes(text)
    for node in nodes:
        child.append(text_node_to_html_node(node))
    return ParentNode("blockquote", children=child)


def parse_code(md):
    lines = md.split("\n")
    inside_lines = lines[1:-1]
    inside_text = "\n".join(inside_lines)
    node = TextNode(inside_text, TextType.TEXT)
    code_node = text_node_to_html_node(node)
    return ParentNode("pre", children=[code_node])


def parse_ul(md):
    li_nodes = []
    lines = md.split("\n")
    for line in lines:
        item_text = line[2:]
        text_nodes = text_to_textnodes(item_text)
        html_children = []
        for tnode in text_nodes:
            html_children.append(text_node_to_html_node(tnode))
        li_nodes.append(ParentNode("li", children=html_children))
    return ParentNode("ul", children=li_nodes)


def parse_ol(md):
    li_nodes = []
    lines = md.split("\n")
    for line in lines:
        dot_index = line.find(". ")
        item_text = line[dot_index + 2 :]
        text_nodes = text_to_textnodes(item_text)
        html_children = []
        for tnode in text_nodes:
            html_children.append(text_node_to_html_node(tnode))
        li_nodes.append(ParentNode("li", children=html_children))
    return ParentNode("ol", children=li_nodes)
