import json
import urllib.request

def _sortedstores():
    with open('./resources/stores.json') as f:
        stores = json.load(f)
        

    # Sort by name
    sorted_obj = dict(stores)
    sorted_obj = sorted(stores, key=lambda x : x['name'])
    return sorted_obj


allpostcodes = [i['postcode'] for i in _sortedstores()]

def _latitudelongitude():

    returnDict = {}

    values = {'postcodes': [i['postcode'] for i in _sortedstores()] }

    api_endpoint = 'https://api.postcodes.io/postcodes/'

    data = json.dumps(values).encode('utf8')

    req = urllib.request.Request(api_endpoint, data,
            headers={'content-type': 'application/json'})

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())

        for i in range(len(result['result'])):
            print(json.dumps(result['result'][i]['result'], indent=2))
            if result['result'][i]['result'] != None:
                County = result['result'][i]['result']['admin_district']
                Postcode = result['result'][i]['result']['postcode']
                Longitude = result['result'][i]['result']['longitude']
                Latitude = result['result'][i]['result']['latitude']

                returnDict[Postcode] = [County, Longitude, Latitude]
    except Exception as e:
        print(e)

    print(returnDict)

_latitudelongitude()






