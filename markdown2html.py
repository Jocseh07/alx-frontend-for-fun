#!/usr/bin/python3

"""
Markdown to HTML

Usage:
    markdown2html.py <input_file> <output_file>

Arguments:
    <input_file>    Input Markdown file.
    <output_file>   Output HTML file.
"""

import sys
import os
import re


def convert(content):
    # Convert Markdown headings to HTML

    return content


def markdown2html(input_file, output_file):
    # Open the input file in read mode
    with open(input_file, "r") as f:
        # Read the content of the input file
        content = f.read()

    # Convert Markdown headings to HTML
    content = convert(content)

    # Open the output file in write mode
    with open(output_file, "w") as f:
        # Write the modified content to the output file
        f.write(content)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3:
        sys.stderr.write(
            "Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Get the input and output file names from the command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        sys.stderr.write("Missing {}\n".format(input_file))
        sys.exit(1)

    # Convert the Markdown file to HTML (implementation not provided)
    # ...
    markdown2html(input_file, output_file)

    # Print nothing and exit 0 if successful
    sys.exit(0)
