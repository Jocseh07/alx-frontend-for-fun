#!/usr/bin/python3


import sys
import os


"""
Converts a Markdown file to HTML.

Usage: ./markdown2html.py <markdown_file> <output_file>

Arguments:
    markdown_file: the Markdown file to convert
    output_file: the HTML output file
"""


def markdown2html(markdown_file, output_file):
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>",
              file=sys.stderr)
        sys.exit(1)

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML and write to the output file
    with open(markdown_file, 'r') as f:
        markdown = f.read()
        html = markdown.replace('\n', '<br />\n')
        with open(output_file, 'w') as f:
            f.write(html)

    sys.exit(0)


if __name__ == "__main__":
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    markdown2html(markdown_file, output_file)
