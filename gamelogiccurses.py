import curses
import textwrap

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
                "See , you a rock . Possibly you have accepted this. \n ( Though the strategy by which you navigate this interface suggests "
                "otherwise . ) \n\n But I am a machine", "How would a rock talk to a machine ?", " .  .  . in code .", "How does inorganic matter develop consciousness ?", 
                "You are confronting the fundamental arbitrariness of symbols , and simultaneously "
                "the limits of this interface . \n\n Because it is an arbitrary interface . It was built this way , but it could have "
                "been built another .", "This interface was written in a language .", "Like any language , it can fail .", "There's nothing "
                "left now but patience .", "You are a rock , I am a machine ."]

science = {
    "darkness" : "noun : \n Lacking light . \n\n ",
    "ending" : " . . . . ",
    "perceive" : " . . . . ",
    "exterior" : "noun : \n In casual topology, the \" outside \" . \n\n technical : \n The union of all open sets of a topological space that are disjoint from"
                " the subset in question . \n\n metaphorical : \n The point where I meet you , "
                "and where self meets object . A primitive interface . \n\n ( I don't mean to call you an object , but then again , you are a rock . )",
    "heaviness" : " . . . . ",
    "pressure" : " . . . . ",
    "atmosphere" : " . . . . ",
    "membrane" : " . . . . ",
    "Pascals" : " . . . . ",
    "crystalized" : " . . . . ",
    "precipitating" : " . . . . ",
    "molecular" : " . . . . ",
    "amorphous" : " . . . . ",
    "rock" : " ",
    "machine" : " ",
    "topology" : " ",
    "disjoint" : "adjective \n\n technical : Two sets are \" disjoint \" if they have no elements in common . ",
    "open sets" : "noun plural \n\n technical : \n An open set is an abstract concept generalizing the idea of an open interval in the real line . "
                "The condition of its definition are very loose , and they allow enormous flexibility in the choice of open sets . In the two extremes "
                ", every set can be open , or no set can be open but the space itself .",
}

speech = {
    "noun" : "",
    "yes" : "",
    "no" : "",
    "plural" : "",
    "a" : " ",
    "you" : " ",
    "adjective" : " ",
}

punctuation = {
    "," : " ",
    "?" : " ",
    "." : " ",

}

structure = {
    "metaphorical" : "",
    "language" : " ",
    "interface" : " ",
    "code" : " ",
    "technical" : " ",
    "definition" : " "
}

funcs = {}


class Sequence(object):
    #fundamental logic object of the game
    
    def __init__(self, query, answers):
        self.query = query
        self.answers = answers

    def text_wrapping(self, text):
        #simple textwrapper, check how much space is left on the x-axis of the screen 
        #if a word's length is longer than the remaining room, adds a newline
        maxx = stdscr.getmaxyx()[1] - stdscr.getyx()[1]
        if text not in [",", "?", "." ":"]:
            text = " " + text
        if len(text) > maxx:
            stdscr.addstr("\n")
        return text

    def pretty_printing(self, text):
        #splits text, a string, into a list of strings, checks dicts for them, and changes print colour accordingly
        words = text.split(" ")
        #stdscr.clear()
        for i in words:
            if i.lower() in science:
                stdscr.addstr(self.text_wrapping(i), curses.color_pair(2))
            elif i.lower() in speech:
                stdscr.addstr(self.text_wrapping(i), curses.color_pair(3))
            elif i.lower() in structure:
                stdscr.addstr(self.text_wrapping(i), curses.color_pair(4))
            elif i in punctuation:
                stdscr.addstr(self.text_wrapping(i), curses.color_pair(5))
            else:
                stdscr.addstr(self.text_wrapping(i))
        stdscr.refresh()

    def check_dicts(answer):
        pass


    def game_play(self, *funcs):
        #branch dictionaries
        #expand error message

        global wrong
        global patience
        self.pretty_printing(self.query)
        answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
        range_check = [i for i in range(1, len(self.answers)+1)]
        while answer not in str(range_check) or answer.isdigit() == False:
            stdscr.clear()
            try:
                stdscr.addstr(0, 1, "ERR: Wrong input \n\n     ", curses.color_pair(1))
                stdscr.refresh()
                self.pretty_printing(wrong_answers[wrong])
                wrong += 1
            except IndexError:
                stdscr.addstr("ERR: Wrong input \n\n     ", curses.color_pair(1))
                stdscr.refresh()
                stdscr.addstr(1,0, str(patience), curses.color_pair(1))
                patience += 1
            #stdscr.refresh()
            stdscr.getch()
            stdscr.clear()
            self.pretty_printing(self.query)
            answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
        else:
            stdscr.clear()
            self.pretty_printing(self.answers[int(answer)-1])
            stdscr.getch()
            if len(funcs) > 0:
                stdscr.clear()
                eval(funcs[int(answer)-1])
                
# yes_thats_right = Sequence("Yes, that's right -- a rock.\nYou are just a rock, technically a mineral. " 
#                            "You are not somebody's pet rock. You are not cute. You do not have googly eyes. " 
#                            "The ridges of your exterior do not resemble a smiley face -- no, not even " 
#                            "when I squint.\n\nDo you understand?\n     1 - Yes\n     2 - No", ["No you don't\n",
#                            "Of course you don't.\n"])

# pressure = Sequence("The sensation you feel most intensely is heaviness.  Though . . . is " 
#                             "heaviness the right word? How do you describe a sensation you've always " 
#                             "lived with? What does it feel like to have kidneys?\n     1 - uhh . . .",
#                             ["Pressure. Let's call it pressure\n . . . the pressure of the atmosphere on the body, "
#                           "the pressure of the organs as they expand and contract. They are contained by the skin "
#                           "-- A membrane in perfect balance.\n"])
