import curses
# from main import stdscr

class GameNode(object):
	#game node object, contains text and major behaiours

	def __init__(self, idnum, query, options):
		self.id = idnum
		# self.stdscr = stdscr
		self.query = query
		self.options = options

	def text_wrapping(self, text):
        #simple textwrapper, check how much space is left on the x-axis of the screen 
        #if a word's length is longer than the remaining space, adds a newline
		maxx = stdscr.getmaxyx()[1] - stdscr.getyx()[1]
		if text not in [",", "?", ".", ":"]:
		    text = " " + text
		if len(text) + 1 > maxx:
		    stdscr.addstr("\n")
		return text
            
	# def pretty_printing(self, text):
	# 	#splits text, a string, into a list of strings, checks dicts for them, and changes print colour accordingly
	# 	words = text.split(" ")
 #        for i in words:
 #            # if vocabulary[i.lower()] == "noun":
 #            #     stdscr.addstr(self.text_wrapping(i), curses.color_pair(2))
 #            # elif vocabulary[i.lower()] == "adjective":
 #            #     stdscr.addstr(self.text_wrapping(i), curses.color_pair(3))
 #            # elif vocabulary[i.lower()] == "verb":
 #            #     stdscr.addstr(self.text_wrapping(i), curses.color_pair(4))
 #            # elif vocabulary[i.lower()] == "adverb":
 #            #     stdscr.addstr(self.text_wrapping(i), curses.color_pair(5))
 #            # elif vocabulary[i.lower()] == "pronoun":
 #            #     stdscr.addstr(self.text_wrapping(i), curses.color_pair(6))
 #            # else:
	#         stdscr.addstr(self.text_wrapping(i))
 #        stdscr.refresh()

	def play(self, standardscreen):
		standardscreen.clear()
        #self.pretty_printing(self.query)
        standardscreen.addstr(self.query)


#id
#text
#options(0-4)
#linked nodes
