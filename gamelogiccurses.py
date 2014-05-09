import curses

stdscr = curses.initscr()
curses.start_color()
curses.noecho()

class Sequence(object):
    
    def __init__(self, query, *answers):
        self.query = query
        self.answers = answers

    def game_play(self):
        stdscr.addstr(1, 0, self.query)
        stdscr.refresh()
        tries = 0
        as_list = list(self.answers)
        answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
        range_check = [i for i in range(1, len(as_list)+1)]
        while tries <= 2:
            if answer in str(range_check):
                stdscr.clear()
                stdscr.addstr(1, 0, as_list[int(answer)-1])
                stdscr.refresh()
                break
            else:
                stdscr.clear()
                stdscr.addstr(1, 0, as_list[int(answer)-1])print("You speak to me like I can understand you. Try again\n . . . ?")
                stdscr.refresh()
                tries += 1
                answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
        else:
            while answer not in str(range_check):
                stdscr.clear()
                stdscr.addstr(1, 0, as_list[int(answer)-1])print("You speak to me like I can understand you. Try again\n . . . ?")
                stdscr.refresh()
                tries += 1
                answer = stdscr.getstr(0, 0).decode(encoding = "utf-8")
            else:
                stdscr.clear()
                stdscr.addstr(1, 0, as_list[int(answer)-1])
                stdscr.refresh()
                    