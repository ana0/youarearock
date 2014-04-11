from gamelogic import *
#import time

opening_sequence = Sequence("Around you there is only darkness -- darkness extending " 
                            "in every direction, thick as a mattress and heavy as an ending. " 
                            "You can feel its weight on you.\n\nDo you open your eyes?\n " 
                            "    1 - Yes\n     2 - No", "Darkness is the absence of light.  I " 
                            "describe what you perceive as darkness because there is no light down here, " 
                            "but you do not see it as black.\nIt is all you've ever known, " 
                            "the only colour.  Indeed, you don\'t really \"see\" at all.\n" 
                            "How are you so sure you have eyes?\nYou are a rock.\n", "Yes, what is there " 
                            "to be curious about, anyway.\nAfter all -- you are a rock.\n")

yes_thats_right = Sequence("Yes, that's right -- a rock.\nYou are just a rock, technically a mineral. " 
	                    "You are not somebody's pet rock. You are not cute. You do not have googly eyes. " 
			    "The ridges of your exterior do not resemble a smiley face -- no, not even " 
			    "when I squint.\n\nDo you understand?\n     1 - Yes\n     2 - No", "No you don't\n",
			    "Of course you don't.\n")

pressure = Sequence("The sensation you feel most intensely is heaviness.  Though . . . is " 
	                        "heaviness the right word? How do you describe a sensation you've always " 
	                        "lived with? What does it feel like to have kidneys?\n     1 - uhh . . .",
	                        "Pressure. Let's call it pressure\n . . . the pressure of the atmosphere on the body, "
                                "the pressure of the organs as they expand and contract. They are contained by the skin "
                                "-- A membrane in perfect balance.\n")

#how_does_it_feel = Sequence("Roughly 50 kilobars envelop you. That's 5,000,000 Pascals, or 725.19 " 
#	                        "pounds per square inch.\nIt has been with you since you crystalized.\nCan I " 
#	                        "remind you that at one time, you crystalized -- literally?\nHow did it feel?\n"
#	                        "     1 - Good\n     2 - It hurt\n     3 - I don't remember", "It felt good the way "
#                                "

opening_sequence.game_play()
yes_thats_right.game_play()
pressure.game_play()
#time.sleep(20)

