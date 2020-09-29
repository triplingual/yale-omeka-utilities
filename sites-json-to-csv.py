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