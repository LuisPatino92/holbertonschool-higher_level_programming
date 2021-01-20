#!/usr/bin/python3
"""This module has a script that adds arguments to list in json repr."""


from sys import argv
from pathlib import Path
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    with open('add_item.json', 'a', encoding='utf-8') as f:
        if Path('add_item.json').stat().st_size == 0:
            c_list = []
        else:
            c_list = load_from_json_file('add_item.json')
        c_list.extend(argv[1:])
        save_to_json_file(c_list, 'add_item.json')
