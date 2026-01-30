"""
Death saves are a little different than normal saving throws. If your 
health drops to 0 or below, you are unconscious and may die. Each time
it is your turn, roll a d20 to determine if you get closer to life
or fall deeper into death. If the number is less than 10, you record 
a "failure". If the number is 10 or greater, you record a "success". 
If you record three "failures", you die. If you record three "successes", 
you are "stable" but unconscious. If you are unlucky and roll a "one",
it counts as two failures. If you are lucky and roll a 20, you gain 1
"health" and have revived. Write a program that simulates death saves. 
What is the probability that one dies, stabilizes, or revives?
""" 
import random

def death_save(): 
    successes = 0 
    failures = 0

    while successes < 3 and failures < 3: 
        roll = random.randint(1, 20)

        if roll == 1: 
            failures += 2 
        elif roll < 10: 
            failures += 1 
        elif roll < 20: 
            successes += 1
        else: 
            return 'revived'

    if failures >= 3: 
        return 'died'
    else: 
        return 'stable'


trials = 5000
results = {'died': 0, 'stable': 0, 'revived': 0}

for i in range(trials): 
    outcome = death_save()
    results[outcome] += 1 
    if i % 1000 == 0: 
        print(i)

for k in results: 
    print(f"{k}: {results[k] / trials:.3f}")




