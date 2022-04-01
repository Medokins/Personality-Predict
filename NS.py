import pandas as pd

intuition_dict = pd.read_csv("Datasets/intuition_df.csv")
sensing_dict = pd.read_csv("Datasets/sensing_df.csv")

intuition_dict.columns = ["word", "score"]
sensing_dict.columns = ["word", "score"]

intuition_words = intuition_dict["word"].tolist()
sensing_words = sensing_dict["word"].tolist()

#Intuition post
post_0 = "easily understandable hard topic thank effort problem example especially inxp react fast dodge quick"

#Sensing post
post_1 = "like spring feel energetic season whatever reason also sit outside first thunderstorm relax op want"

#Sensing post
post_2 = "say abusive holy shit sound like si sound like even though relate lol might worth simply list gender"

def evaluate(post, intuition_words, sensing_words, intuition_df, sensing_df):
    intuition_score = 0
    sensing_score = 0
    for word in post.split():
        if word in intuition_words:    
            intuition_score += intuition_df.loc[intuition_df["word"] == word]["score"].tolist()[0]
        if word in sensing_words:
            sensing_score += sensing_df.loc[sensing_df["word"] == word]["score"].tolist()[0]
    

    print("Intuition: ", intuition_score, end = "  |  ")
    print("Sensing: ", sensing_score)

    if intuition_score > sensing_score: return "N"
    else: return "S"

print(evaluate(post_0, intuition_words, sensing_words, intuition_dict, sensing_dict)) #N
print(evaluate(post_1, intuition_words, sensing_words, intuition_dict, sensing_dict)) #S this one is wrong
print(evaluate(post_2, intuition_words, sensing_words, intuition_dict, sensing_dict)) #S


