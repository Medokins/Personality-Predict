import pandas as pd

introverts_dict = pd.read_csv("Datasets/introverts_df.csv")
extroverts_dict = pd.read_csv("Datasets/extroverts_df.csv")

introverts_dict.columns = ["word", "score"]
extroverts_dict.columns = ["word", "score"]

introverts_words = introverts_dict["word"].tolist()
extroverts_words = extroverts_dict["word"].tolist()

#this is Introvert post
post_0 = "good conflict prefer good civil argument sometimes civility inappropriate circumstance case like often call asshole fine thing\
        good asshole handle language allow put people really like manipulate people counter argument say something dumb asshole may time bystander\
        usually entertain like say continuous function think probably issue remember age usually think one year young actually take long realize\
        old best friend year since like almost see daughter point get jealous get depress see someone something attribute relationship usually\
        overwhelm sadness despair think mostly right consider volunteer charity work invest thrill slow conversion find god start take religion\
        seriously year old cannot save world make impact world immediately surround make difference mean exclusive club well stress dream last"

#this is Introvert post
post_1 = "know intj tool use interaction people excuse antisocial truly enlighten mastermind know would count pet peeze something time matter\
        people either whether group people mall never see best friend sit outside conversation jsut listen want interject sit formulate say wait\
        inject argument thought find fascinate sit watch people talk people fascinate sit class watch different people find intrigue dad intj\
        u stand look like line safeway watch people home talk people like think military job people voluntarily go job important show deference\
        endanger live glorify way civilian think pretty ignorant general think military necessary defense mechanism political tactic feel like u\
        specifically invest much money could put money education whatnot though personally sound budget aernative really comment one way base two\
        politician eye year ago come name somewhat important kinda role model nowadays pick keep score individual level mean little vary accord\
        number condition day may score high others low sweat really good cast physiotherapist like fiberglass cast break arm whatever sometimes\
        want take picture beast put someone arm sadly people blind brilliance need tell directly wave arm frantically totally beyond oblivious\
        get good eye contact help lot start find like attention get opposite sex notice however gay men tend little aggressive always walk away"

#this is Extrovert post
post_2 = "mbti uncanny valley astrology change format make palatable keep internal consistency difficu especially stigma already associate tl\
        r math something point economics predictable even best model map communicate experience something quality remember mbti theoretical model\
        subject change good information present even good mbti generalize intend act like rule thumb set hard fast rule anyway quite finish post\
        figure good start get ready work may may finish late fuck hate college sooo prolly different finish two week though yay yes maybe focus\
        self improvement join club something kinda treat like game try go class little possible efficient possible fill life new experience new\
        situation much possible travel try new thing get job go party know people whatever hell stuff use entpness come thing get internship actual\
        company help lot use leadership skill really like get motivate maybe indeed dovie andi se tovya sagain also minato arisato persona together\
        epic character know keep repeat nail grave start support union co ops thing nature work within exist system move right direction think tpp\
        hit lot intellectual property asset etc money represent labor creative intellectual productivity contract consuant takeover employee dominant\
        market work set guideline pay per project task etc possibly point system charity type work basic income gaurenteed minimum income negative income\
        also implement earn income credit also profit share investment rental income never would even think agree sure perhaps think lack empathy way teach\
        make feel stupid agree hehe think people make sooo many assumption forget teach explain bit take grant people general really good abstract idea\
        thing tell word assign know word mean thus leave dust interrupt people ask explain say seem work decently maybe entp thing advice go straight\
        forward ask meredith say seek harmonize selfishly like want conflict people argue care much two question sure mean clarify intp like flair say"

def evaluate(post, extroverts_words, introverts_words, extrovert_df, introvert_df):
    extrovert_score = 0
    introvert_score = 0
    for word in post.split():
        if word in extroverts_words:
            extrovert_score += extrovert_df.loc[extrovert_df["word"] == word]["score"].tolist()[0]
        if word in introverts_words:    
            introvert_score += introvert_df.loc[introvert_df["word"] == word]["score"].tolist()[0]

    print("Extrovert: ", extrovert_score, end = "  |  ")
    print("Introvert: ", introvert_score)

    if extrovert_score > introvert_score: return "E"
    else: return "I"

print(evaluate(post_0, extroverts_words, introverts_words, extroverts_dict, introverts_dict)) #I
print(evaluate(post_1, extroverts_words, introverts_words, extroverts_dict, introverts_dict)) #I
print(evaluate(post_2, extroverts_words, introverts_words, extroverts_dict, introverts_dict)) #E