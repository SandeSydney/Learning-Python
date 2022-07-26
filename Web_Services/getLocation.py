## Python script that uses google apis to find the location

import urllib.request, urllib.parse, urllib.error
import json

service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter your location:> ')
    if len(address) < 1: break

    url = service_url + urllib.parse.urlencode({'address': address})

    print('Getting {} for You...'.format(url))
    url_hand = urllib.request.urlopen(url)
    data = url_hand.read().decode()
    print('Obtained', len(data), ' items.')

    # load data from the json provided
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failed to get location ===')
        print(data)
        continue

    lat_gotten = js["results"][0]["geometry"]["location"]["lat"]
    lng_gotten = js["results"][0]["geometry"]["location"]["lng"]
    print('Latitude: ', lat_gotten, ' Longitude: ', lng_gotten)
    location = js["results"]["0"]['formatted_address']
    print(location)