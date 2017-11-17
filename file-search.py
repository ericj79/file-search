#! python
import argparse
import os


parser = argparse.ArgumentParser(description="Look for string in files")
parser.add_argument('search', help="The string to search for")
parser.add_argument('--dir', dest="directory", default=os.getcwd(), help="Optional directory to search. Default: current directory")

args = parser.parse_args()

print(args.search) 
print(args.directory)
