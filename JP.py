import pandas as pd

judging_dict = pd.read_csv("Datasets/judging_df.csv")
perceiving_dict = pd.read_csv("Datasets/perceiving_df.csv")

judging_dict.columns = ["word", "score"]
perceiving_dict.columns = ["word", "score"]

judging_words = judging_dict["word"].tolist()
perceiving_words = perceiving_dict["word"].tolist()

#Juding post
post_0 = "know intj tool use interaction people excuse antisocial truly enlighten mastermind know would count pet peeze something time\
        matter people either whether group people mall never see best friend sit outside conversation jsut listen want interject sit\
        formulate say wait inject argument thought find fascinate sit watch people talk people fascinate sit class watch different\
        people find intrigue dad intj u stand look like line safeway watch people home talk people like think military job people\
        voluntarily go job important show deference endanger live glorify way civilian think pretty ignorant general think military\
        necessary defense mechanism political tactic feel like u specifically invest much money could put money education whatnot\
        though personally sound budget aernative really comment one way base two politician eye year ago come name somewhat important\
        kinda role model nowadays pick keep score individual level mean little vary accord number condition day may score high others low sweat\
        really good cast physiotherapist like fiberglass cast break arm whatever sometimes want take picture beast put someone arm sadly people"

#Perceiving post
post_1 = "good start say look make deep run year trade would improve team considerably expect resign franson next year plus keep mention\
        phil introvert like miss leg something really bad tavares introvert case realize would start introduce tell u one fun fact human\
        intelligence consider endless course would really complicate technical rig probably coworker super friendly ask time know intent\
        good man hate ask totally stop ask dick essentially ask stop say hi try clarify thought sound like try control manner one say hello\
        would potentially even bad answer usually force good instead depth analysis life would appropriate give question say someone close ask\
        totally relatively open tend talk much people tell sometimes smart intelligent maybe way speak mannerism something give away seem like lot\
        people meet resent like go way make people feel stupid assume think good somehow believe think probably happy could relate wish would stop\
        pas judgement even know act make seem stupid think add clarification difference role polr function go use beebe model well socionics provide"

#Perceiving post
post_2 = "fulfil cheat good situation pretend everythings great side note ton people use work google work le recognizable entity name alphabet\
        umbrella anyway like waymo verily surprise prestige work big tech name steadily drop next year favor work shadow company ut also mind get\
        stock option big company part compensation blame abstract potential possibility something earn right regret chase fancy tech career bay area never\
        get big fat payday point seem follow logic without xyz long get giant compensation giant compensation uncertain reward forgo xyz certain loss obviously\
        nature delay gratification key maximize delay gratification carefully weigh odds miss spend prime life something satisfy ura risky gamble incredibly rare\
        weah necessarily say kind sound like might turn fine continue rent room save money least year market crash great critical outcome perceive necessary make\
        lifestyle worth outcome measurably likely thing want see side next decade besides fat bank account amass via frugality lifestyle still worth bad happen\
        want kid need big house expensive car want life long relationship someone willingness forgo luxury car big house bay area exactly profound evidence humble\
        attainable desire get far define need stuff consider important let work relationship actively try meet people wait hop right person come along latter true urge revisit\
        lifelong relationship one specific thing actually know want forgo act seek one abstract possibility good job good city good look strange make say nah good wait get serious"

def evaluate_JP(post, perceiving_words, judging_words, perceiving_df, judging_df):
    perceiving_score = 0
    judging_score = 0
    for word in post.split():
        if word in perceiving_words:    
            perceiving_score += perceiving_df.loc[perceiving_df["word"] == word]["score"].tolist()[0]
        if word in judging_words:
            judging_score += judging_df.loc[judging_df["word"] == word]["score"].tolist()[0]
    

    print("Perceiving: ", perceiving_score, end = "  |  ")
    print("Judging: ", judging_score)

    if perceiving_score > judging_score: return "P"
    else: return "J"

# print(evaluate_JP(post_0, perceiving_words, judging_words, perceiving_dict, judging_dict)) #J
# print(evaluate_JP(post_1, perceiving_words, judging_words, perceiving_dict, judging_dict)) #P
# print(evaluate_JP(post_2, perceiving_words, judging_words, perceiving_dict, judging_dict)) #P  this one it gets wrong