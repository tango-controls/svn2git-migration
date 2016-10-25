#!/usr/bin/python

import sys
import getopt
import re


def usage():
    print sys.argv[0], '-j <json_file>'
    sys.exit(2)


def main(argv):
    jsonfilename = ''
    try:
        opts, args = getopt.getopt (argv, "hj:", ["jsonfile"])
    except getopt.GetoptError:
        usage ()
    for opt, arg in opts:
        if opt == '-h':
            usage ()
        elif opt in ("-j", "--jsonfile"):
            jsonfilename = arg
    if not jsonfilename:
        print 'Please use -j option to specify a json filename'
        sys.exit(3)
    # print 'json-file is ', jsonfilename

    with open(jsonfilename, "r+") as f:
        data = f.read()

    authors = set(re.findall('"author": "(.*)",',  data))
    assignees = set(re.findall('"assigned_to": "(.*)",',  data))
    reporters = set(re.findall('"reported_by": "(.*)",',  data))

    print '{'
    for name in sorted(assignees):
        print ' "%s" : "ENTER_GH_USER",' % name
    print
    for name in sorted((authors or reporters) - assignees):
        print ' "{name}" : "[{name} @SF](http:/sf.net/u/{name})",'.format(name=name)
    print'}'




if __name__ == "__main__":
    main (sys.argv[1:])
