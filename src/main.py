import os
import shutil
import sys

from copytree import copytree
from gencontent import generate_pages_recursive

src = "content"
template = "template.html"
dest = "docs"


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[0]
    else:
        basepath = "/"
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    copytree("static", dest)
    generate_pages_recursive(src, template, dest, basepath)


if __name__ == "__main__":
    main()
