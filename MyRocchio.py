# Rocchio implementation for query expansion. 
# Finds the top 2 weighted terms in the list of words.
# Uses the Term-Weight output of Weights class and orders them correctly. 

import math

class Rocchio:
    def __init__(self):
        self.orderedTermWeights = [] # Eventually select the top 2 from this list
        self.termWeights = {} # All the rocchio term-weights 
        self.terms = []
        self.weights = [] 
        self.alpha = 1 # Reasonable values as mentioned in Introduction to Information Retrieval, Chapter 9.
        self.beta = 0.75
        self.gamma = 0.15
        return 
    def RocchioAlgo(self, oldQuery, docList, objTerms, objWeights):
        self.terms = objTerms
        self.weights = objWeights
        # Find the number of relevant and irrelevant docs and compute parameters
        relevantDocs = 0
        irrelevantDocs = 0
        for i in range(len(docList)):
            [words, desVector, relevant]  = docList[i]
            if relevant is True:
                relevantDocs += 1
            else:
                irrelevantDocs += 1
        alpha = self.alpha
        beta = self.beta/relevantDocs
        gamma = self.gamma/irrelevantDocs

        # All the terms in original query should be in the terms list.
        for term in oldQuery:
            if term not in self.terms:
                (self.terms).append(term)
                for i in range(len(self.weights)):
                    self.weights[i][term] = 0 # Since the term was not found in any document
        
        # Form the rocchio query vector
        sum = 0
        for term in self.terms:
            if term in oldQuery:
                self.termWeights[term] = 1
                sum = sum + 1
            else:
                self.termWeights[term] = 0

        # Normalize the rocchio query vector
        sum = math.sqrt(sum)
        for term in self.terms:
            self.termWeights[term] /= sum
        
        # The algorithm
        for term in self.terms:
            self.termWeights[term] = self.termWeights[term] * alpha
            for i in range(len(docList)):
                [words, desVector, relevant]  = docList[i]
                if relevant:
                    self.termWeights[term] += beta * self.weights[i][term]
                else:
                    self.termWeights[term] -= gamma * self.weights[i][term]
        return
    
    def RocchioOrder(self):
        d = self.termWeights
        dSorted = sorted(d.items(), key = lambda d:d[1], reverse=True) # Order terms according to weight
        self.orderedTermWeights = dSorted
        return

    def RocchioExpansion(self, oldQuery, docList, objTerms, objWeights):
        self.RocchioAlgo(oldQuery, docList, objTerms, objWeights)
        self.RocchioOrder()
        n = 0
        # Add the top 2 weighted terms
        for term in self.orderedTermWeights:
            if term[0] not in oldQuery:
                oldQuery.append(term[0])
                n = n + 1
                if n == 2:
                    break

        # Re-order terms
        modifiedQueryTerms = {}
        for term in oldQuery:
            if term in self.termWeights:
                modifiedQueryTerms[term] = self.termWeights[term]
            else:
                modifiedQueryTerms[term] = 0
        d = modifiedQueryTerms
        dSorted = sorted(d.items(), key=lambda d: d[1], reverse=True)
        sortedTermList = []
        for t in dSorted:
            sortedTermList.append(t[0])

        return sortedTermList