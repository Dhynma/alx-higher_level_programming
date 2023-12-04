#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print the number of and list of arguments"""

    arguments = sys.argv[1:]
    count = len(arguments)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    for i, arg in enumerate(arguments):
        print(f"{i + 1}: {arg}")
