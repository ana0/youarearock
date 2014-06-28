import curses
from gamedict import *


stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.curs_set(False)

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)

wrong = 0
patience = 1


wrong_answers = ["You speak to me like I can understand you .", "Consider that your assumptions are wrong : we don't speak the same "
                "language .", " .  .  . ", "Are you doing this to be obstinate ?", "Imagine what language sounds like to a rock", 
                "See , you are a rock . Possibly you have accepted this . \n ( Though the strategy by which you navigate this interface suggests "
                "otherwise . ) \n\n But I am a machine .", "How would a rock talk to a machine ?", " .  .  . in code ?",  
                "You are confronting the fundamental arbitrariness of symbols , and simultaneously "
                "the limits of this interface . \n\n Because it is an arbitrary interface ." , "It was built this way , but it could have "
                "been built another .", "This interface was written in a language .", "Like any language , it can fail .", "Are you sure these words you're"
                " using mean anything at all ?", "There's nothing left now but patience .", "You are a rock , I am a machine . \n\n  .  .  . not as different"
                " as you'd think ."]

class Sequence(object):
    #fundamental logic object of the game
    
    def __init__(self, query, answers):
        self.query = query
        self.answers = answers

    def text_wrapping(self, text):
        #simple textwrapper, check how much space is left on the x-axis of the screen 
        #if a word's length is longer than the remaining space, adds a newline
        maxx = stdscr.getmaxyx()[1] - stdscr.getyx()[1]
        if text not in [",", "?", ".", ":"]:
            text = " " + text
        if len(text) + 1 > maxx:
            stdscr.addstr("\n")
        return text

    def pretty_printing(self, text):
        #splits text, a string, into a list of strings, checks dicts for them, and changes print colour accordingly
        words = text.split(" ")
        for i in words:
            if vocabulary[i.lower()] == "noun":
                stdscr.addstr(self.text_wrapping(i), curses.color_pair(2))
            elif vocabulary[i.lower()] == "adjective":
                stdscr.addstr(self.text_wrapping(i), curses.color_pair(3))
            elif vocabulary[i.lower()] == "verb":
                stdscr.addstr(self.text_wrapping(i), curses.color_pair(4))
            elif vocabulary[i.lower()] == "adverb":
                stdscr.addstr(self.text_wrapping(i), curses.color_pair(5))
            elif vocabulary[i.lower()] == "pronoun":
                stdscr.addstr(self.text_wrapping(i), curses.color_pair(6))
            else:
                stdscr.addstr(self.text_wrapping(i))
        stdscr.refresh()

    def game_play(self, *funcs):
        #fundamental gameplay method, checks answer (int) against a list index to print the 
        #corresponding statement, also iterates through a list of possible wrong answers stored above as global variables
        global wrong
        global patience
        stdscr.clear()
        self.pretty_printing(self.query)
        answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
        range_check = [i for i in range(len(self.answers))]
        while answer not in str(range_check) or answer.isdigit() == False:
            try:
                stdscr.clear()
                stdscr.addstr(0, 1, "ERR: Wrong input \n\n", curses.color_pair(1))
                stdscr.refresh()
                self.pretty_printing(wrong_answers[wrong])
                wrong += 1
            except IndexError:
                stdscr.clear()
                stdscr.addstr(0, 1, "ERR: Wrong input \n\n", curses.color_pair(1))
                stdscr.refresh()
                stdscr.addstr(1,0, "\n " + str(patience), curses.color_pair(1))
                patience += 1
            stdscr.getch()
            stdscr.clear()
            self.pretty_printing(self.query)
            answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
        else:
            stdscr.clear()
            self.pretty_printing(self.answers[int(answer)])
            stdscr.getch()
            if len(funcs) > 0:
                stdscr.clear()
                eval(funcs[int(answer)])

    def game_end(self):
        global wrong
        global patience
        while True:
            try:
                stdscr.clear()
                stdscr.addstr(0, 1, "ERR: Wrong input \n\n", curses.color_pair(1))
                stdscr.refresh()
                self.pretty_printing(wrong_answers[wrong])
                wrong += 1
            except IndexError:
                stdscr.clear()
                stdscr.addstr(0, 1, "ERR: Wrong input \n\n", curses.color_pair(1))
                stdscr.refresh()
                stdscr.addstr(1,0, "\n " + str(patience), curses.color_pair(1))
                patience += 1
            answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
