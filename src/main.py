import os
import shutil
from copystatic import copy_static_to_public
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
content_dir = "./content"
template = "./template.html"
public_dir = "./public"


def main():
    copy_static_to_public(dir_path_static, dir_path_public)
    generate_pages_recursive(content_dir, template, public_dir)
    print("All pages generated successfully!")
    
    
main()