import curses
from gamelogiccurses import *
from gamedata import *
from gamedict import *

opening_sequence.game_play()
yes_thats_right.game_play()
technical_composition.game_play()
pressure.game_play()
how_does_it_feel.game_play()
how_long.game_play()
time_passes.game_play()
# exterior.game_play()
# curses.flash()

curses.echo()
curses.curs_set(True)
curses.endwin()

