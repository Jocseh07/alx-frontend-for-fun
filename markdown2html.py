#!/usr/bin/python3

"""Markdown to HTML

    Parameters:
    None

    Returns:
    None
"""


import sys
import markdown
from pathlib import Path


def markdown2html():
    """This function converts a markdown file to an HTML file.

    Parameters:
    - None

    Returns:
    - None
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not Path(md_file).is_file():
        print("Missing {}".format(md_file), file=sys.stderr)
        sys.exit(1)

    with open(md_file, 'r') as f:
        md = f.read()

    html = markdown.markdown(md)

    with open(html_file, 'w') as f:
        f.write(html)

    sys.exit(0)


if __name__ == "__main__":
    """This is the main entry point of the program."""
    markdown2html()
