'''Simple web api call to get city lattitude and longitude using googleapis'''
import urllib.request
import json

city='newyork'
url = 'http://maps.googleapis.com/maps/api/geocode/json?address='+city+'&sensor=false'

data_in_json = urllib.request.urlopen(url)


data = json.loads((data_in_json.read()).decode('utf-8'))


for i in data['results']:
    city_lat= i['geometry']['location']['lat']
    city_lng= i['geometry']['location']['lng']

print('City: ',city,'\nLattitude: ',city_lat,"\nLongitude: ",city_lng)