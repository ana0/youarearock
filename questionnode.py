# coding: utf-8

import curses
from parts import everyword
import time
import random


class GameNode(object):
    #game node object, contains text and major behaiours

    def __init__(self, query, options):
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
        standardscreen.refresh()

    def end_punc_check(self, word):
        """check end of word and count punctuation"""
        if word[-1:] in ["'", ".", "!", ":", ";", ")", ",", "(", "?", "-"]:
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
        if word[:1] in ["'", ".", "!", ":", ";", ")", ",", "(", "?" "-"]:
            return self.begin_punc_check(word[1:]) +1
        return 0

    def colour_lookup(self, word, standardscreen):
        """goes against a nltk dictionary to get part of speech and change
        colour accordingly"""
        try:
            part = everyword[word.strip(" ")]
            if part in ["WP", "WRB", "TO", "CC", "EX", "WDT"]:
                standardscreen.addstr(word, curses.color_pair(1))
            if part in ["NN", "NNS", "NNP"]:
                standardscreen.addstr(word, curses.color_pair(2))
            if part in ["JJ", "DT", "JJR", "JJS"]:
                standardscreen.addstr(word, curses.color_pair(3))
            if part in ["VBD", "VBG", "VBZ", "VB", "VBP", "VBN"]:
                standardscreen.addstr(word, curses.color_pair(4))
            if part in ["RB", "RP", "MD"]:
                standardscreen.addstr(word, curses.color_pair(5))
            if part in ["PRP", "IN", "PRP$"]:
                standardscreen.addstr(word, curses.color_pair(6))
            if part in ["LS", "CD", "POS", "$", "-NONE-"]:
                standardscreen.addstr(word)
        except KeyError:
            standardscreen.addstr(word)


    def play(self, standardscreen, wrong):
        """main play function, gets user input and returns next node"""
        answer = self.prompt_input(standardscreen)
        while not answer in self.answer_map:
            wrong.play(standardscreen, wrong)
            answer = self.prompt_input(standardscreen)
        else:
            return self.answer_map[answer].play(standardscreen, wrong)

    def prompt_input(self, standardscreen):
        """prints the query and options using pretty printing methods, and 
        prompts for user input"""
        standardscreen.clear()
        standardscreen.addstr("\n")
        for i in self.query:
            self.pretty_printing(i, standardscreen)
            standardscreen.addstr("\n\n     ")
        for i in self.options:
            self.pretty_printing(i, standardscreen)
            standardscreen.addstr("\n     ")
        standardscreen.addstr(standardscreen.getmaxyx()[0]-2,5,"$ ")
        answer = standardscreen.getstr(
            standardscreen.getmaxyx()[0]-2,7).decode(encoding = "utf-8")
        standardscreen.refresh()
        return answer

class NoAnswerNode(GameNode):
    def __init__(self, query):
        self.query = query
        self.answer_map = {}

    def play(self, standardscreen, wrong):
        """main play function displays text and returns next node"""
        standardscreen.clear()
        standardscreen.addstr("\n")
        for i in self.query:
            self.pretty_printing(i, standardscreen)
            standardscreen.addstr("\n\n     ")
        answer = standardscreen.getch(
            standardscreen.getmaxyx()[0]-2,5)
        standardscreen.refresh()
        return self.answer_map["0"].play(standardscreen, wrong)

class GameEnd(GameNode):
    def play(self, standardscreen, wrong):
        """prints errors if there are any remaining errors, and asks the final
        ending question"""
        while wrong.eternity < 17:
            wrong.play(standardscreen, wrong)
        else:
            answer = self.prompt_input(standardscreen)
            while answer not in ["0", "1"]:
                answer = self.prompt_input(standardscreen)
            else:
                if answer == "0":
                    while True:
                        wrong.play(standardscreen, wrong)
                else:
                    wrong.glitch_out(standardscreen)
                    wrong.spasm(standardscreen)


class WrongAnswerHandler(GameNode):
    def __init__(self, errors, glitch):
        self.errors = errors
        self.glitch = glitch
        self.wrong = 0
        self.eternity = 0

    def play(self, standardscreen, wrong):
        """prints error message if there are any remaining, and if not, prints
        an incrementing counter"""
        if self.wrong < len(self.errors):
            standardscreen.clear()
            standardscreen.addstr("\n ERR: Unidentified Error\n\n",
                curses.color_pair(1))
            self.pretty_printing(self.errors[self.wrong], standardscreen)
            self.wrong += 1
            standardscreen.refresh()
            hang = standardscreen.getch(standardscreen.getmaxyx()[0]-2,5)
        else:
            standardscreen.clear()
            standardscreen.addstr("\n ERR: Unidentified Error\n\n",
                curses.color_pair(1))
            standardscreen.addstr("     " + str(self.eternity))
            self.eternity += 1
            hang = standardscreen.getch(standardscreen.getmaxyx()[0]-2,5)

    def spasm(self, standardscreen):
        """calls recursive loop until throws maximum recursion depth error"""
        standardscreen.clear()
        standardscreen.addstr("\n ERR: Unidentified Error\n\n",
            curses.color_pair(1))
        standardscreen.addstr("     " + str(self.eternity))
        self.eternity += 1
        self.spasm(standardscreen)

    def glitch_out(self, standardscreen):
        standardscreen.clear()
        standardscreen.addstr("\n ERR: Unidentified Error\n\n",
            curses.color_pair(1))
        standardscreen.addstr("     " + str(self.eternity))
        plain = []
        for char in self.glitch:
            plain.append(char)
            if standardscreen.getyx()[1]+1 >= standardscreen.getmaxyx()[1]-5:
                standardscreen.addstr(" \n     ")
            else:
                standardscreen.addstr(char)
        standardscreen.refresh()
        time.sleep(1)
        while len(plain) > 0:
            change = random.choice(plain)
            blue_chars = []
            blue_chars.append(change)
            plain.remove(change)
            standardscreen.clear()
            standardscreen.addstr("\n ERR: Unidentified Error\n\n     ",
                curses.color_pair(1))
            for char in self.glitch:
                if char in plain:
                    if standardscreen.getyx()[1] >= standardscreen.getmaxyx()[1]-5:
                        standardscreen.addstr(" \n     ")
                    else:
                        standardscreen.addstr(char)
                else:
                    if standardscreen.getyx()[1]+1 >= standardscreen.getmaxyx()[1]-5:
                        standardscreen.addstr(" \n     ")
                    else:
                        standardscreen.addstr(char, curses.color_pair(2))
            standardscreen.refresh()
            curses.flash()
        time.sleep(.5)



