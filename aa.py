import json
import urllib.request

import json

allpostcodes = ["OX49 5NU", "M32 0JG", "NE30 1DP"]
#allpostcodes = [i['postcode'] for i in sortedstores] # Getting postcodes from json file

values = {}
# creating a dictionary and keeping `postcodes` and key and
# the postcode's as the value as shown in the example
values['postcodes'] = allpostcodes 

api_endpoint = 'https://api.postcodes.io/postcodes/'
data = json.dumps(values).encode('utf8')
req = urllib.request.Request(api_endpoint, data,
        headers={'content-type': 'application/json'})
try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read())
        print(json.dumps(result, indent=2))
except Exception as e:
    print(e)
