from evaluate_full import evaluate_full_personality

post = "" #Paste Your post in here

if len(post) == 0: print("You didn't paste in Your post!")
else:
    personality_type = evaluate_full_personality(post)
    print(f"Your personality type is {personality_type}")
