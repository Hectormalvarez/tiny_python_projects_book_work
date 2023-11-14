#!/usr/bin/env python3
"""
Author : codespace <codespace@codespaces-145c34>
Date   : 2023-10-28
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='stupid word game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A word argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main function"""

    args = get_args()
    word_arg = args.word
    article = 'an' if word_arg[0].lower() in 'aeiou' else 'a'

    print(f"Ahoy, Captain, {article} {word_arg} off the larboard bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
