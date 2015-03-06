__author__ = 'meril'

import math

class Weights:

    def Vector(self, objectList):
        self.words = [] #list of all words in all doc descriptions
        self.desVector = []
        for i in range(len(objectList)):
            description = objectList[i][1]
            for w in description:
                if w not in self.words:
                    self.words.append(w)
        for i in range(len(objectList)):
            description = objectList[i][1] #description of i th doc
            self.desVector.append({}) #create dictionary for i th doc
            for w in self.words:
                self.desVector[i][w] = 0
            for w in description:
                self.desVector[i][w] += 1 #frequency of words in description
        return (self.words, self.desVector)



    def Weight(self, objectList):
        self.WeightV = []
        t=1
        [words, desVector] = self.Vector(objectList)
        N = len(objectList)
        for i in range(N):
            self.WeightV.append({})
            sum = 0
            for w in words:
                if self.desVector[i][w] == 0:
                    self.WeightV[i][w] = 0
                else:
                    tf = self.desVector[i][w]
                    df = 0
                    for j in range(N):
                        if self.desVector[j][w] > 0:
                            df += 1
                    d = float(N)/float(df)
                    self.WeightV[i][w] = tf * (math.log(d))
                sum += math.pow(self.WeightV[i][w], 2)
            sum = math.sqrt(sum)
            for t in self.words:
                self.desVector[i][t] /= sum
        return (self.words, self.WeightV)