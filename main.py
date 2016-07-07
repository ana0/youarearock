import curses
import database
import questionnode
import time
import locale




def run(stdscr):
    curses.echo()
    nodes = {i: database.__dict__[i] for i in database.__dict__ if 
            isinstance(database.__dict__[i], questionnode.GameNode)}
    next_node = database.opening.play(stdscr)
    while next_node != "":
	    for node in nodes:
	        if nodes[node].idnum == next_node:
	            next_node = nodes[node].play(stdscr)
    time.sleep(5)

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL,"")
    curses.wrapper(run)
