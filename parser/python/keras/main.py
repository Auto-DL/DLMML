import json
import os
import sys
from pprint import pprint

from .write import write_to_file


def generate_code(inputs, filename="test.py", output_dir=''):
    """Trigger function to generate code from JSON."""
    try:
        write_to_file(filename, inputs, output_dir)
        return 0, None
    except Exception as e:
        return 1, e


if __name__ == "__main__":
    print("Not yet implemented, please use generator for now...")
