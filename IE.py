import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import GaussianNB
from collections import Counter

data = pd.read_csv("Datasets/IEclassification.csv")

#first I want to get most frequent words in I/E classification
post_dict = {}
for i in range(len(data['type'])):
    if data['type'][i] not in post_dict:
        post_dict[data['type'][i]] = [data['posts'][i]]
    else:
        post_dict[data['type'][i]].append(data['posts'][i])

def list_all_words(personality):
    allWords = []
    for i in range(len(post_dict[personality])):
        allWords += [post_dict.get(personality)[i]]
    return allWords

text = " ".join(list_all_words("I"))
introverts = Counter(text.split()).most_common(11)

text = " ".join(list_all_words("E"))
extroverts = Counter(text.split()).most_common(11)

print(f"Intoverts: {introverts}")
print(f"Extoverts: {extroverts}")