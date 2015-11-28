import nltk.data
import gamelogiccurses
import gamedata


def listmaker(text):
    # words = text.split(" ")
    everyword = [everyword.append() for w in text.split(" ")]
    return everyword

# print(len(everyword))

def dictmaker(everyword):
	pass


# print(gamedata.opening_sequence.return_answers())

# print(gamedata.opening_sequence.get_all_words())

all_modules = [gamedata.opening_sequence,
gamedata.yes_thats_right,
gamedata.technical_composition,
gamedata.pressure,
gamedata.how_does_it_feel,
gamedata.how_long,
gamedata.time_passes,
gamedata.exterior,
gamedata.coltan]

main = [i.get_all_words() for i in all_modules]

def text_collector(text):
	ok = ""
	for t in text:
		ok = ok + " " + t
	return ok

trying = text_collector(gamelogiccurses.wrong_answers) + text_collector(main)

corpus = nltk.word_tokenize("You are a granular pegmatite, an igneous rock composed of phaneritic orthorhombic crystals of stone .")
tagged = nltk.pos_tag(corpus)

print("\n\n")
print(tagged)


#main = [main.append(i) for i in gamelogiccurses.wrong_answers]

#print(main)