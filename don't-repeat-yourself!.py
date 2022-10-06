# First of all we need to create two empty string variables, one for the whole story and one for the last word.
# This is important, because repeating the last word will end the story for our user.
story = ""
last = ""

# We'll prompt our user for a word inside of a while loop to keep on getting word as long as user don't break the rule (or call the 'end' of it).
while True:
    word = input("Please type in a word: ")

    # If the user type 'end', the story will end.
    if word == "end":
        break
    # If the user repeats themself, it will end as well.
    elif word == last:
        break
    # If the user respect the rules, they can express.
    else:
        last = word
        story += word + " "

# Once the story is all over, the user will be able to see their masterpiece all together.    
print(words)
