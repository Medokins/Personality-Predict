import pandas as pd
data = pd.read_csv("Datasets/MBTI 500.csv")

IE = False
NS = False
TF = False
JP = False

if IE == True:
    def classify(x):
        if "I" in x:
            return "I"
        else:
            return "E"

    data['type'] = data["type"].apply(classify)
    data.to_csv("Datasets/IEclassification.csv")

if NS == True:
    def classify(x):
        if "N" in x:
            return "N"
        else:
            return "s"

    data['type'] = data["type"].apply(classify)
    data.to_csv("Datasets/NSclassification.csv")

if TF == True:
    def classify(x):
        if "T" in x:
            return "T"
        else:
            return "F"

    data['type'] = data["type"].apply(classify)
    data.to_csv("Datasets/TFclassification.csv")

if JP == True:
    def classify(x):
        if "J" in x:
            return "J"
        else:
            return "P"

    data['type'] = data["type"].apply(classify)
    data.to_csv("Datasets/JPclassification.csv")