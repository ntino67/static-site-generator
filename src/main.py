from textnode import TextNode, TextType


def main():
    print("Hello")
    object = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(object)


if __name__ == "__main__":
    main()
