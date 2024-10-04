from random import choice, randint
from data import data

score = 0 

while True:
    first_celebrity = choice(data)
    second_celebrity = choice(data)
    
    if first_celebrity == second_celebrity:
        second_celebrity = choice(data)

    print(f'Compare A: {first_celebrity["name"]} a {first_celebrity["description"]}, from {first_celebrity["country"]}')
    print(f'Compare B: {second_celebrity["name"]} a {second_celebrity["description"]}, from {second_celebrity["country"]}')

    max_followers = max(first_celebrity["follower_count"], second_celebrity["follower_count"])
        
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if (user_guess == "a" and max_followers == first_celebrity["follower_count"]) or \
       (user_guess == "b" and max_followers == second_celebrity["follower_count"]):
        score += 1
        print(f'You\'re right! Current score: {score}')
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
