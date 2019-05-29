import json
import collections
import urllib.request
from operator import itemgetter
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

"""
Create a new Python-based application (any framework is fine, we prefer Flask)
Render the list of stores from the stores.json file in alphabetical order through a backend template
Use postcodes.io to get the latitude and longitude for each postcode and render them next to each store-location in the template
Build the functionality that allows you to return a list of stores in any given radius of any given postcode
in the UK ordered from north to south and unit test it - no need to render anything
"""

def read_jsonfile():
    # Open stores.json and return json obj
    with open('./resources/stores.json') as f:
        stores = json.load(f)

    return stores

""" Render the list of stores from the stores.json file in alphabetical order through a backend template """
""" Use postcodes.io to get the latitude and longitude for each postcode and render them next to each
    store location in the template """
def render_alphabetically_longitude_latitude():

    returnDict = {}

    # Make dictionary with all postcodes to use "Bulk Postcode Lookup"
    values = {'postcodes': [i['postcode'] for i in read_jsonfile()]}

    # Bulk Postcode Lookup api end point
    api_endpoint = 'https://api.postcodes.io/postcodes/'

    data = json.dumps(values).encode('utf8')

    # Use correct request and headers for post method
    req = urllib.request.Request(api_endpoint, data,
            headers={'content-type': 'application/json'})

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())

        # Look through response and add relevant data to dictionary if it is not null
        for i in range(len(result['result'])):
            if result['result'][i]['result'] != None:
                County = result['result'][i]['result']['admin_district']
                Postcode = result['result'][i]['result']['postcode']
                Longitude = result['result'][i]['result']['longitude']
                Latitude = result['result'][i]['result']['latitude']

                returnDict[Postcode] = [County, Longitude, Latitude]

    except Exception as e:
        print(e)

    # Render list of stores in alphabetical order
    return {k: returnDict[k] for k in sorted(returnDict, key = returnDict.get)}


""" Build the functionality that allows you to return a list of stores in any given radius of any given postcode
    in the UK ordered from north to south and unit test it - no need to render anything """
def search_postcode_radius(radius, postcode):

    returnDict = {}

    try:
        # Retrieve Longitude and Latitude from postcode
        individual_url = 'https://api.postcodes.io/postcodes/{}'.format(postcode)
        individual_url_data = urllib.request.urlopen(individual_url)
        _longlat = json.loads(individual_url_data.read())

        # Pass Long and Lat into this end points to get all admin_district's
        url = 'https://api.postcodes.io/outcodes?lon={}&lat={}?radius={}?limit=99'.format(_longlat['result']['longitude'],
                                                                                          _longlat['result']['latitude'], radius)
        data = urllib.request.urlopen(url)
        content = json.loads(data.read())

        # Check if Stores are within the list of admin_district's
        # if they admin_district's match then the store is within the given radius so it is added to the dictionary
        for i in range(len(content['result'])):
            if content['result'][i] != None:
                for postcode, longlat in _longitudelatitude().items():
                    if longlat[0] in content['result'][i]['admin_district']:
                        County = longlat[0]
                        Postcode = postcode
                        Longitude = longlat[1]
                        Latitude = longlat[2]

                        # Add to dictonary and return
                        returnDict[Postcode] = [County, Longitude, Latitude]
    except Exception as e:
        print(e)

    # North to south
    return {k: returnDict[k] for k in sorted(returnDict)}


@app.route('/', methods=['POST', 'GET'])
def Tails():

    # Check if User has made submitted a form with postcode and radius,
    # Retrieve given radius and postcode and return a template with the data return from _searchfunctionality
    if request.method == 'POST':
        _radius = request.form['radius']
        _postcode = request.form['postcode']
        return render_template("Tails.html", LocationData = search_postcode_radius(_radius, _postcode))
    else:
        # Normal template with all stores listed alphabetically
        return render_template('Tails.html', LocationData = render_alphabetically_longitude_latitude())
