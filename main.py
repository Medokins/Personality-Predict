from evaluate_full import evaluate_full_personality
from modifyData import prepare_post

post = "" #Paste Your post in here
post = prepare_post(post)

if len(post) == 0: print("You didn't paste in Your post!")
else:
    personality_type = evaluate_full_personality(post)
    print(f"Your personality type is {personality_type}")
