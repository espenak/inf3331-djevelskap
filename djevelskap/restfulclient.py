import urllib2
import json



def get_all_deliveries(url):
    return json.loads(urllib2.urlopen(url).read())

def get_delivery(url, id):
    return json.loads(urllib2.urlopen(url + str(id)).read())



url = 'http://localhost:8000/delivery/'
print get_all_deliveries(url)
print get_delivery(url, 1)
