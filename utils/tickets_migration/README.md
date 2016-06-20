## Tools to help importing tickets from SF to GitHub

The scripts located in this directory are a set of tools which can be useful to create json files 
containing the list of tickets which should be moved from a Sourceforge project to a given repository.

The list of bugs and feature requests tickets form the SF project can be exported from SF from a page like this: https://sourceforge.net/p/tango-cs/admin/export for the tango-cs project for instance. This export will generate 2 json files containing the list of bug tickets and feature-request tickets.

In the case of the tango-cs project, the list of tango-cs SF tickets will have to be split into several sets of tickets which will be migrated into different GitHub repositories.

The tools in this folder will help to manipulate these json files and to create new json files from them.

gosf2github directory contains the script which is actually doing the migration.
The script is named gosf2github.pl and his a slighlty modified version of [https://github.com/cmungall/gosf2github](https://github.com/cmungall/gosf2github) perl script.

### assignees_set.py

This script takes as input a json files containing a list of SF tickets and returns the list of persons having tickets assigned to them among this list of tickets.

### category_list.py

This script takes as input a json files containing a list of SF tickets and returns the list of possible tickets categories found among this list of tickets.

### filter_tickets.py

This script is able to get all the ticket numbers of the tickets having 
at least one of the labels or belonging to the categories given in parameter or having the ticket number in the ticket number list given as paarameter

If an output filename is specified, the script will extract all the tickets 
containing the given labels, belonging to the given categories and/or having a ticket number in the given ticket number list and save them into the output json file.

### remove_tickets.py

This script is able to remove the tickets having 
at least one of the labels given in parameter or having a ticket number in the specified list.

If an output filename is specified, the script will keep all the tickets 
not containing the given labels nor having the specified ticket number and save them into the output json file.
