import json
from flask import Flask, request, render_template
import urllib.request

app = Flask(__name__)

"""
Create a new Python-based application (any framework is fine, we prefer Flask)
Render the list of stores from the stores.json file in alphabetical order through a backend template
Use postcodes.io to get the latitude and longitude for each postcode and render them next to each store location in the template
Build the functionality that allows you to return a list of stores in any given radius of any given postcode
in the UK ordered from north to south and unit test it - no need to render anything
"""

""" Render the list of stores from the stores.json file in alphabetical order through a backend template """
def _sortedstores():

    with open('./resources/stores.json') as f:
        stores = json.load(f)

    sorted_obj = dict(stores)
    sorted_obj = sorted(stores, key=lambda x : x['name'])
    return sorted_obj


""" Use postcodes.io to get the latitude and longitude for each postcode and render them next to each
    store location in the template """
def _longitudelatitude():

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
            if result['result'][i]['result'] != None:
                County = result['result'][i]['result']['admin_district']
                Postcode = result['result'][i]['result']['postcode']
                Longitude = result['result'][i]['result']['longitude']
                Latitude = result['result'][i]['result']['latitude']

                returnDict[Postcode] = [County, Longitude, Latitude]

    except Exception as e:
        print(e)

    return returnDict


""" Build the functionality that allows you to return a list of stores in any given radius of any given postcode
    in the UK ordered from north to south and unit test it - no need to render anything """
def _searchfunctionality(radius, postcode):

    returnDict = {}
    
    try:
        url = 'https://api.postcodes.io/postcodes/{}'.format(postcode)
        data = urllib.request.urlopen(url)
        content = json.loads(data.read())
        returnDict[content['result']['postcode']] = [content['result']['admin_district'], content['result']['longitude'], content['result']['latitude']]
    except Exception as e:
        print(e)

    return returnDict


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        print("post working")
        _radius = request.form['radius']
        _postcode = request.form['postcode']
        return render_template("Tails.html", LocationData = _searchfunctionality(_radius, _postcode))
    else:
        print("default working")
        return render_template('Tails.html', LocationData = _longitudelatitude())
