import curses
from database import opening, one, two
import questionnode
import time

def get_node_by_idnum(num):
	pass

nodes = [opening, one, two]

def run():
	#initialize terminal
	stdscr = curses.initscr()
	curses.start_color()

	next_node = opening.play(stdscr)
	for node in nodes:
		if node.idnum == next_node:
			node.play(stdscr)
	time.sleep(5)

	curses.endwin()


if __name__ == '__main__':
	run()



