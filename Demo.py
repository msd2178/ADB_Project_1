__author__ = 'meril'

import urllib2
import Weights
import base64
import re
import json
import MyRocchio

def cleanData(str):
        newStr = re.sub(ur"[\,\|\-\?\[\]\{\}\(\)\"\:\;\!\@\#\$\ %\^\&\*\>\<]|(\.$)|(\.\.\.)", ' ', str)
        wordsList = newStr.lower().split()
        newWordList = []
        for eachWord in wordsList:
            if eachWord not in cachedStopWords:
                newWordList.append(eachWord)
            newWordList = [item for item in newWordList if item.isalpha()] #Remove numeric values from query
        return newWordList

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
                  'you', 'your', 'age', 'concern', 'about' ,
                    'above' ,
                    'after' ,
                    'again' ,
                    'against' ,
                    'all' ,
                    'am' ,
                    'an' ,
                    'and' ,
                    'any' ,
                    'are' ,
                    'aren' ,
                    'as' ,
                    'at' ,
                    'be' ,
                    'because' ,
                    'been' ,
                    'before' ,
                    'being' ,
                    'below' ,
                    'between' ,
                    'both' ,
                    'but' ,
                    'by' ,
                    'can' ,
                    'cannot' ,
                    'could' ,
                    'couldn' ,
                    'did' ,
                    'didn' ,
                    'do' ,
                    'does' ,
                    'doesn' ,
                    'doing' ,
                    'don' ,
                    'down' ,
                    'during' ,
                    'each' ,
                    'few' ,
                    'for' ,
                    'from' ,
                    'further' ,
                    'had' ,
                    'hadn' ,
                    'has' ,
                    'hasn' ,
                    'have' ,
                    'haven' ,
                    'having' ,
                    'he' ,
                    'her' ,
                    'here' ,
                    'here' ,
                    'hers' ,
                    'herself' ,
                    'him' ,
                    'himself' ,
                    'his' ,
                    'how' ,
                    'how' ,
                    'if' ,
                    'in' ,
                    'into' ,
                    'is' ,
                    'isn' ,
                    'it' ,
                    'its' ,
                    'itself' ,
                    'let' ,
                    'me' ,
                    'more' ,
                    'most' ,
                    'mustn' ,
                    'my' ,
                    'myself' ,
                    'no' ,
                    'nor' ,
                    'not' ,
                    'of' ,
                    'off' ,
                    'on' ,
                    'once' ,
                    'only' ,
                    'or' ,
                    'other' ,
                    'ought' ,
                    'our' ,
                    'ours' ,
                    'ourselves' ,
                    'out' ,
                    'over' ,
                    'own' ,
                    'same' ,
                    'shan' ,
                    'she' ,
                    'should' ,
                    'shouldn' ,
                    'so' ,
                    'some' ,
                    'such' ,
                    'than' ,
                    'that' ,
                    'the' ,
                    'their' ,
                    'theirs' ,
                    'them' ,
                    'themselves' ,
                    'then' ,
                    'there' ,
                    'these' ,
                    'they' ,
                    'this' ,
                    'those' ,
                    'through' ,
                    'to' ,
                    'too' ,
                    'under' ,
                    'until' ,
                    'up' ,
                    'using',
                    'very' ,
                    'was' ,
                    'wasn' ,
                    'we' ,
                    'were' ,
                    'weren' ,
                    'what' ,
                    'when' ,
                    'where' ,
                    'which' ,
                    'while' ,
                    'who' ,
                    'whom' ,
                    'why' ,
                    'with' ,
                    'would' ,
                    'wouldn' ,
                    'you' ,
                    'your' ,
                    'yours' ,
                    'yourself' ,
                    'yourselves' ]
objectList =[]
precision = 0.0
count = 1
query = raw_input("Enter the list of query words :").split(" ")
desired_precision = float (raw_input("Enter the precision desired (between 0 and 1): "))

while precision < desired_precision:
    print("ROUND " + str(count) + ":")
    count = count + 1
    queryList = ''
    relevance_count = 0.0
    # Build query list
    for q in query:
        queryList += q + " "

    queryList=urllib2.quote(queryList)

    # Query bing search api
    bingUrl = 'https://api.datamarket.azure.com/Bing/Search/Web?Query=%27'+ queryList +'%27&$top=10&$format=Json'

    accountKey = 'Amj5zEym/93UZqhYv2TvvO9pgzU1mcewT7NNWAm9JMY' # Provide your account key here
    accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
    headers = {'Authorization': 'Basic ' + accountKeyEnc}
    req = urllib2.Request(bingUrl, headers = headers)
    response = urllib2.urlopen(req)
    json_obj = json.load(response)
    result_list = json_obj['d']['results']
    resultCount = len(result_list)

    if resultCount > 0:
        # Add title and summary from results to a list
        for x in range(0,resultCount):

            result_list[x]['Relevant'] = False
            print "\n"
            print "============================================================="
            print( "Title: " + result_list[x]['Title'].encode("utf-8"))
            print( "Description: " + result_list[x]['Description'].encode("utf-8"))
            print( "URL: " + result_list[x]['Url'].encode("utf-8"))
            print "============================================================="
            ans = raw_input("Is it relevant? (y/n) :".encode("utf-8"))
            print "\n"
            if ans == 'y':
                relevance_count += 1
                result_list[x]['Relevant'] = True
            Clean_title = cleanData(result_list[x]['Title'])
            Clean_description = cleanData(result_list[x]['Description'])
            Relevant = result_list[x]['Relevant']
            object = [Clean_title, Clean_description, Relevant]
            objectList.append(object)

        if relevance_count > 0:
            precision = relevance_count/10
            print('Precision: '+ str(precision))
            obj = Weights.Weights()
            (terms, weights) = obj.Weight(objectList)
            rocObject = MyRocchio.Rocchio()
            query= rocObject.RocchioExpansion(query,objectList, terms, weights)
            print(query)
        else:
            print("No relevant results found..Exiting..")
            break
    else:
        print "=======No results found from Bing========="
        break
