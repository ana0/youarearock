import curses
from gamelogiccurses import *


opening_sequence = Sequence("Around you there is only darkness -- darkness extending " 
                            "in every direction , thick as a mattress and heavy as an ending . " 
                            "You can feel its weight on you . \n\n Do you open your eyes ? "
                            "\n\n     0 - Yes \n     1 - No \n      .  .  .  ?", ["Darkness is the absence of light .  I " 
                            "describe what you perceive as darkness because there is no light down here , " 
                            "but you do not see it as black . It is all you've ever known , " 
                            "the only colour .  Indeed , you don\'t really \" see \" at all . "
                            "How are you so sure you have eyes ? \n\n You are a rock .", "Yes , what is there " 
                            "to be curious about , anyway . After all -- you are a rock ."])

yes_thats_right = Sequence("Yes , that's right -- a rock . \n You are just a rock , technically a mineral . " 
                           "You are not somebody's pet rock . You are not cute . You do not have googly eyes . " 
                           "The ridges of your exterior do not resemble a smiley face -- no , not even " 
                           "when I squint . \n\n Do you understand ? \n\n     0 - Yes \n     1 - No \n      .  .  .  ?", ["No you don't .",
                           "Of course you don't ."])

technical_composition = Sequence("You are a granular pegmatite, an igneous rock composed of phaneritic orthorhombic crystals of columbite-tantalite ."
                                  " \n\n Does that make it more clear to you ? \n\n     0 -  .  .  . what ? \n     1 - Those words don't make sense to me \n     2 - I think I'm starting"
                                  " to understand \n     3 - No really , I'm a geologist \n      .  .  .  ?", [" .  .  . that's a respectable , honest response .", 
                                  "They don't make sense to me either , I'm just a computer .", "That's an interesting illusion .", "As a scientist ,"
                                  " you should appreciate better than most the fundamental impossibility of understanding the subjective reality of "
                                  "another being , no matter how many arbitrary symbols we exchange , disguised as language . Do "
                                  "we see the same green ? \n\n "
                                  "Maybe you just wanted to point out that describing you as a pegmatite composed of phaneritic crystals is a little redundant ?"])

pressure = Sequence("The sensation you feel most intensely is heaviness .  Though  .  .  .  is " 
	                        "heaviness the right word ? How do you describe a sensation you've always " 
	                        "lived with ? \n\n What does it feel like to have kidneys ? \n\n    0 - uhh . . .",
	                        ["Pressure . Let's call it pressure \n\n  .  .  .  the pressure of the atmosphere on the body , "
                          "the pressure of the organs as they expand and contract . They are contained by the skin "
                          "-- A membrane in perfect balance ."])

how_does_it_feel = Sequence("Roughly 16,500,000 Pascals envelopes you -- that's 2,393.12 " 
	                         "pounds per square inch , or 162.84 times the pressure of the atmosphere at sea level . "
                           "It has been with you since you crystalized . \n\n Can I " 
	                         "remind you that at one time , you crystalized -- literally ? \n\n How did it feel ?"
	                         " \n\n     0 - Good \n     1 - It hurt \n     2 - I don't remember ", ["Good . Sure . \n\n" 
                           " \" Nice \" -- but hardly comfortable . \n You were rearranging on a molecular level , "
                           "precipitating in the geological version of embryonic fluid . It didn't feel good "
                           "so much as inevitable .", "Of course it hurt . You were rearranging on a molecular level . " 
                           "But it hurt the way getting a bone set , or picking out a splinter hurts -- a pain to pass "
                           "through on your way to order , as what was amorphous becomes regular . ", 
                           "I hear that's normal . I don't remember being born either ."])

how_long = Sequence("So , how long have you been down here ? \n\n     0 - 1.7060976e+16 seconds \n"
                      "     1 - As long as the lifespans of 154,571,428 bees , or 7,213,333 humans \n"
                      "     2 - 25.51 percent of the estimated age of the universe "
                      "\n     3 - Since the end of the Precambrian Eon \n      .  .  .  ?",
                      ["All of these answers are equally true .", "All of these answers are equally true .",
                      "All of these answers are equally true .", "All of these answers are equally true ."])

time_passes = Sequence("For you , time is a body of water in which you float that has no current . \n\n Where do you end and it begin ? "
                        "How do you know you're separate from the rocks around you ? \n\n " 
                        "     0 -  .  .  . uhh , I guess I'm not \n      1 - You addressed me as an individual \n      2 - How am I floating if I'm a rock ? ", 
                        ["No , me neither", "And before that ?", "There's a fine line between metaphor and nonsense -- "
                        "another ambiguous distinction ."])

exterior = Sequence("Feel your fingertips on the keys of your keyboard -- this simple interface . From your nerves ( radial , median , ulnar ) "
                    " up your arms to your synapses , firing . \n\n ( Rock don't have nerves . Rocks don't have synapses . ) \n\n "
                    "There is an entire branch of mathematics dedicated to studying shapes and spaces . There is no way to be sure we're separate . \n\n"
                    " \" Exterior \" : noun . technical . The union of all open sets of a topological space that are disjoint from"
                    " the subset in question . idiomatic . The \" outside \" . The point where I meet you , where self meets object . \n\n "
                    "( I don't mean to call you an object but then again, You are a rock . ) \n\n "
                    "     0 - ( You say nothing .)", ["There is nothing left to say ."])

coltan = Sequence("You are columbite-tantalite . Trade name : coltan . \n\n ", [])

