import curses
from gamelogiccurses import *
from gamedata import *

opening_sequence.game_play()
yes_thats_right.game_play()
pressure.game_play()
how_does_it_feel.game_play()


curses.echo()
curses.curs_set(True)
curses.endwin()
