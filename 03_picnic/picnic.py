#!/usr/bin/env python3
"""
Author : eltor0day
Date   : 2024-03-04
Purpose: create picnic list
"""

import argparse


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="create picnic list",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("items", metavar="str", help="Items we are bringing", nargs="+")
    parser.add_argument("-s", "--sorted", help="sort the output", action="store_true")

    return parser.parse_args()


def main():
    """main function"""

    args = get_args()

    if args.sorted:
        args.items.sort()

    items = ""
    quantity = len(args.items)
    if quantity == 1:
        items = args.items[0]
    elif quantity == 2:
        items = " and ".join(args.items)
    elif quantity > 2:
        items =  ", ".join(args.items[:-1]) + ", and " + args.items[-1]
    
    print(f"You are bringing {items}.")


if __name__ == "__main__":
    main()
