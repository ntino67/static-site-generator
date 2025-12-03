import os
import shutil


def copytree(src, dest):
    for item in os.listdir(src):
        path = os.path.join(src, item)
        if os.path.isfile(path):
            shutil.copy(path, dest)
        else:
            os.mkdir(os.path.join(dest, item))
            copytree(path, os.path.join(dest, item))
