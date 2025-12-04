import os
import shutil

from copytree import copytree
from gencontent import generate_pages_recursive

src = "content"
template = "template.html"
dest = "public"


def main():
    shutil.rmtree("public")
    os.mkdir("public")
    copytree("static", "public")
    generate_pages_recursive(src, template, dest)


if __name__ == "__main__":
    main()
