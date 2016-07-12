import curses


class GameNode(object):
    #game node object, contains text and major behaiours

    def __init__(self, idnum, query, options):
        self.idnum = idnum
        self.query = query
        self.options = options
        self.answer_map = {}

    def text_wrapping(self, word, standardscreen):
        """simple textwrapper, check how much space is left on the x-axis  
        if a word's length is longer than the remaining space, adds a newline"""
        maxx = standardscreen.getmaxyx()[1] - standardscreen.getyx()[1]
        word = " " + word
        if len(word) + 1 > maxx:
            standardscreen.addstr("\n")
        return word
            
    def pretty_printing(self, text, standardscreen):
        """splits text, a string, into a list of strings, checks dicts for them, 
        and changes print colour accordingly"""
        words = text.split(" ")
        for i in words:
            i = self.text_wrapping(i, standardscreen)
            standardscreen.addstr(i[:self.begin_punc_check(i)])
            self.colour_lookup(
                i[self.begin_punc_check(i):self.safe_end_punc(i)[0]],
                standardscreen)
            standardscreen.addstr(i[self.safe_end_punc(i)[1]:])
            # if vocabulary[i.lower()] == "noun":
            #     stdscr.addstr(self.text_wrapping(i), curses.color_pair(2))
            # elif vocabulary[i.lower()] == "adjective":
            #     stdscr.addstr(self.text_wrapping(i), curses.color_pair(3))
            # elif vocabulary[i.lower()] == "verb":
            #     stdscr.addstr(self.text_wrapping(i), curses.color_pair(4))
            # elif vocabulary[i.lower()] == "adverb":
            #     stdscr.addstr(self.text_wrapping(i), curses.color_pair(5))
            # elif vocabulary[i.lower()] == "pronoun":
            #     stdscr.addstr(self.text_wrapping(i), curses.color_pair(6))
            # else:
            # standardscreen.addstr(self.text_wrapping(i, standardscreen))
        standardscreen.refresh()

    def end_punc_check(self, word):
        """check end of word and count punctuation"""
        if word[-1:] in ["'", ".", "!", ":", ";", ")", ",", "("]:
            return self.end_punc_check(word[:-1]) -1
        return 0

    def safe_end_punc(self, word):
        """corrects end_punc_check for weird string slicing behaviour"""
        count = self.end_punc_check(word)
        if count == 0:
            return (None,len(word))
        else:
            return (count,count)

    def begin_punc_check(self, word):
        """check beginning of word and counts punctuation"""
        if word[:1] in ["'", ".", "!", ":", ";", ")", ",", "("]:
            return self.begin_punc_check(word[1:]) +1
        return 0

    def colour_lookup(self, word, standardscreen):
        """not implemented yet - will go against nltk to get word part of 
        speech"""
        standardscreen.addstr(word)

    def play(self, standardscreen):
        """main play function, gets user input and returns next node"""
        standardscreen.clear()
        standardscreen.addstr("\n")
        for i in self.query:
            self.pretty_printing(i, standardscreen)
            standardscreen.addstr("\n\n     ")
        for i in self.options:
            self.pretty_printing(i, standardscreen)
            standardscreen.addstr("\n     ")
        answer = standardscreen.getstr(
            standardscreen.getmaxyx()[0]-2,5).decode(encoding = "utf-8")
        standardscreen.refresh()
        while not answer in self.answer_map:
            answer = standardscreen.getstr(
                standardscreen.getmaxyx()[0]-2,5).decode(encoding = "utf-8")
        else:
            return self.answer_map[answer]

class NoAnswerNode(GameNode):
    def __init__(self, idnum, query):
        self.idnum = idnum
        self.query = query
        self.answer_map = {}

    def play(self, standardscreen):
        """main play function displays text and returns next node"""
        standardscreen.clear()
        standardscreen.addstr("\n")
        for i in self.query:
            self.pretty_printing(i, standardscreen)
            standardscreen.addstr("\n\n     ")
        answer = standardscreen.getch(
            standardscreen.getmaxyx()[0]-2,5)
        standardscreen.refresh()
        return self.answer_map["0"]

class GameEnd(GameNode):
    # def __init__(self, idnum, query):
    #     self.idnum = idnum
    #     self.ERRS = ERRS
    #     self.count = count
    #     self.query = query
    #     self.options = options
    #     self.answer_map = answer_map

    # def play(self, standardscreen):
    #     """main play function displays text and returns next node"""
    #     standardscreen.clear()
    #     standardscreen.addstr("\n")
    #     for i in self.query:
    #         self.pretty_printing(i, standardscreen)
    #         standardscreen.addstr("\n\n     ")
    #     answer = standardscreen.getch(
    #         standardscreen.getmaxyx()[0]-2,5)
    #     standardscreen.refresh()
    #     return self.answer_map["0"]

    pass