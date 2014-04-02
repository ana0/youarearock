from gamelogic import *

opening_sequence = TwoAnswers("Around you there is only darkness -- darkness extending " +
                            "in every direction, thick as a mattress and heavy as an ending. " +
                            "You can feel its weight on you.\n Do you open your eyes?\n " +
                            "    1 - Yes\n     2 - No", "Darkness is the absence of light.  I " +                            "describe what you perceive as darkness because there is no light down here, " \
                            "but you do not see it as black.\nIt is all you've ever known, " +
                            "the only colour.  Indeed, you don\'t really \"see\" at all.\n" +
                            "How are you so sure you have eyes?\nYou are a rock.", "Yes, what is there " +
                            "to be curious about, anyway.\nAfter all -- you are a rock.", "", "", "")

opening_sequence.game_play()
