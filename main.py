import curses
from database import *
import questionnode
import time
import locale


def run(stdscr):
    curses.echo()
    next_node = opening.play(stdscr, wrong)
    while next_node != "":
        next_node = next_node.play(stdscr, wrong)
    time.sleep(5)

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL,"")
    curses.wrapper(run)
