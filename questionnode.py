import curses

# stdscr = curses.initscr()
# curses.start_color()

class GameNode(object):
	#game node object, contains text and major behaiours

	def __init__(self, idnum, query, options):
		self.idnum = idnum
		# self.stdscr = stdscr
		self.query = query
		self.options = options

	def initialize_term(self):
		if self.idnum == 0:
			stdscr = curses.initscr()
			curses.start_color()
			opening.play()

	def text_wrapping(self, text, standardscreen):
        #simple textwrapper, check how much space is left on the x-axis of the screen 
        #if a word's length is longer than the remaining space, adds a newline
		maxx = standardscreen.getmaxyx()[1] - standardscreen.getyx()[1]
		if text not in [",", "?", ".", ":"]:
		    text = " " + text
		if len(text) + 1 > maxx:
		    standardscreen.addstr("\n")
		return text
            
	def pretty_printing(self, text, standardscreen):
		#splits text, a string, into a list of strings, checks dicts for them, and changes print colour accordingly
		words = text.split(" ")
		for i in words:
			# if vocabulary[i.lower()] == "noun":
			#     stdscr.addstr(self.text_wrapping(i), curses.color_pair(2))
			# elif vocabulary[i.lower()] == "adjective":
			#     stdscr.addstr(self.text_wrapping(i), curses.color_pair(3))
			# elif vocabulary[i.lower()] == "verb":
			#     stdscr.addstr(self.text_wrapping(i), curses.color_pair(4))
			# elif vocabulary[i.lower()] == "adverb":
			#     stdscr.addstr(self.text_wrapping(i), curses.color_pair(5))
			# elif vocabulary[i.lower()] == "pronoun":
			#     stdscr.addstr(self.text_wrapping(i), curses.color_pair(6))
			# else:
			standardscreen.addstr(self.text_wrapping(i, standardscreen))
		standardscreen.refresh()

	def play(self):
		if self.idnum == 0:
			stdscr = curses.initscr()
			curses.start_color()
			# return stdscr
		stdscr.clear()
		self.pretty_printing(self.query, stdscr)
		# stdscr.addstr("cats")
		stdscr.refresh()



#id
#text
#options(0-4)
#linked nodes
