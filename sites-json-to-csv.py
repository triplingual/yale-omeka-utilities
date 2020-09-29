'''
Note: You'll need to have in hand a JSON file with your sites data in it. 
For Yale, the API call is 
https://onlineexhibits.library.yale.edu/api/sites?sort_by=created&sort_order=DESC&per_page=100&key_identity=[YOUR-API-IDENTITY]&key_credential=[YOUR-API-CREDENTIAL]
This pulls it up in a browser, but it's possible to do it directly from the shell with curl. I just haven't gotten there yet.

This script is NOT GOOD for updating so much, as it would erase the liaison and library if used crudely.
'''

import sys
import json
import csv
from datetime import datetime, date

if len(sys.argv) < 2:
	print("\nYou must supply a JSON file of Omeka site metadata. Exiting script.\n")
	sys.exit()

site_info = open(sys.argv[1], 'r')
parsed_json = json.load(site_info)

with open('exhibit-data.csv', 'w', newline='') as csvfile:
	datawriter = csv.writer(csvfile,dialect='excel')
	datawriter.writerow(['ID', 'Theme', 'Title', 'Summary', 'OwnerID', 'Created', 'LastModified', 'Public?', 'Liaison', 'Library'])
	for x in range(len(parsed_json)):
		datawriter.writerow([parsed_json[x]['o:id'], parsed_json[x]['o:theme'], parsed_json[x]['o:title'], parsed_json[x]['o:summary'], parsed_json[x]['o:owner']['o:id'], datetime.fromisoformat(parsed_json[x]['o:created']['@value']).date().isoformat(), datetime.fromisoformat(parsed_json[x]['o:modified']['@value']).date().isoformat(), parsed_json[x]['o:is_public'], '[liaison placeholder]', '[library placeholder]'])