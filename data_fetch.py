from tableausdk import *
from tableausdk.HyperExtract import *
import dataextract as tde
import json
import requests as re
from requests.auth import HTTPBasicAuth
#tableau data fetch

#fetch data
def get(call):
	r = re.get(call, auth=HTTPBasicAuth('', api_key), headers=headers)
	if check_err(r):
		return None
	return r.json()

api_key = 'xx'
list_entry = ''

api_call = 'https://api.affinity.co/lists/17698 -u :' + api_key
#+ '/field-values?list_entry_id=' + list_entry
dataset = get(api_call)

#add headers to data

#create blank tableau extract
dataExtract = tde.Extract('affinityExtract.tde')

#create extract schema: define columns with correct data types
dataSchema = tde.TableDefinition()
dataSchema.addColumn('comapany',	tde.Type.CHAR_STRING)
dataSchema.addColumn('source',		tde.Type.CHAR_STRING)

table = dataExtract.addTable('Extract',dataSchema)
#fill extract with data: one by one row
newRow = tde.Row(dataSchema)
for i in range(0, len(dataset)):
	newRow.setCharString		(0, dataset['company'][i])
	newRow.setCharString		(1, dataset['source'][i])
	table.insert(newRow)

dataExtract.close()
print('done')
