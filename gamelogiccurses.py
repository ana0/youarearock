import curses
import textwrap

stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.curs_set(False)

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

wrong = 0
patience = 1

wrong_answers = [["You speak to me like I can understand you."], ["Consider that your assumptions are wrong: we don't speak the same "
                "language."], [" . . . "], ["Are you doing this to be obstinate?"], ["Imagine what language sounds like to a rock"], 
                ["See, you a rock. Possibly you have accepted this.", "(Though the strategy by which you navigate this interface suggests "
                "otherwise.)", " ", "But I am a machine"], ["How would a rock talk to a machine?"], [" . . . in code."], ["How would inorganic "
                "matter develop consciousness?"], ["You are confronting the fundamental arbitrariness of symbols, and simultaneously "
                "the limits of this interface.", " ", "Because it is an arbitrary interface. It was built this way, but it could have "
                "been built another."], ["This interface was written in a language."], ["Like any language, it can fail."], ["There's nothing "
                "left now but patience."], ["You are a rock, I am a machine."]]

vocabulary = {
    "darkness" : " . . . . ",
    "ending" : " . . . . ",
    "perceive" : " . . . . ",
    "exterior" : " . . . . ",
    "heaviness" : " . . . . ",
    "pressure" : " . . . . ",
    "atmosphere" : " . . . . ",
    "membrane" : " . . . . ",
    "Pascals" : " . . . . ",
    "crystalized" : " . . . . ",
    "precipitating" : " . . . . ",
    "molecular" : " . . . . ",
    "amorphous" : " . . . . ",
}

class Sequence(object):
    
    def __init__(self, query, answers):
        self.query = query
        self.answers = answers

    def text_wrapping(self, text):
        maxx = stdscr.getmaxyx()[1] - stdscr.getyx()[1]
        if len(text) > maxx:
            stdscr.addstr("\n")
        return text

    def game_play(self, *funcs):
        global wrong
        global patience
        #NEXT implement punctuation exceptions
        for i in self.query:
            if i in vocabulary:
                stdscr.addstr(self.text_wrapping(i) + " ", curses.color_pair(1))
            elif i == " ":
                stdscr.addstr("\n")
            else:
                stdscr.addstr(self.text_wrapping(i) + " ")
        stdscr.refresh()
        answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
        range_check = [i for i in range(1, len(self.answers)+1)]
        while answer not in str(range_check) or answer.isdigit() == False:
            stdscr.clear()
            try:
                stdscr.addstr(1, 0, self.text_wrapping(wrong_answers[wrong]), curses.color_pair(1))
                wrong += 1
            except IndexError:
                stdscr.addstr(1,0, str(patience), curses.color_pair(1))
                patience += 1
            stdscr.refresh()
            stdscr.getch()
            stdscr.clear()
            stdscr.addstr(1, 0, self.text_wrapping(self.query))
            stdscr.refresh()
            answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
        else:
            stdscr.clear()
            stdscr.addstr(1, 0, self.text_wrapping(self.answers[int(answer)-1]))
            stdscr.refresh()
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
