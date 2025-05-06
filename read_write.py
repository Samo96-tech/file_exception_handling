#!/usr/bin/env python3
import sys

def transform_line(line: str) -> str:
    """
    Transform a line of text. Example: uppercase and strip trailing newline.
    """
    return line.rstrip().upper() + "\n"


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>")
        sys.exit(1)

    input_path, output_path = sys.argv[1], sys.argv[2]

    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except Exception as e:
        print(f"Error reading '{input_path}': {e}")
        sys.exit(1)

    transformed = [transform_line(line) for line in lines]

    try:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.writelines(transformed)
        print(f"Successfully wrote transformed content to '{output_path}'")
    except Exception as e:
        print(f"Error writing to '{output_path}': {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
