import unittest
from logging import warn

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_no_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "x")]).to_html()

    def test_parent_children_none_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_parent_empty_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_parent_with_multiple_children(self):
        n = ParentNode(
            "p", [LeafNode(None, "a"), LeafNode("b", "b"), LeafNode(None, "c")]
        )
        self.assertEqual(n.to_html(), "<p>a<b>b</b>c</p>")

    def test_parent_with_props_and_children(self):
        n = ParentNode("div", [LeafNode("i", "x")], {"class": "c", "id": "i"})
        html = n.to_html()
        self.assertIn("<div", html)
        self.assertIn('class="c"', html)
        self.assertIn('id="i"', html)
        self.assertTrue(html.endswith("</div>"))

    def test_nested_three_levels(self):
        g = LeafNode("b", "g")
        c = ParentNode("span", [g])
        p = ParentNode("div", [LeafNode(None, "x"), c, LeafNode(None, "y")])
        self.assertEqual(p.to_html(), "<div>x<span><b>g</b></span>y</div>")

    def test_props_order_insensitive(self):
        n1 = HTMLNode("a", "t", None, {"href": "u", "target": "_blank"})
        n2 = HTMLNode("a", "t", None, {"target": "_blank", "href": "u"})
        self.assertEqual(n1, n2)

    def test_htmlnode_neq_tag(self):
        self.assertNotEqual(HTMLNode("a", "t"), HTMLNode("p", "t"))

    def test_htmlnode_neq_value(self):
        self.assertNotEqual(HTMLNode("a", "t1"), HTMLNode("a", "t2"))

    def test_child_must_have_to_html(self):
        class NotNode:
            pass

        with self.assertRaises(AttributeError):
            ParentNode("div", [NotNode()]).to_html()
