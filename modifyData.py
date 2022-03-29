import pandas as pd
from collections import Counter
from nltk.corpus import stopwords

data = pd.read_csv("Datasets/MBTI 500.csv")

IE = False
NS = False
TF = False
JP = False

create_IE_dict = True

if IE == True:
    def classify(x):
        if "I" in x:
            return "I"
        else:
            return "E"

    data["type"] = data["type"].apply(classify)
    data.to_csv("Datasets/IEclassification.csv")

if NS == True:
    def classify(x):
        if "N" in x:
            return "N"
        else:
            return "S"

    data["type"] = data["type"].apply(classify)
    data.to_csv("Datasets/NSclassification.csv")

if TF == True:
    def classify(x):
        if "T" in x:
            return "T"
        else:
            return "F"

    data["type"] = data["type"].apply(classify)
    data.to_csv("Datasets/TFclassification.csv")

if JP == True:
    def classify(x):
        if "J" in x:
            return "J"
        else:
            return "P"

    data["type"] = data["type"].apply(classify)
    data.to_csv("Datasets/JPclassification.csv")

if create_IE_dict == True:
    stopwords = stopwords.words('english')
    stopwords.append("like")
    introverts_dict = {}
    extroverts_dict = {}

    data = pd.read_csv("Datasets/IEclassification.csv")

    post_dict = {}

    for i in range(len(data['type'])):
        if data['type'][i] not in post_dict:
            post_dict[data['type'][i]] = [data['posts'][i]]
        else:
            post_dict[data['type'][i]].append(data['posts'][i])

    def list_all_words(personality):
        allWords = []
        for i in range(len(post_dict[personality])):
            words = post_dict.get(personality)[i].split()
            words = [w for w in words if w not in stopwords]
            allWords += words
        return allWords

    text = " ".join(list_all_words("I"))
    introverts = Counter(text.split()).most_common(500)
    for word in introverts:
        introverts_dict[word[0]] = [word[1]]
    introverts_df = pd.DataFrame.from_dict(introverts_dict)
    introverts_df = introverts_df.T
    introverts_df.to_csv("Datasets/introverts_df.csv")


    text = " ".join(list_all_words("E"))
    extroverts = Counter(text.split()).most_common(100)
    for word in extroverts:
        extroverts_dict[word[0]] = [word[1]]
    extroverts_df = pd.DataFrame.from_dict(extroverts_dict)
    extroverts_df = extroverts_df.T
    extroverts_df.to_csv("Datasets/extroverts_df.csv")