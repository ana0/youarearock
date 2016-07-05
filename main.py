

import curses
import database
import questionnode
import time
import locale

def get_node_by_idnum(num):
    pass

nodes = {i: database.__dict__[i] for i in database.__dict__ if 
        isinstance(database.__dict__[i], questionnode.GameNode)}

def run():
    #initialize terminal
    locale.setlocale(locale.LC_ALL,"")
    stdscr = curses.initscr()
    curses.start_color()

    next_node = database.opening.play(stdscr)
    while next_node != "":
	    for node in nodes:
	        if nodes[node].idnum == next_node:
	            next_node = nodes[node].play(stdscr)
    time.sleep(5)

    curses.endwin()

if __name__ == "__main__":
	run()


