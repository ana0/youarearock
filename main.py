import curses
from database import *
import questionnode
import time
import locale

questionnode.state = opening
questionnode.tricks_dict = tricks
questionnode.tricks_list = [trick for trick in questionnode.tricks_dict]
questionnode.tricks_list = tuple(questionnode.tricks_list)


def run(stdscr):
    curses.echo()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    next_node = questionnode.state.play(stdscr, wrong)

    time.sleep(5)

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL,"")
    curses.wrapper(run)
