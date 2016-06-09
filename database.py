import curses
from questionnode import GameNode

idnums = {0: "opening", }

opening = GameNode(0, ["Around you there is only darkness -- darkness extending" 
    " in every direction , thick as a mattress and heavy as an ending . You can"
    " feel its weight on you .", "Do you open your eyes ? "],
    ["0 - Yes", "1 - No", ".  .  .  ?"], 
    {"0":1, "1":2, "yes":1, "no":2, "y":1, "n":2})

one = NoAnswerNode(1, ["Darkness is the absence of light . I describe what you "
    "perceive as darkness because there is no light down here , but you do not "
    "see it as black . It is all you've ever known , the only colour .  Indeed "
    ", you don't really ' see ' at all .", "How are you so sure you have "
    "eyes ?"],
    {"0":8})

two = GameNode(2, ["Hmm .", "Why not ?"], 
    ["0 - I'm asleep", "1 - I'm dreaming", "2 - I'm obstinate .", "3 - I'm not "
    "curious .", "4 - I . . . don't know .", ".  .  .  ?"], 
    {"0":4, "1":5, "2":6, "3":3, "4":7})

three = NoAnswerNode(3, ["How strange .", "You can't be human . "
    "You must be a rock ."],
    {"0":8})

four = NoAnswerNode(4, ["Asleep like a foot ?\nAsleep like a computer monitor"
    " ?", "You are not asleep ."],
    {"0":8})

five = GameNode(5, ["What are you dreaming about ?"],
    ["0 - The past .", "1 - The future .", "2 - I don't remember ."], 
    {"0":, "1":, "2":})

six = GameNode(6, ["No you're not .", "You are a rock ."]
    ["0 - uh, ok", "1 - ( Let me teach you something about being obstinate )"],
    {"0":8, "1":7})

NUMBERS = GameNode(7, [], [], {})

eight = GameNode(8, ["Yes , that's right -- a rock .", "You are just a rock ,"
    " technically a mineral . You are not somebody's pet rock . You are not "
    "cute . You do not have googly eyes . The ridges of your exterior do not "
    "resemble a smiley face -- no , not even when I squint .", "Do you "
    "understand ?"], 
    ["0 - Yes", "1 - No", "2 - I don't want to be a rock"], 
    {"0":, "1":, "2",})

