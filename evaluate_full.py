import pandas as pd
from IE import evaluate_IE
from NS import evaluate_NS
from TF import evaluate_TF
from JP import evaluate_JP

def evaluate_full_personality(post):
    full_personality = []
    #IE
    introverts_dict = pd.read_csv("Datasets/introverts_df.csv")
    introverts_dict.columns = ["word", "score"]
    introverts_words = introverts_dict["word"].tolist()
    extroverts_dict = pd.read_csv("Datasets/extroverts_df.csv")
    extroverts_dict.columns = ["word", "score"]
    extroverts_words = extroverts_dict["word"].tolist()
    full_personality.append(evaluate_IE(post, extroverts_words, introverts_words, extroverts_dict, introverts_dict))

    #NS
    intuition_dict = pd.read_csv("Datasets/intuition_df.csv")
    intuition_dict.columns = ["word", "score"]
    intuition_words = intuition_dict["word"].tolist()
    sensing_dict = pd.read_csv("Datasets/sensing_df.csv")
    sensing_dict.columns = ["word", "score"]
    sensing_words = sensing_dict["word"].tolist()
    full_personality.append(evaluate_NS(post, intuition_words, sensing_words, intuition_dict, sensing_dict))

    #TF
    thinking_dict = pd.read_csv("Datasets/thinking_df.csv")
    thinking_dict.columns = ["word", "score"]
    thinking_words = thinking_dict["word"].tolist()
    feeling_dict = pd.read_csv("Datasets/feeling_df.csv")
    feeling_dict.columns = ["word", "score"]
    feeling_words = feeling_dict["word"].tolist()
    full_personality.append(evaluate_TF(post, thinking_words, feeling_words, thinking_dict, feeling_dict))

    #JP
    judging_dict = pd.read_csv("Datasets/judging_df.csv")
    judging_dict.columns = ["word", "score"]
    judging_words = judging_dict["word"].tolist()
    perceiving_dict = pd.read_csv("Datasets/perceiving_df.csv")
    perceiving_dict.columns = ["word", "score"]
    perceiving_words = perceiving_dict["word"].tolist()
    full_personality.append(evaluate_JP(post, perceiving_words, judging_words, perceiving_dict, judging_dict))

    return "".join(str(x) for x in full_personality)