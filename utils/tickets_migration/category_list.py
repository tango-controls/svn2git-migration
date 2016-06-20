#!/usr/bin/python

import sys
import getopt
import json

def usage():
	print sys.argv[0],' -j <json_file>'
	sys.exit(2)

def main(argv):
	jsonfilename = ''
	try:
		opts, args = getopt.getopt(argv,"hj:",["jsonfile"])
	except getopt.GetoptError:
		usage()
	for opt, arg in opts:
		if opt == '-h':
			usage()
		elif opt in ("-j", "--jsonfile"):
			jsonfilename = arg
	if not jsonfilename:
		print 'Please use -j option to specify a json filename'
		usage()
	print 'json-file is ', jsonfilename
	jsonfile = open(jsonfilename,"r+")
	data = json.load(jsonfile)
	
	categories_set = set([])
	tickets = data["tickets"]
	for ticket in tickets:
		if "_category" in ticket["custom_fields"]:
			categories_set.add(ticket["custom_fields"]["_category"])
	
	for category in categories_set:
		print category
	
if __name__ == "__main__":
	main(sys.argv[1:])
