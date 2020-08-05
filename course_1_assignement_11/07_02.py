wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []

for i in wrds:
    i = i + "ed"
    past_wrds.append(i)

print(past_wrds)

# For each string in wrds, add ‘ed’ 
# to the end of the word (to make the word past tense). 
# Save these past tense words to a list called past_wrds.