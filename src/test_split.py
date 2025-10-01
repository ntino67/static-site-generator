import unittest

from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
)
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_pass_through_non_text(self):
        nodes = [TextNode("bold", TextType.BOLD)]
        out = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(out, nodes)

    def test_no_delimiters_present(self):
        nodes = [TextNode("just text", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0].text, "just text")
        self.assertEqual(out[0].text_type, TextType.TEXT)

    def test_single_pair_start(self):
        nodes = [TextNode("`code` tail", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual([n.text for n in out], ["", "code", " tail"])
        self.assertEqual(
            [n.text_type for n in out], [TextType.TEXT, TextType.CODE, TextType.TEXT]
        )

    def test_single_pair_end(self):
        nodes = [TextNode("head `code`", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual([n.text for n in out], ["head ", "code", ""])
        self.assertEqual(
            [n.text_type for n in out], [TextType.TEXT, TextType.CODE, TextType.TEXT]
        )

    def test_multiple_pairs(self):
        nodes = [TextNode("a `x` b `y` c", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual([n.text for n in out], ["a ", "x", " b ", "y", " c"])
        self.assertEqual(
            [n.text_type for n in out],
            [TextType.TEXT, TextType.CODE, TextType.TEXT, TextType.CODE, TextType.TEXT],
        )

    def test_adjacent_pairs(self):
        nodes = [TextNode("`` ``", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual([n.text for n in out], ["", "", " ", "", ""])
        self.assertEqual(
            [n.text_type for n in out],
            [TextType.TEXT, TextType.CODE, TextType.TEXT, TextType.CODE, TextType.TEXT],
        )

    def test_entire_string_wrapped(self):
        nodes = [TextNode("`x`", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual([n.text for n in out], ["", "x", ""])
        self.assertEqual(
            [n.text_type for n in out], [TextType.TEXT, TextType.CODE, TextType.TEXT]
        )

    def test_unbalanced_raises(self):
        nodes = [TextNode("bad `code", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "`", TextType.CODE)

    def test_italic_underscore(self):
        nodes = [TextNode("pre _it_ post", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual([n.text for n in out], ["pre ", "it", " post"])
        self.assertEqual(
            [n.text_type for n in out], [TextType.TEXT, TextType.ITALIC, TextType.TEXT]
        )

    def test_bold_double_asterisk(self):
        nodes = [TextNode("pre **b** post", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual([n.text for n in out], ["pre ", "b", " post"])
        self.assertEqual(
            [n.text_type for n in out], [TextType.TEXT, TextType.BOLD, TextType.TEXT]
        )

    def test_mixed_list_only_split_text(self):
        nodes = [
            TextNode("pre ", TextType.TEXT),
            TextNode("already bold", TextType.BOLD),
            TextNode(" mid `x` post", TextType.TEXT),
        ]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        texts = [n.text for n in out]
        types = [n.text_type for n in out]
        self.assertEqual(texts, ["pre ", "already bold", " mid ", "x", " post"])
        self.assertEqual(
            types,
            [TextType.TEXT, TextType.BOLD, TextType.TEXT, TextType.CODE, TextType.TEXT],
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "![a](url1) text ![b](url2) and ![c d](url3.png)"
        self.assertListEqual(
            [("a", "url1"), ("b", "url2"), ("c d", "url3.png")],
            extract_markdown_images(text),
        )

    def test_extract_markdown_images_empty_alt(self):
        text = "![](https://img.com/x.png)"
        self.assertListEqual(
            [("", "https://img.com/x.png")],
            extract_markdown_images(text),
        )

    def test_extract_markdown_images_empty_url(self):
        text = "![alt]()"
        self.assertListEqual(
            [("alt", "")],
            extract_markdown_images(text),
        )

    def test_extract_markdown_images_ignores_links(self):
        text = "[not image](https://x.com) and ![img](https://y.com)"
        self.assertListEqual(
            [("img", "https://y.com")],
            extract_markdown_images(text),
        )

    def test_extract_markdown_links_multiple(self):
        text = "[one](u1) some [two words](u2.png) and [three](http://u3)"
        self.assertListEqual(
            [("one", "u1"), ("two words", "u2.png"), ("three", "http://u3")],
            extract_markdown_links(text),
        )

    def test_extract_markdown_links_empty_text(self):
        text = "[](https://example.com)"
        self.assertListEqual(
            [("", "https://example.com")],
            extract_markdown_links(text),
        )

    def test_extract_markdown_links_empty_url(self):
        text = "[anchor]()"
        self.assertListEqual(
            [("anchor", "")],
            extract_markdown_links(text),
        )

    def test_links_do_not_match_images(self):
        text = "![pic](x) and [link](y)"
        self.assertListEqual([("link", "y")], extract_markdown_links(text))

    def test_no_matches(self):
        text = "plain text with (parentheses) and [brackets] but no pairs"
        self.assertListEqual([], extract_markdown_images(text))
        self.assertListEqual([], extract_markdown_links(text))


if __name__ == "__main__":
    unittest.main()
