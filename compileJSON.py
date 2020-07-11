import json
from operator import itemgetter  

with open('arxivData.json') as file:
    data = json.load(file);

sort = {}
db = {}

for paper in data:
    for author in paper['author'].replace('{\'name\': \'','').replace('\'}','').replace('[','').replace(']','').split(', '):
        if not author in db:
            sort[author] = 1
            db[author] = {'abstract' : paper['summary'].replace('\n',' '), 'titles' : [paper['title'].replace('\n','')]}
        else:
            sort[author] += 1
            db[author]['abstract'] += ' '+paper['summary'].replace('\n',' ')
            db[author]['titles'].append(paper['title'].replace('\n','')) 

sorted_keys = sorted(sort.items(), key=itemgetter(1), reverse=True)
output = {}
for author, papers in sorted_keys:
    output[author] = db[author]

with open('sample.json', 'wb') as json_file:
  json.dump(output, json_file, indent=4, sort_keys=True)
