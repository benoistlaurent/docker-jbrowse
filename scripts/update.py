
"""Copy files from root data directory to current directory."""

from __future__ import print_function

import filecmp
import os
import shutil


# Directory where original data is.
ROOT_DATA_DIR = '../../../../cv11_transcriptome'

# Map final name with original name.
NAME_MAP = {'cv11.fa': 'cv11.fasta',
            'cv11.gff3': 'cv11_annotation.gff3'}



def copy_file(source, target):
    """Ask if a file should be copied from `source` to `target` and copy
    it if answer is yes."""
    answer = raw_input("Copy {} --> {} ?[Y] ".format(source, target))
    if answer.upper() not in ('YES', 'Y', ''):
        raise ValueError('Unrecognized answer')
    shutil.copyfile(source, target)


def copy_unless_same_file(source, target):
    if filecmp.cmp(source, target):
        print("Ignoring {}: unchanged".format(target))
    else:
        copy_file(source, target)


def main():
    # Files in current directory.
    filelist = os.listdir('.')

    # Remove current script from list.
    filelist.remove(os.path.basename(__file__))

    # Remove all configuration files from list.
    print("Ignoring *.conf")
    filelist = [fname for fname in filelist if not fname.endswith('.conf')]

    for fname in filelist:
        if fname in NAME_MAP:
            source = os.path.join(ROOT_DATA_DIR, NAME_MAP[fname])
            target = fname
        else:
            source = os.path.join(ROOT_DATA_DIR, fname)
            target = fname
            if os.path.exists(source):
                copy_unless_same_file(source, target)
            else:
                print("Ignoring {}".format(source))
            


if __name__ == '__main__':
    main()



