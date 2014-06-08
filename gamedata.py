import curses
from gamelogiccurses import *


opening_sequence = Sequence("Around you there is only darkness -- darkness extending " 
                            "in every direction , thick as a mattress and heavy as an ending . " 
                            "You can feel its weight on you . \n\n Do you open your eyes ? "
                            "\n\n     1 - Yes \n     2 - No \n      .  .  .  ?", ["Darkness is the absence of light .  I " 
                            "describe what you perceive as darkness because there is no light down here , " 
                            "but you do not see it as black . It is all you've ever known , " 
                            "the only colour .  Indeed , you don\'t really \" see \" at all . "
                            "How are you so sure you have eyes ? \n\n You are a rock .", "Yes , what is there " 
                            "to be curious about , anyway . After all -- you are a rock ."])

yes_thats_right = Sequence("Yes , that's right -- a rock . \n You are just a rock , technically a mineral . " 
                           "You are not somebody's pet rock . You are not cute . You do not have googly eyes . " 
                           "The ridges of your exterior do not resemble a smiley face -- no , not even " 
                           "when I squint . \n\n Do you understand ? \n\n     1 - Yes \n     2 - No \n      .  .  .  ?", ["No you don't .",
                           "Of course you don't ."])

technical_composition = Sequence("You are a granular pegmatite, an igneous rock composed of phaneritic orthorhombic crystals of columbite-tantalite ."
                                  " \n\n     1 -  .  .  . what ? \n     2 - Those words don't make sense to me \n     3 - I think I'm starting"
                                  " to understand \n     4 - No really , I'm a geologist \n      .  .  .  ?", [" .  .  . that's a respectable , honest response .", 
                                  "They don't make sense to me either , I'm just a computer .", "That's an interesting illusion .", "As a scientist ,"
                                  " you should appreciate better than most the fundamental impossibility of understanding the subjective reality of "
                                  "another being . \n  .  .  . no matter how many arbitrary symbols we exchange , disguised as language . \n\n "
                                  "Maybe you just wanted to point of that describing you as a pegmatite composed of phaneritic crystals is a little redundant ?"])

pressure = Sequence("The sensation you feel most intensely is heaviness .  Though  .  .  .  is " 
	                        "heaviness the right word ? How do you describe a sensation you've always " 
	                        "lived with ? \n\n What does it feel like to have kidneys ? \n\n    1 - uhh . . .",
	                        ["Pressure. Let's call it pressure \n\n  .  .  .  the pressure of the atmosphere on the body , "
                          "the pressure of the organs as they expand and contract . They are contained by the skin "
                          "-- A membrane in perfect balance ."])

how_does_it_feel = Sequence("Roughly 16,500,000 Pascals envelopes you -- that's 2,393.12 " 
	                         "pounds per square inch , or 162.84 times the pressure of the atmosphere at sea level . "
                           "It has been with you since you crystalized . \n\n Can I " 
	                         "remind you that at one time , you crystalized -- literally ? \n\n How did it feel ?"
	                         " \n\n     1 - Good \n     2 - It hurt \n     3 - I don't remember ", ["Good . Sure . \n" 
                           " \" Nice \" -- but hardly comfortable . \n You were rearranging on a molecular level , "
                           "precipitating in the geological version of embryonic fluid . It didn't feel good "
                           "so much as inevitable .", "Of course it hurt . You were rearranging on a molecular level . " 
                           "But it hurt the way getting a bone set , or picking out a splinter hurts -- a pain to pass "
                           "through on your way to order , as what was amorphous becomes regular . ", 
                           "I hear that's normal . I don't remember being born either ."])

how_long = Sequence("So , how long have you been down here ? \n\n     1 - 1.7060976e+16 seconds \n"
                      "     2 - As long as the lifespans of 154,571,428 bees, or 7,213,333 humans \n"
                      "     3 - 25.51 percent of the estimated age of the universe "
                      "\n     4 - Since the end of the Precambrian Eon \n      .  .  .  ?",
                      ["All of these answers are equally true.", "All of these answers are equally true.",
                      "All of these answers are equally true.", "All of these answers are equally true."])
