#!/usr/bin/python3


"""
Markdown to html.

Usage: ./markdown2html.py [input] [output]

Args:
    input (str): Input markdown file.
    output (str): Output html file.
"""


import sys
import markdown  # type: ignore
from pathlib import Path


def markdown2html(md):
    """Convert markdown to html.

    Args:
        md (str): Markdown string.

    Returns:
        str: HTML string."""
    return markdown.markdown(md)


def main():
    """Main function.

    This function is the entry point of the program. It takes two command line arguments: the path to the Markdown file and the path to the HTML file. It reads the content of the Markdown file, converts it to HTML using the `markdown2html` function, and writes the HTML content to the specified HTML file.

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

    html = markdown2html(md)

    with open(html_file, 'w') as f:
        f.write(html)

    sys.exit(0)


if __name__ == "__main__":
    """This is the main entry point of the program."""
    main()
