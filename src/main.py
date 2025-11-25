import os
import shutil
import sys
from copystatic import copy_static_to_public
from gencontent import generate_pages_recursive


static_dir = "./static"
content_dir = "./content"
template = "./template.html"
public_dir = "./docs"


def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"Using base path: {base_path}")

    copy_static_to_public(static_dir, public_dir)
    generate_pages_recursive(content_dir, template, public_dir, base_path)

    print("All pages generated successfully!")
    
    
if __name__ == "__main__":
    main()