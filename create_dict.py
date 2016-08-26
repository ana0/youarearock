import database
import nltk.data
import questionnode

nodes = {i: database.__dict__[i] for i in database.__dict__ if 
        isinstance(database.__dict__[i], questionnode.GameNode)}

everyword_list = []

for node in nodes:
    try:
        for i in nodes[node].query:
            try:
                corpus = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(corpus)
                everyword_list.append(tagged)
            except UnicodeDecodeError:
                pass
    except AttributeError:
        pass
    try:
        for i in nodes[node].options:
            try:
                corpus = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(corpus)
                everyword_list.append(tagged)
            except UnicodeDecodeError:
                pass
    except AttributeError:
        pass
    # try:
    #     for i in nodes[node].options:
    #         try:
    #             corpus = nltk.word_tokenize(i)
    #             tagged = nltk.pos_tag(corpus)
    #             everyword_list.append(tagged)
    #         except UnicodeDecodeError:
    #             pass
    # except AttributeError:
    #     pass

# print everyword_list

f = open("parts.txt", "r+")

everyword_dict = {}

for sentence in everyword_list:
    for i in sentence:
        everyword_dict[i[0]] = i[1]
    # f.write()

print everyword_dict

f.write(str(everyword_dict))
f.close()

