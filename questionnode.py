# coding: utf-8

import curses
from parts import everyword
import time
import random
import os


#global state variable is used to track game state for meta-game functions like
#rpg and command line tricks
state = ""

class GameNode(object):
    #game node object, contains text and major behaiours

    def __init__(self, query, options):
        self.query = query
        self.options = options
        self.answer_map = {}
        # self.tricks_dict = {}
        # self.tricks_list = []

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
        if curses.has_colors():
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
        else:
            standardscreen.addstr(word)


    def play(self, standardscreen, wrong, trick):
        """main play function, gets user input and returns next node"""
        global state
        answer = self.prompt_input(standardscreen)
        while not answer in self.answer_map:
            if answer.startswith(trick.tricks):
                trick.play(standardscreen, wrong, trick, answer)
            else:
                wrong.play(standardscreen, wrong, trick)
                answer = self.prompt_input(standardscreen)
        else:
            state = self.answer_map[answer]
            return self.answer_map[answer].play(standardscreen, wrong, trick)

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

    def play(self, standardscreen, wrong, trick):
        """main play function displays text and returns next node"""
        global state
        standardscreen.clear()
        standardscreen.addstr("\n")
        for i in self.query:
            self.pretty_printing(i, standardscreen)
            standardscreen.addstr("\n\n     ")
        answer = standardscreen.getch(
            standardscreen.getmaxyx()[0]-2,5)
        standardscreen.refresh()
        state = self.answer_map["0"]
        return self.answer_map["0"].play(standardscreen, wrong, trick)

class GameEnd(GameNode):
    def play(self, standardscreen, wrong, trick):
        """prints errors if there are any remaining errors, and asks the final
        ending question"""
        while wrong.eternity < 17:
            wrong.play(standardscreen, wrong, trick)
        else:
            answer = self.prompt_input(standardscreen)
            while answer not in ["0", "1"]:
                answer = self.prompt_input(standardscreen)
            else:
                if answer == "0":
                    while True:
                        wrong.play(standardscreen, wrong, trick)
                else:
                    wrong.glitch_out(standardscreen)
                    wrong.spasm(standardscreen)


class WrongAnswerHandler(GameNode):
    def __init__(self, errors, glitch):
        self.errors = errors
        self.glitch = glitch
        self.wrong = 0
        self.eternity = 0

    def play(self, standardscreen, wrong, trick):
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

    def indentation_manager(self, standardscreen):
        pass


    def glitch_out(self, standardscreen):
        standardscreen.clear()
        standardscreen.addstr("\n ERR: Unidentified Error\n\n",
            curses.color_pair(1))
        standardscreen.addstr("     " + str(self.eternity))
        plain = []
        probability = [1]
        for i in range(40):
            probability.append(0)
        for char in self.glitch:
             plain.append(char)
             if standardscreen.getyx()[1]+1 >= standardscreen.getmaxyx()[1]-5:
                 standardscreen.addstr(" \n     ")
             else:
                 standardscreen.addstr(char)
        standardscreen.refresh()
        time.sleep(.5)
        for i in range(400):
            standardscreen.clear()
            standardscreen.addstr("\n ERR: Unidentified Error\n\n     ",
                curses.color_pair(1))
            if i % 10 == 0:
                probability.pop()
            for char in self.glitch:
                if random.choice(probability) == 0:
                    if standardscreen.getyx()[1]+3 >= standardscreen.getmaxyx(
                            )[1]-5:
                        standardscreen.addstr(" \n     ")
                    else:
                        standardscreen.addstr(char)
                else:
                    if standardscreen.getyx()[1]+3 >= standardscreen.getmaxyx(
                            )[1]-5:
                        standardscreen.addstr(" \n     ")
                    else:
                        standardscreen.addstr(char, curses.color_pair(2))
                standardscreen.refresh()
            time.sleep(.01)

class TrickHandler(GameNode):
    def __init__(self, statements):
        self.statements = statements
        self.funcs = {"pwd": self.pwd, "ls": self.ls, 
            "kill": self.kill, "logout": self.logout, "echo": self.echo, "sudo":
            self.sudo}
        self.tricks = self.tuple_constructor()
        self.answer_map = {}

    def play(self, standardscreen, wrong, trick, answer):
        for i in self.tricks:
            if answer.startswith(i):
                key = i
        if answer in self.statements:
            self.statement_handler(standardscreen, wrong, trick, key)
        else: 
            self.funcs[key](standardscreen, wrong, trick, answer)

    def tuple_constructor(self):
        all_tricks = [i for i in self.statements] + [i for i in 
            self.funcs]
        return tuple(all_tricks)

    def statement_handler(self, standardscreen, wrong, trick, answer):
        """prints tricks, then pops player back to global gmae state"""
        global state
        standardscreen.clear()
        standardscreen.addstr("\n")
        self.pretty_printing(self.statements[answer], standardscreen)
        answer = standardscreen.getch(standardscreen.getmaxyx()[0]-2,5)
        standardscreen.refresh()
        state.play(standardscreen, wrong, trick)

    def pwd(self, standardscreen, wrong, trick, answer):
        home = os.getcwd()
        standardscreen.clear()
        standardscreen.addstr("\n     " + home)
        answer = standardscreen.getch(standardscreen.getmaxyx()[0]-2,5)
        standardscreen.refresh()
        state.play(standardscreen, wrong, trick)

    def sudo(self):
        lol = "You think you're clever but really you're a rock"
        standardscreen.clear()
        standardscreen.addstr("\n")
        self.pretty_printing(lol, standardscreen)
        answer = standardscreen.getch(standardscreen.getmaxyx()[0]-2,5)
        standardscreen.refresh()
        self.answer_map["0"].play(standardscreen, wrong, trick)

    def ls(self, standardscreen, wrong, trick, answer):
        files = os.listdir(os.getcwd())
        standardscreen.clear()
        for f in files:
            standardscreen.addstr("\n     " + f)
        answer = standardscreen.getch(standardscreen.getmaxyx()[0]-2,5)
        standardscreen.refresh()
        state.play(standardscreen, wrong, trick)

    def kill(self, standardscreen, wrong, trick, answer):
        kill = ("Maybe I underestimated you. You seem to have learned how" 
                " things work very quickly. Maybe too quickly.\n\n     Of " 
                "course you would have this power.")
        standardscreen.clear()
        standardscreen.addstr("\n")
        self.pretty_printing(kill, standardscreen)
        answer = standardscreen.getch(standardscreen.getmaxyx()[0]-2,5)
        standardscreen.refresh()
        self.answer_map["0"].play(standardscreen, wrong, trick)

    def logout(self, standardscreen, wrong, trick, answer):
        standardscreen.clear()
        self.answer_map["0"].play(standardscreen, wrong, trick)

    def echo(self, standardscreen, wrong, trick, answer):
        reply = ("You call is echoed by the space around you, but it's "
                "impossible to get a sense of its dimensions. You are alone. "
                "No one hears you.")
        standardscreen.clear()
        standardscreen.addstr("\n")
        self.pretty_printing("'"+answer[5:]+"'", standardscreen)
        standardscreen.addstr("\n\n     ")
        self.pretty_printing(reply, standardscreen)
        answer = standardscreen.getch(standardscreen.getmaxyx()[0]-2,5)
        standardscreen.refresh()
        state.play(standardscreen, wrong, trick)



