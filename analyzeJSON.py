import json, numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

sampleFile = 'sample.json'
outputFile = 'similarity.np'

with open(sampleFile,'rb') as file:
    authors = json.load(file)

abstracts = []
for author in authors.keys():
   abstracts.append(authors[author]['abstract'])

vect = TfidfVectorizer(min_df=1, stop_words="english")                                                                                                                                                                                                   
tfidf = vect.fit_transform(abstracts)
pairwise_similarity = tfidf * tfidf.T

arr = pairwise_similarity.toarray()
np.fill_diagonal(arr, np.nan)  

np.save(outputFile,arr)