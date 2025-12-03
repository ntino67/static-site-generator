import unittest

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import LeafNode, ParentNode
from main import (
    markdown_to_html_node,
    parse_code,
    parse_heading,
    parse_paragraph,
    parse_quote,
)


class TestMarkdownToBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UL)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OL)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


class TestMarkdownToHtmlNode(unittest.TestCase):
    # --- parse_paragraph -------------------------------------------------

    def test_parse_paragraph_plain_text(self):
        md = "This is a plain paragraph."
        node = parse_paragraph(md)

        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, "p")
        self.assertEqual(len(node.children), 1)
        text_child = node.children[0]
        self.assertIsInstance(text_child, LeafNode)
        self.assertEqual(text_child.value, "This is a plain paragraph.")

    def test_parse_paragraph_with_bold_and_italic(self):
        md = "This is **bold** and _italic_."
        node = parse_paragraph(md)

        self.assertEqual(node.tag, "p")
        # shape: "This is ", <b>bold</b>, " and ", <i>italic</i>, "."
        values = [child.value for child in node.children]
        tags = [child.tag for child in node.children]

        self.assertIn("This is ", values[0])
        self.assertIn(" and ", values[2])
        self.assertEqual(tags[1], "b")
        self.assertEqual(values[1], "bold")
        self.assertEqual(tags[3], "i")
        self.assertEqual(values[3], "italic")

    # --- parse_heading ---------------------------------------------------

    def test_parse_heading_level_one(self):
        md = "# Heading 1"
        node = parse_heading(md)

        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, "h1")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].value, "Heading 1")

    def test_parse_heading_level_three(self):
        md = "### Deep heading"
        node = parse_heading(md)

        self.assertEqual(node.tag, "h3")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].value, "Deep heading")

    # --- parse_quote -----------------------------------------------------

    def test_parse_quote_single_line(self):
        md = "> This is a quote"
        node = parse_quote(md)

        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, "blockquote")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].value, "This is a quote")

    def test_parse_quote_multi_line(self):
        md = "> Line one\n> Line two"
        node = parse_quote(md)

        self.assertEqual(node.tag, "blockquote")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].value, "Line one\nLine two")

    # --- parse_code ------------------------------------------------------

    def test_parse_code_single_line(self):
        md = "```\nprint('hi')\n```"
        node = parse_code(md)

        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, "pre")
        self.assertEqual(len(node.children), 1)
        code_leaf = node.children[0]
        self.assertIsInstance(code_leaf, LeafNode)
        self.assertEqual(code_leaf.value, "print('hi')")

    def test_parse_code_multi_line(self):
        md = "```\nline 1\nline 2\n```"
        node = parse_code(md)

        self.assertEqual(node.tag, "pre")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].value, "line 1\nline 2")

    # --- markdown_to_html_node -------------------------------------------

    def test_markdown_to_html_node_paragraph(self):
        md = "This is **bold** text."
        root = markdown_to_html_node(md)

        self.assertIsInstance(root, ParentNode)
        self.assertEqual(root.tag, "div")
        self.assertEqual(len(root.children), 1)

        p = root.children[0]
        self.assertIsInstance(p, ParentNode)
        self.assertEqual(p.tag, "p")

        # sanity: make sure bold node is present
        bold_nodes = [c for c in p.children if isinstance(c, LeafNode) and c.tag == "b"]
        self.assertEqual(len(bold_nodes), 1)
        self.assertEqual(bold_nodes[0].value, "bold")

    def test_markdown_to_html_node_heading_block(self):
        md = "# Title"
        root = markdown_to_html_node(md)

        self.assertEqual(root.tag, "div")
        self.assertEqual(len(root.children), 1)
        h1 = root.children[0]
        self.assertEqual(h1.tag, "h1")
        self.assertEqual(h1.children[0].value, "Title")

    def test_markdown_to_html_node_quote_block(self):
        md = "> quoted text"
        root = markdown_to_html_node(md)

        self.assertEqual(root.tag, "div")
        self.assertEqual(len(root.children), 1)
        blockquote = root.children[0]
        self.assertEqual(blockquote.tag, "blockquote")
        self.assertEqual(blockquote.children[0].value, "quoted text")

    def test_markdown_to_html_node_code_block(self):
        md = "```\ncode line\n```"
        root = markdown_to_html_node(md)

        self.assertEqual(root.tag, "div")
        self.assertEqual(len(root.children), 1)
        pre = root.children[0]
        self.assertEqual(pre.tag, "pre")
        self.assertEqual(pre.children[0].value, "code line")
