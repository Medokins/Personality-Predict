import pandas as pd

thinking_dict = pd.read_csv("Datasets/thinking_df.csv")
feeling_dict = pd.read_csv("Datasets/feeling_df.csv")

thinking_dict.columns = ["word", "score"]
feeling_dict.columns = ["word", "score"]

thinking_words = thinking_dict["word"].tolist()
feeling_words = feeling_dict["word"].tolist()

#Thinking post
post_0 = "sure ego check except immature intjs painfully slow developmentally potential chart know sure whether ego legitimate would caution put every intj"

#Feeling post
post_1 = "uncontrollable emotion conquer believe also commonly say type help grind people let go fear get ready dive depth mind trust friend help pull back problem solve interest kind sad journey"

#Thinking post
post_2 = "content thread see similarity say focus wrong part statement case ask end evil ask powerful point would cross mind tear entire city thus harm"

def evaluate(post, thinking_words, feeling_words, thinking_df, feeling_df):
    thinking_score = 0
    feeling_score = 0
    for word in post.split():
        if word in thinking_words:    
            thinking_score += thinking_df.loc[thinking_df["word"] == word]["score"].tolist()[0]
        if word in feeling_words:
            feeling_score += feeling_df.loc[feeling_df["word"] == word]["score"].tolist()[0]
    

    print("Thinking: ", thinking_score, end = "  |  ")
    print("Feeling: ", feeling_score)

    if thinking_score > feeling_score: return "T"
    else: return "F"

print(evaluate(post_0, thinking_words, feeling_words, thinking_dict, feeling_dict)) #T
print(evaluate(post_1, thinking_words, feeling_words, thinking_dict, feeling_dict)) #F
print(evaluate(post_2, thinking_words, feeling_words, thinking_dict, feeling_dict)) #T

