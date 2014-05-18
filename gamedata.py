import curses
from gamelogiccurses import *

# vocabulary = {
#     "darkness" : " . . . . ";
#     "ending" :
#     "perceive"
#     "exterior"
#     "heaviness"
#     "pressure"
#     "atmosphere"
#     "membrane"
#     "Pascals"
#     "crystalized"
#     "precipitating"
#     "molecular"
#     "amorphous"
#     ""
#}


opening_sequence = Sequence(["Around you there is only darkness -- darkness extending " 
                            "in every direction, thick as a mattress and heavy as an ending. " 
                            "You can feel its weight on you.", " ", "Do you open your eyes?" ,
                            "    1 - Yes", "    2 - No", "    . . . ?"], [["Darkness is the absence of light.  I " 
                            "describe what you perceive as darkness because there is no light down here, " 
                            "but you do not see it as black. It is all you've ever known, " 
                            "the only colour.  Indeed, you don\'t really \"see\" at all.", " ",
                            "How are you so sure you have eyes?", "You are a rock."], ["Yes, what is there " 
                            "to be curious about, anyway.", "After all -- you are a rock."]])

yes_thats_right = Sequence(["Yes, that's right -- a rock.", "You are just a rock, technically a mineral. " 
                           "You are not somebody's pet rock. You are not cute. You do not have googly eyes. " 
                           "The ridges of your exterior do not resemble a smiley face -- no, not even " 
                           "when I squint.", " ", "Do you understand?", "    1 - Yes", "    2 - No"], [["No you don't"],
                           ["Of course you don't."]])

pressure = Sequence(["The sensation you feel most intensely is heaviness.  Though . . . is " 
	                        "heaviness the right word? How do you describe a sensation you've always " 
	                        "lived with?", " ", "What does it feel like to have kidneys?", "    1 - uhh . . ."],
	                        [["Pressure. Let's call it pressure", " . . . the pressure of the atmosphere on the body, "
                          "the pressure of the organs as they expand and contract. They are contained by the skin "
                          "-- A membrane in perfect balance."]])

how_does_it_feel = Sequence(["Roughly 50 kilobars envelop you. That's 5,000,000 Pascals, or 725.19 " 
	                         "pounds per square inch. It has been with you since you crystalized.", "Can I " 
	                         "remind you that at one time, you crystalized -- literally?", " ", "How did it feel?",
	                         "    1 - Good", "    2 - It hurt", "    3 - I don't remember"], [["Good. Sure.", 
                           "\"Nice\" -- but hardly comfortable.", "You were rearranging on a molecular level, "
                           "precipitating in the geological version of embryonic fluid. It didn't feel good "
                           "so much as inevitable."], ["Of course it hurt. You were rearranging on a molecular level.", 
                           "But it hurt the way getting a bone set, or picking out a splinter hurts -- a pain to pass "
                           "through on your way to order, as what was amorphous becomes regular.", "Do planets pant on their way "
                           "around the sun?"], ["I hear that's normal. I don't remember being born either."]])