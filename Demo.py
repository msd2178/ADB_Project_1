__author__ = 'meril'

import urllib2
import Weights
import base64
import re
import json
from porter2 import stem

def cleanData(str):
        newStr = re.sub(ur"[\,\|\-\?\[\]\{\}\(\)\"\:\;\!\@\#\$\ %\^\&\*\>\<]|(\.$)|(\.\.\.)", ' ', str)
        wordsList = newStr.lower().split()
        #print wordsList
        newWordList = []
        for eachWord in wordsList:
            if eachWord not in cachedStopWords:
                newWordList.append(eachWord)
        #print newWordList
        newerWordList = []
        for eachWord in newWordList:
            newerWordList.append(stem(eachWord))
        #print newerWordList
        return newerWordList

cachedStopWords = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an',
                  'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot',
                  'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from',
                  'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however',
                  'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may',
                  'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often',
                  'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should',
                  'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these',
                  'they', 'this', 'tis', 'to', 'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what',
                  'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet',
                  'you', 'your']
objectList =[]
relevance_count = 0.0
query = raw_input("Enter the list of query words").split(" ")
print query
queryList = ""
#print type(query)   #list
l = len(query)
for q in query:
    queryList += '&Query=%27' + q # CHECK QUERY FOR 1ST PARAMETER
#print queryList
desired_precision = float (raw_input("Enter the precision desired"))
print desired_precision
#print type(desired_precision)

bingUrl = 'https://api.datamarket.azure.com/Bing/Search/Web?Query=%27'+ queryList +'%27&$top=10&$format=Json'
print bingUrl
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
result_list = json_obj['d']['results']
#print json_obj
#print type(json_obj)
#print "dict['Name']: ", dict['Name'];
l=  len(result_list)
print l
for x in range(0,l):
    print "The entry number", x+1, "is :"
    print "Title is :", result_list[x]['Title']
    print "Description is : ", result_list[x]['Description']
    print "URL is : ", result_list[x]['Url']
    ans = raw_input("Is it relevant? (y/n)")
    if ans == 'y':
        relevance_count += 1
    Clean_title = cleanData(result_list[x]['Title'])
    Clean_description = cleanData(result_list[x]['Description'])
    object = [Clean_title, Clean_description]
    objectList.append(object)
    print 'Clean_title is : ', ', '.join(Clean_title)
    print 'Clean_description is : ', ', '.join(Clean_description)
    print objectList
    print type(objectList)
    #object.title = Clean_title
    #object.description = Clean_description
    #print object


print relevance_count

precision = relevance_count/10.0
print precision

print "==============CALLING WEIGHTS FUNCTION =============="
obj = Weights.Weights()
obj.Weight(objectList)