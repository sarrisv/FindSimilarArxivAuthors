# FindSimilarArxivAuthors
Given an author in the dataset this project uses Sklearn text feature extraction to find the most similar authors based on the abstracts of their published papers

## Process
1. Get the data formatted
> `python3 compileJSON.py`
2. Create the csr_matrix of similarity values
> `python3 analyzeJSON.py`
3. Output the list of the most similar authors
> `python3 findSimilar.py [author's name] [# of desired similar authors]` \
> e.g. `python3 findSimilar.py 'Yoshua Bengio' 5`

### Pre-Processed Similarity File
* [link](https://drive.google.com/file/d/1slgjSGBKQmg3D6ODntHztDHcJ5yS-KB6/view?usp=sharing)

### Collaborators
* [hashFactory](https://github.com/hashFactory)

### Special Thanks
* [Neel Shah](https://github.com/neelshah18) for uploading the dataset to Kaggle which can be found [here](https://www.kaggle.com/neelshah18/arxivdataset)
