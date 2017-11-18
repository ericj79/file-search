#! python
import argparse
from os import listdir, getcwd
from os.path import isfile, join, abspath


parser = argparse.ArgumentParser(description="Look for string in files")
parser.add_argument('search', help="The string to search for")
parser.add_argument('--dir', dest="directory", default=getcwd(), help="Optional directory to search. Default: current directory")

args = parser.parse_args()

needle = args.search
path = abspath(args.directory)
print "\nSearching all files in " + path + " for the '" + needle + "':\n"

allFiles = [filename for filename in listdir(path) if isfile(join(path, filename))]

fileMatches = 0
contentMatches = 0
for filename in allFiles:
    if needle in filename:
        print "File Name match: " + filename
        fileMatches = fileMatches + 1
    if needle in open(join(path, filename)).read():
        print "Contents match: " + filename
        contentMatches = contentMatches + 1

print "\n{} file names matched".format(fileMatches)
print "{} file contents matched".format(contentMatches)
