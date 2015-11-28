import curses
from questionnode import GameNode

idnums = {0: "opening"}

opening = GameNode(0, "Around you there is only darkness -- darkness extending " 
                            "in every direction , thick as a mattress and heavy as an ending . " 
                            "You can feel its weight on you . \n\n Do you open your eyes ? "
                            "\n\n", {1: "     0 - Yes \n", 2:"     1 - No \n      .  .  .  ?"})