__author__ = 'meril'

import urllib2
import base64
import json

query = raw_input("Enter the list of query words").split(" ")
print query
#print type(query)

precision = float (raw_input("Enter the precision desired"))
print precision
#print type(precision)

bingUrl = 'https://api.datamarket.azure.com/Bing/Search/Web?Query=%27gates%27&$top=10&$format=Json'
#Provide your account key here
accountKey = ''

accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
headers = {'Authorization': 'Basic ' + accountKeyEnc}
req = urllib2.Request(bingUrl, headers = headers)
response = urllib2.urlopen(req)
#content = response.read()
#content contains the xml/json response from Bing.
#print content
#print type(content)
json_obj = json.load(response)
#print json_obj
#print type(json_obj)
#print "dict['Name']: ", dict['Name'];
l=  len(json_obj['d']['results'])
print l
for x in range(0,l):
    print "The entry number", x+1, "is :"
    print "Title is :", json_obj['d']['results'][x]['Title']
    print "Description is : ", json_obj['d']['results'][x]['Description']
    print "URL is : ", json_obj['d']['results'][x]['Url']
    print
