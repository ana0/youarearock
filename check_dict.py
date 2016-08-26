from parts import everyword

parts_of_speech = []
handled = ["WDT", "JJS", "MD", "JJR", "VBN", "WRB", "EX", "CC", "PRP$", "TO", "NNP", "DT", "RP", "WP", "NN", "NNS", "JJ", "VB", "RB", "PRP", "IN", "VBD", "VBG", "VBZ", "VBP"]
not_handled = []

for word in everyword:
    if everyword[word] not in parts_of_speech:
        parts_of_speech.append(everyword[word])

for word in parts_of_speech:
    if word not in handled:
        not_handled.append(word)

for word in everyword:
    if everyword[word] in not_handled:
        print word, everyword[word]