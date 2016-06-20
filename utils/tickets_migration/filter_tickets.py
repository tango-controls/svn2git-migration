#!/usr/bin/python

import sys
import getopt
import json

def usage():
	print 'This script is able to get all the ticket numbers of the tickets having '
	print 'at least one of the labels or belonging to the categories given in parameter or having the ticket number in the ticket number list given as paarameter'
	print
	print 'If an output filename is specified, the script will extract all the tickets '
	print 'containing the given labels, belonging to the given categories and/or having a ticket number in the given ticket number list '
	print 'and save them in the output json file'
	print sys.argv[0], '-j <json_file> [-o <output_json_file>] '
	print '             [-c "Category1,Category2,...,Category3"] '
	print '             [-n "n1,n2,...,n3"] '
	print '             [-l <label1>,label2,...labelx]'
	sys.exit(2)

def extract_tickets_to_json_file(tickets,tickets_num_set,outputjsonfilename):
	if not outputjsonfilename:
		return
	filtered_tickets = []
	for ticket_num in sorted(tickets_num_set):
		for ticket in tickets:
			if ticket["ticket_num"] == ticket_num:
				filtered_tickets.append(ticket)
	labelled_tickets_json_object = { "tickets" : filtered_tickets }
	with open(outputjsonfilename,'w') as outfile:
		json.dump(labelled_tickets_json_object,outfile,indent=4)
	print 'tickets extracted to ', outputjsonfilename
#	print json_object

def main(argv):
	jsonfilename = ''
	outputjsonfilename = ''
	labels = []
	categories = []
	tickets_num_list = []
	tickets_num_set = set()
	try:
		opts, args = getopt.getopt(argv,"hj:o:n:l:c:",["jsonfile","outputjsonfile","tickets_num_list","labels","categories"])
	except getopt.GetoptError:
		usage()
	for opt, arg in opts:
		if opt == '-h':
			usage()
		elif opt in ("-j", "--jsonfile"):
			jsonfilename = arg
		elif opt in ("-o", "--outputjsonfile"):
			outputjsonfilename = arg
		elif opt in ("-n", "--tickets_num_list"):
			tickets_num_list_str = arg.split(',')
			for t in tickets_num_list_str:
				tickets_num_set.add(int(t))
		elif opt in ("-l", "--labels"):
			labels = arg.split(',')
		elif opt in ("-c", "--categories"):
			categories = arg.split(',')
	if not jsonfilename:
		print 'Please use -j option to specify a json filename'
		usage()
	print 'json-file is ', jsonfilename
	if len(labels) == 0 and len(categories)==0 and len(tickets_num_list) == 0:
		print 'Please specify at least one label, one category or one ticket number'
		usage()
	jsonfile = open(jsonfilename,"r+")
	data = json.load(jsonfile)
	
	for ticket_num in tickets_num_list:
		tickets_num_set.add(ticket_num)
	for ticket in data["tickets"]:
		for label in ticket["labels"]:
			for input_label in labels:
				if label == input_label:
					tickets_num_set.add(ticket["ticket_num"])
		if "_category" in ticket["custom_fields"]:
			for input_category in categories:
				if input_category == ticket["custom_fields"]["_category"]:
					tickets_num_set.add(ticket["ticket_num"])
	for ticket_num in sorted(tickets_num_set):
		print ticket_num
		
	if outputjsonfilename:
		extract_tickets_to_json_file(data["tickets"], tickets_num_set, outputjsonfilename)
	
if __name__ == "__main__":
	main(sys.argv[1:])
