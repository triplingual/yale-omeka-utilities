'''
For Yale, API calls are in the form 
https://onlineexhibits.library.yale.edu/api/[omeka object, such as sites or users]?sort_by=created&sort_order=DESC&per_page=100&key_identity=[YOUR-API-IDENTITY]&key_credential=[YOUR-API-CREDENTIAL]

This script is written for creating a CSV and is 100% NOT VALID for updating an existing CSV.
'''

import sys
import json
import csv
import requests


secrets = __import__('secrets')
baseApiUrl = secrets.baseURL + '/api/'
basePublicUrl = secrets.baseURL + '/s/'

print("Requesting data for Sites from Omeka S API")
sites = requests.get(baseApiUrl + 'sites?sort_order=DESC&per_page=200&key_identity=' + secrets.identity + '&key_credential=' + secrets.credential).json()
print("Data for " + str(len(sites)) + " Sites retrieved.")

with open('curator-list.csv', 'w', newline='') as csvfile:
	datawriter = csv.writer(csvfile,dialect='excel')
	datawriter.writerow(['Title', 'URI', 'Public?', 'OwnerID', 'Name', 'Email', 'Active?'])
	print("Requesting data for site owners from Omeka S API")
	for x in range(len(sites)):
# 		print('Target URI = ' + baseApiUrl + str(sites[x]['o:owner']['o:id']) +\
# 		'?key_identity=' + secrets.identity + '&key_credential=' + secrets.credential)
# 		print("Requesting data for User with account id " +\
# 		str(sites[x]['o:owner']['o:id']) + " from Omeka S API")
		ownerJSON = requests.get(baseApiUrl + 'users/' + str(sites[x]['o:owner']['o:id']) +\
		'?key_identity=' + secrets.identity + '&key_credential=' + secrets.credential)\
		.json()
		if (x % 5 == 0 and x > 0):
			print("Data for " + str(x) + " Site owners written to CSV")
		datawriter.writerow([sites[x]['o:title'], basePublicUrl + sites[x]['o:slug'], 'Y' if sites[x]['o:is_public'] else 'N', ownerJSON['o:id'], ownerJSON['o:name'], ownerJSON['o:email'], 'Y' if ownerJSON['o:is_active'] else 'N'])
	print("Data for " + str(x+1) + " Sites written to CSV")
