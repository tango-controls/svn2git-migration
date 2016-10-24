#!/usr/bin/python

from __future__ import print_function
import sys
import getopt
import json

def usage():
    print(sys.argv[0], '-j <json_file>')
    sys.exit (2)


def main(argv):
    jsonfilename = ''
    try:
        opts, args = getopt.getopt (argv, "hj:", ["jsonfile"])
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-j", "--jsonfile"):
            jsonfilename = arg
    if not jsonfilename:
        print('Please use -j option to specify a json filename')
        sys.exit (3)
    print('json-file is ', jsonfilename)
    jsonfile = open (jsonfilename, "r+")
    data = json.load (jsonfile)

    for page in data["pages"]:
        with open(page["title"] + ".md", 'w') as f:
            print(page["text"].encode('ascii', 'replace'), file=f)

if __name__ == "__main__":
    main(sys.argv[1:])
