import os
import shutil

from copytree import copytree
from gencontent import generate_page

src = "content/index.md"
template = "template.html"
dest = "public/index.html"


def main():
    shutil.rmtree("public")
    os.mkdir("public")
    copytree("static", "public")
    generate_page(src, template, dest)


if __name__ == "__main__":
    main()
