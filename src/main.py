from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    object = HTMLNode("a", "This is a link", None, {"href": "http://BMC.com/"})
    print(object)


if __name__ == "__main__":
    main()
