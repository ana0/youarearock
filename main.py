import curses
from database import opening
import questionnode
import time

def run():
	#initialize terminal
	opening.play()
	time.sleep(2)
	# stdscr.clear()
	# stdscr.addstr("cats")
	# stdscr.refresh()
	curses.endwin()


if __name__ == '__main__':
	run()