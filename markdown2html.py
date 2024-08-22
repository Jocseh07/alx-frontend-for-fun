#!/usr/bin/python3


"""
This is a script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""


import sys
import markdown
from pathlib import Path


if __name__ == "__main__":
    """This is the main entry point of the program."""
    # Check if the number of command line arguments is less than 3
    if len(sys.argv) < 3:
        # Print the correct usage of the script to stderr
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        # Exit the program with a non-zero status code
        sys.exit(1)

    # Get the name of the Markdown file from the command line arguments
    md_file = sys.argv[1]
    # Get the name of the output HTML file from the command line arguments
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not Path(md_file).is_file():
        # Print an error message indicating the missing file to stderr
        print("Missing {}".format(md_file), file=sys.stderr)
        # Exit the program with a non-zero status code
        sys.exit(1)

    # Read the contents of the Markdown file
    with open(md_file, 'r') as f:
        md = f.read()

    # Convert the Markdown to HTML
    html = markdown.markdown(md)

    # Write the HTML to the output file
    with open(html_file, 'w') as f:
        f.write(html)

    # Exit the program with a zero status code
    sys.exit(0)
