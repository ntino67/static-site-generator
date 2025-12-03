import os
import shutil


def copytree(src, dest):
    print(f"Copy {src} directory into {dest}")
    for item in os.listdir(src):
        path = os.path.join(src, item)
        if os.path.isfile(path):
            shutil.copy(path, dest)
            print(f"Copying {path} into {dest}")
        else:
            os.mkdir(os.path.join(dest, item))
            print(f"Creating {os.path.join(dest, item)}")
            copytree(path, os.path.join(dest, item))
