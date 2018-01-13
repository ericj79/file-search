#! python
"""Simple script to find files in a directory that contain a string in the file name or contents."""

# import needed libraries
import argparse
from os import listdir, getcwd
from os.path import isfile, join, abspath

# Parse command line arguments. we will need a string to search for and
PARSER = argparse.ArgumentParser(description="Look for string in files")
PARSER.add_argument('search', help="The string to search for")
PARSER.add_argument('--dir', dest="directory", default=getcwd(),
                    help="Optional directory to search. Default: current directory")

ARGS = PARSER.parse_args()

NEEDLE = ARGS.search
PATH = abspath(ARGS.directory)
print "\nSearching all files in " + PATH + " for the '" + NEEDLE + "':\n"

ALL_FILES = [filename for filename in listdir(
    PATH) if isfile(join(PATH, filename))]

FILE_MATCHES = 0
CONTENT_MATCHES = 0
for filename in ALL_FILES:
    if NEEDLE in filename:
        print "File Name match: " + filename
        FILE_MATCHES = FILE_MATCHES + 1
    if NEEDLE in open(join(PATH, filename)).read():
        print "Contents match: " + filename
        CONTENT_MATCHES = CONTENT_MATCHES + 1

print "\n{} file names matched".format(FILE_MATCHES)
print "{} file contents matched".format(CONTENT_MATCHES)
