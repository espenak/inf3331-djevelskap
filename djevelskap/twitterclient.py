# Do a twitter search
# See: https://dev.twitter.com/docs/api/1/get/search

from urllib2 import urlopen
from urllib import urlencode
import json
from pprint import pprint


def search(**search_params):
    searchurl = 'http://search.twitter.com/search.json?'
    fullurl = searchurl + urlencode(search_params)
    return json.loads(urlopen(fullurl).read())


results = search(q='Linus Torvalds')
#print results
pprint(results)
