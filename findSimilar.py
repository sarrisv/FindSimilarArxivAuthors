import json, sys, numpy as np

sampleFile = 'sample.json'
outputFile = 'similarity'

if sys.argv < 3:
    print('Not enough args - [author] [# of desired similar authors]')
    sys.exit

input = sys.argv[1]   # 'Yoshua Bengio' - most published author
numberOfSimilarAuthors = int(sys.argv[2])

def max(similarity, n):
    temp = similarity
    maxVals = []
    for i in range(0, n):
        j = np.nanargmax(temp)
        maxVals.append(j)
        temp[j] = np.nan
    return maxVals

with open(sampleFile,'rb') as file:
    dict = json.load(file)

authors = []
for author in dict.keys():
    authors.append(author)

similarities = np.load(outputFile)

input_idx = authors.index(input)  

maxVals = max(similarities[input_idx], numberOfSimilarAuthors)

for i in maxVals:
    print(authors[i])
