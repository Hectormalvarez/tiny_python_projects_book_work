#!/usr/bin/env python3
"""
Author : codespace <codespace@codespaces-f1ae81>
Date   : 2024-03-20
Purpose: Rock the Casbah
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('text',
                        metavar='str',
                        help='A positional argument')

    return parser.parse_args()


def main():
    """main function"""

    args = get_args()
    pos_arg = args.positional
    print(encode_numbers(pos_arg))

encoding_table = {
    "1": "9",
    "2": "8",
    "3": "7",
    "4": "6",
    "5": "0",
    "6": "4",
    "7": "3",
    "8": "2",
    "9": "1",
    "0": "5"
}

def encode_numbers(string):
    new_string = ""
    for char in string:
        if char in encoding_table:
            new_string += encoding_table[char]
        else:
            new_string += char
    return new_string


if __name__ == '__main__':
    main()
