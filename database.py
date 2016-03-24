import curses
from questionnode import GameNode

idnums = {0: "opening", }

opening = GameNode(0, ["Around you there is only darkness -- darkness extending " 
                            "in every direction , thick as a mattress and heavy as an ending . " 
                            "You can feel its weight on you .","Do you open your eyes ? "],
                            ["0 - Yes","1 - No",".  .  .  ?"], {"0":1,"1":2,"yes":1,"no":2,"y":1,"n":2})

one = GameNode(1, ["test"],["0 - Yes","1 - No",".  .  .  ?"], {"0":1,"1":2,"yes":1,"no":2,"y":1,"n":2})

two = GameNode(2, ["test"],["0 - Yes","1 - No",".  .  .  ?"], {"0":1,"1":2,"yes":1,"no":2,"y":1,"n":2})