#!/usr/bin/env python3
"""
Author : eltor0day
Date   : 2024-04-29
Purpose: convert letters to rants
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="convert letters to rants",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("text", metavar="str", type=str, help="A positional argument")
    parser.add_argument(
        "-o", "--outfile", metavar="str", default="", help="output file"
    )

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """main function"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + "\n")
    out_fh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
