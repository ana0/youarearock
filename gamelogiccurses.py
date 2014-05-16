import curses

stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.curs_set(False)

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

wrong = 0
patience = 1

wrong_answers = ["You speak to me like I can understand you.", "Consider that your assumptions are wrong: we don't speak the same "
                "language.", " . . . ", "Are you doing this to be obstinate?", "Imagine what language sounds like to a rock", "See, "
                "you a rock. Possibly you have accepted this.\n(Though the strategy by which you navigate this interface suggests "
                "otherwise.)\n\nBut I am a machine", "How would a rock talk to a machine?", " . . . in code.", "How would inorganic "
                "matter develop consciousness?", "You are confronting the fundamental arbitrariness of symbols, and simultaneously "
                "the limits of this interface.\n\nBecause it is an arbitrary interface. It was built this way, but it could have "
                "been built another.", "This interface was written in a language.", "Like any language, it can fail.", "There's nothing "
                "left now but patience.", "You are a rock, I am a machine."]

class Sequence(object):
    
    def __init__(self, query, answers):
        self.query = query
        self.answers = answers

    def game_play(self, *funcs):
        global wrong
        global patience
        stdscr.addstr(1, 0, self.query)
        stdscr.refresh()
        answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
        range_check = [i for i in range(1, len(self.answers)+1)]
        while answer not in str(range_check) or answer.isdigit() == False:
            stdscr.clear()
            try:
                stdscr.addstr(1, 0, wrong_answers[wrong], curses.color_pair(1))
                wrong += 1
            except IndexError:
                stdscr.addstr(1,0, str(patience), curses.color_pair(1))
                patience += 1
            stdscr.refresh()
            stdscr.getch()
            stdscr.clear()
            stdscr.addstr(1, 0, self.query)
            stdscr.refresh()
            answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
        else:
            stdscr.clear()
            stdscr.addstr(1, 0, self.answers[int(answer)-1])
            stdscr.refresh()
            stdscr.getch()
            if len(funcs) > 0:
                stdscr.clear()
                eval(funcs[int(answer)-1])
                

        
