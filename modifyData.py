import pandas as pd
from collections import Counter
from nltk.corpus import stopwords

data = pd.read_csv("Datasets/MBTI 500.csv")
stopwords = stopwords.words('english')
stopwords.append("like")

IE = False
NS = False
TF = False
JP = False

create_IE_dict = False
create_NS_dict = False
create_TF_dict = False
create_JP_dict = False

def prepare_post(post):

    cleared_post = []
    
    words = post.split(" ")
    words = [w for w in words if w not in stopwords]    
    cleared_post +=  words
    cleared_post = ' '.join(str(x) for x in cleared_post)

    cleared_post = cleared_post.replace(".","")
    cleared_post = cleared_post.replace("'","")
    cleared_post = cleared_post.replace(",","")
    cleared_post = cleared_post.replace(":","")
    cleared_post = cleared_post.replace(";","")
    cleared_post = cleared_post.replace("!","")
    cleared_post = cleared_post.replace("?","")
    
    return cleared_post

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

def list_all_words(personality):
    allWords = []
    for i in range(len(post_dict[personality])):
        words = post_dict.get(personality)[i].split()
        words = [w for w in words if w not in stopwords]
        allWords += words
    return allWords

if create_IE_dict == True:
    introverts_dict = {}
    extroverts_dict = {}

    data = pd.read_csv("Datasets/IEclassification.csv")

    post_dict = {}

    for i in range(len(data['type'])):
        if data['type'][i] not in post_dict:
            post_dict[data['type'][i]] = [data['posts'][i]]
        else:
            post_dict[data['type'][i]].append(data['posts'][i])

    text = " ".join(list_all_words("I"))
    introverts = Counter(text.split()).most_common(500)
    for word in introverts:
        introverts_dict[word[0]] = [word[1]]
    introverts_df = pd.DataFrame.from_dict(introverts_dict)
    introverts_df = introverts_df.T
    introverts_df.columns = ["count"]
    count = introverts_df["count"].sum()
    introverts_df["count"] =  introverts_df["count"].div(count)
    introverts_df.to_csv("Datasets/introverts_df.csv")

    text = " ".join(list_all_words("E"))
    extroverts = Counter(text.split()).most_common(500)
    for word in extroverts:
        extroverts_dict[word[0]] = [word[1]]
    extroverts_df = pd.DataFrame.from_dict(extroverts_dict)
    extroverts_df = extroverts_df.T
    extroverts_df.columns = ["count"]
    count = extroverts_df["count"].sum()
    extroverts_df["count"] =  extroverts_df["count"].div(count)
    extroverts_df.to_csv("Datasets/extroverts_df.csv")

if create_NS_dict == True:
    intuition_dict = {}
    sensing_dict = {}

    data = pd.read_csv("Datasets/NSclassification.csv")

    post_dict = {}
    for i in range(len(data['type'])):
        if data['type'][i] not in post_dict:
            post_dict[data['type'][i]] = [data['posts'][i]]
        else:
            post_dict[data['type'][i]].append(data['posts'][i])


    text = " ".join(list_all_words("N"))
    intuition = Counter(text.split()).most_common(500)
    for word in intuition:
        intuition_dict[word[0]] = [word[1]]
    intuition_df = pd.DataFrame.from_dict(intuition_dict)
    intuition_df = intuition_df.T
    intuition_df.columns = ["count"]
    count = intuition_df["count"].sum()
    intuition_df["count"] =  intuition_df["count"].div(count)
    intuition_df.to_csv("Datasets/intuition_df.csv")


    text = " ".join(list_all_words("S"))
    sensing = Counter(text.split()).most_common(500)
    for word in sensing:
        sensing_dict[word[0]] = [word[1]]
    sensing_df = pd.DataFrame.from_dict(sensing_dict)
    sensing_df = sensing_df.T
    sensing_df.columns = ["count"]
    count = sensing_df["count"].sum()
    sensing_df["count"] =  sensing_df["count"].div(count)
    sensing_df.to_csv("Datasets/sensing_df.csv")

if create_TF_dict == True:
    thinking_dict = {}
    feeling_dict = {}

    data = pd.read_csv("Datasets/TFclassification.csv")

    post_dict = {}
    for i in range(len(data['type'])):
        if data['type'][i] not in post_dict:
            post_dict[data['type'][i]] = [data['posts'][i]]
        else:
            post_dict[data['type'][i]].append(data['posts'][i])


    text = " ".join(list_all_words("T"))
    thinking = Counter(text.split()).most_common(500)
    for word in thinking:
        thinking_dict[word[0]] = [word[1]]
    thinking_df = pd.DataFrame.from_dict(thinking_dict)
    thinking_df = thinking_df.T
    thinking_df.columns = ["count"]
    count = thinking_df["count"].sum()
    thinking_df["count"] =  thinking_df["count"].div(count)
    thinking_df.to_csv("Datasets/thinking_df.csv")


    text = " ".join(list_all_words("F"))
    feeling = Counter(text.split()).most_common(500)
    for word in feeling:
        feeling_dict[word[0]] = [word[1]]
    feeling_df = pd.DataFrame.from_dict(feeling_dict)
    feeling_df = feeling_df.T
    feeling_df.columns = ["count"]
    count = feeling_df["count"].sum()
    feeling_df["count"] =  feeling_df["count"].div(count)
    feeling_df.to_csv("Datasets/feeling_df.csv")

if create_JP_dict == True:
    judging_dict = {}
    perceiving_dict = {}

    data = pd.read_csv("Datasets/JPclassification.csv")

    post_dict = {}
    for i in range(len(data['type'])):
        if data['type'][i] not in post_dict:
            post_dict[data['type'][i]] = [data['posts'][i]]
        else:
            post_dict[data['type'][i]].append(data['posts'][i])


    text = " ".join(list_all_words("J"))
    judging = Counter(text.split()).most_common(500)
    for word in judging:
        judging_dict[word[0]] = [word[1]]
    judging_df = pd.DataFrame.from_dict(judging_dict)
    judging_df = judging_df.T
    judging_df.columns = ["count"]
    count = judging_df["count"].sum()
    judging_df["count"] =  judging_df["count"].div(count)
    judging_df.to_csv("Datasets/judging_df.csv")


    text = " ".join(list_all_words("P"))
    perceiving = Counter(text.split()).most_common(500)
    for word in perceiving:
        perceiving_dict[word[0]] = [word[1]]
    perceiving_df = pd.DataFrame.from_dict(perceiving_dict)
    perceiving_df = perceiving_df.T
    perceiving_df.columns = ["count"]
    count = perceiving_df["count"].sum()
    perceiving_df["count"] =  perceiving_df["count"].div(count)
    perceiving_df.to_csv("Datasets/perceiving_df.csv")