import os
import shutil


def copy_static_to_public(source, destination):
    clear_dir(destination)
    copy_dir_to_destination(source, destination)

def clear_dir(path):
    if not os.path.exists(path):
        return
    for name in os.listdir(path):
        full = os.path.join(path, name)
        if os.path.isdir(full) and not os.path.islink(full):
            shutil.rmtree(full)
        else:
            os.remove(full)

def copy_dir_to_destination(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(source)
    os.makedirs(destination, exist_ok=True)

    for name in os.listdir(source):
        source_path = os.path.join(source, name)
        destination_path = os.path.join(destination, name)

        if os.path.isdir(source_path) and not os.path.islink(source_path):
            os.makedirs(destination_path, exist_ok=True)
            copy_dir_to_destination(source_path, destination_path)
        else:
            shutil.copy2(source_path, destination_path)
