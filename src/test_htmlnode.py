import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "it's a link", None, {"href": "http://BMC.com/"})
        node2 = HTMLNode("a", "it's a link", None, {"href": "http://BMC.com/"})
        self.assertEqual(node, node2)

    def test_neq_props(self):
        node = HTMLNode("a", "it's a link", None, {"href": "http://BM.com/"})
        node2 = HTMLNode("a", "it's a link", None, {"href": "http://BMC.com/"})
        self.assertNotEqual(node, node2)

    def test_eq_children(self):
        children = HTMLNode("a", "it's a link", None, {"href": "http://BM.com/"})
        node = HTMLNode("a", "it's a link", children, {"href": "http://BMC.com/"})
        node2 = HTMLNode("a", "it's a link", children, {"href": "http://BMC.com/"})
        self.assertEqual(node, node2)

    def test_neq_children(self):
        children = HTMLNode("a", "it's a link", None, {"href": "http://BM.com/"})
        children2 = HTMLNode("a", "it's not a link", None, {"href": "http://BM.com/"})
        node = HTMLNode("a", "it's a link", children, {"href": "http://BMC.com/"})
        node2 = HTMLNode("a", "it's a link", children2, {"href": "http://BMC.com/"})
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )
