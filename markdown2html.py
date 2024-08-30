#!/usr/bin/python3

"""
Markdown to HTML

Usage:
    markdown2html.py <input_file> <output_file>

Arguments:
    <input_file>    Input Markdown file.
    <output_file>   Output HTML file.
"""

import re
import sys
import os


def convertHeading(content):
    # Convert Markdown heading to HTML
    newContent = []
    for line in content:
        match = re.match(r"^(#+) (.*)", line)
        if match:
            level = len(match.group(1))
            title = match.group(2)
            line = "<h{0}>{1}</h{0}>\n".format(level, title)
        newContent.append(line)

    return newContent


def convertUnordered(content):
    # Convert unordered list to HTML
    newContent = []
    list_stack = []

    for i, line in enumerate(content):
        match = re.match(r"^- (.*)", line)
        if match:
            item = match.group(1)
            line = "<li>{}</li>\n".format(item)
            if not list_stack or i - 1 not in list_stack:
                list_stack.append(i)
                newContent.append("<ul>\n")
            else:
                list_stack.append(i)
            newContent.append(line)
        else:
            if list_stack:
                newContent.append("</ul>\n")
                list_stack.pop()
            newContent.append(line)

    while list_stack:
        newContent.append("</ul>\n")
        list_stack.pop()

    return newContent


def convertOrdered(content):
    # Convert ordered list to HTML
    newContent = []
    list_stack = []

    for i, line in enumerate(content):
        match = re.match(r"^\* (.*)", line)
        if match:
            item = match.group(1)
            line = "<li>{}</li>\n".format(item)
            if not list_stack or i - 1 not in list_stack:
                list_stack.append(i)
                newContent.append("<ol>\n")
            newContent.append(line)
        else:
            if list_stack:
                newContent.append("</ol>\n")
            newContent.append(line)

    while list_stack:
        newContent.append("</ol>\n")
        list_stack.pop()

    return newContent


def convert(content):
    # Convert Markdown headings to HTML
    content = convertHeading(content)
    content = convertUnordered(content)
    content = convertOrdered(content)

    content = "".join(content)

    return content


def markdown2html(input_file, output_file):
    # Open the input file in read mode
    with open(input_file, "r") as f:
        # Read the content of the input file
        content = f.readlines()

    # Convert Markdown headings to HTML
    content = convert(content)

    # Open the output file in write mode
    with open(output_file, "w") as f:
        # Write the modified content to the output file
        f.writelines(content)


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
