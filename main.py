import curses
from database import opening

def run():
	#initialize terminal
	stdscr = curses.initscr()

	curses.start_color()
	opening.play(stdscr)
	# stdscr.clear()
	# stdscr.addstr("cats")
	# stdscr.refresh()
	curses.endwin()


if __name__ == '__main__':
	run()