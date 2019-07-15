# bad word: "mall"
# sentance: "I went to the mall today"
# output: "I went to the **** today"

# ["shit", "lol", "whoa"]

def censor(badWord, sentance):
    splitty = sentance.split(badWord)
    output = splitty[0]

    for i in range(1, len(splitty)):
        output += (len(badWord) * "*") + splitty[i]

    return output


def censors(badWords, sentance):
    badWords.sort()
    badWords.reverse()

    for bw in badWords:
        sentance = censor(bw, sentance)     

    return sentance
        

print(censors(["hi", "es", "shit"], "hi, hes a shithead"))
# i feel ****ty
# you dumb****
