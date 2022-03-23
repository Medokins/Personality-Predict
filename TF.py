import pandas as pd
from collections import Counter

data = pd.read_csv("Datasets/TFclassification.csv")

#first I want to get most frequent words in T/F classification
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

text = " ".join(list_all_words("T"))
thinking = Counter(text.split()).most_common(14)[4:]

text = " ".join(list_all_words("F"))
feeling = Counter(text.split()).most_common(14)[4:]

print(f"Thinking: {thinking}")
print(f"Feeling: {feeling}")