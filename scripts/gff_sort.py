#!/usr/bin/env python3
"""Sort gff3 files by feature name."""


import argparse
import itertools


def parse_command_line():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('gff',
                        help='gff3 input file')
    return parser.parse_args()


def main():
    args = parse_command_line()

    # Read line ignoring comment lines and empty lines.
    header_lines = []
    content_lines = []
    with open(args.gff, 'rt') as f:
        for line in f:
            if line.startswith('#'):
                header_lines.append(line.strip())
            elif line.strip():
                content_lines.append(line)

    # Group lines by feature.
    content_lines.sort(key=lambda line : line.split()[2])
    groups = itertools.groupby(content_lines, key=lambda line : line.split()[2])

    # Print sorted gff.
    print('\n'.join(header_lines))
    keys = []
    for feature, group in groups:
        print(''.join(list(group)))
        keys.append(feature)

    # Print the set of all feature names.
    print("# All features: {}".format(', '.join(keys)))


if __name__ == '__main__':
    main()
