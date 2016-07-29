#!/usr/bin/env python3

"""Remove the 'Parent' attribute from GFF3 files."""


import argparse
import re


def parse_command_line():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('gff3')
    return parser.parse_args()


def main():
    args = parse_command_line()

    regex = re.compile('(;?Parent=.*);?')

    with open(args.gff3, 'rt') as f:
        for line in f:
            match = regex.search(line)
            if match:
                line = line[0:match.start()] + line[match.end():]
            print(line, end='')






if __name__ == '__main__':
    main()
