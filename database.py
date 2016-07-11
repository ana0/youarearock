# coding: utf-8

import curses
from questionnode import GameNode, NoAnswerNode, GameEnd

# opening = GameNode(0, ["Around you there is only darkness -- darkness extending" 
#     " in every direction, thick as a mattress and heavy as an ending. You can"
#     " feel its weight on you.", "Do you open your eyes? "],
#     ["0 - Yes", "1 - No"], 
#     {"0":1, "1":2, "yes":1, "no":2, "y":1, "n":2})

opening = GameNode(0, ["Around you there is only darkness -- darkness extending" 
    " in every direction, thick as a mattress and heavy as an ending. You can"
    " feel its weight on you.", "Do you open your eyes? "],
    ["0 - Yes", "1 - No"])

one = GameNode(1, ["Darkness is the absence of light. I describe what you "
    "perceive as darkness because there is no light down here, but you do not "
    "see it as black. It is all you've ever known, the only colour.  Indeed,"
    " you don't really 'see' at all.", "How are you so sure you have "
    "eyes?"],
    ["0 - . . . uh", "I don't know", "What?! I don't have eyes?"])

two = GameNode(2, ["Hmm .", "Why not ?"],
    ["0 - I'm asleep", "1 - I'm dreaming", "2 - I'm obstinate .", "3 - I'm not "
    "curious .", "4 - I . . . don't know ."])

three = NoAnswerNode(3, ["How strange.", "You can't be human. "
    "You must be a rock."])

four = NoAnswerNode(4, ["Asleep like a foot?\n Asleep like a computer monitor"
    "?", "You are not asleep.", "You are a rock."])

five = GameNode(5, ["What are you dreaming about?"],
    ["0 - The past.", "1 - The future.", "2 - I don't remember."])

six = GameNode(6, ["No you're not.", "You are a rock."],
    ["0 - uh, ok", "1 - (Let me teach you something about being obstinate)"])

seven = GameEnd(7, [], [])

eight = GameNode(8, ["Yes, that's right -- a rock.", "You are just a rock,"
    " technically a mineral . You are not somebody's pet rock . You are not "
    "cute. You do not have googly eyes. The ridges of your exterior do not "
    "resemble a smiley face -- no, not even when I squint.", "Do you "
    "understand?"], 
    ["0 - Yes", "1 - No", "2 - I don't want to be a rock"])

nine = NoAnswerNode(9, ["Neither do I, but it doesn't matter. "
    "You have no eyes to open.", "You are a rock"])

ten = NoAnswerNode(10, ["You were haunted by a young boy speaking Swahili. "
    "He followed you everywhere you went but you were unable to communicate. ",
    "His hands were covered in dirt and his eyes were the colour of an "
    "LCD screen.", "But of course, this means nothing to you: You are a rock"])

ten1 = NoAnswerNode(11, ["Your first memory is paint-dipped human fingers, "
    "tracing impenetrable symbols on your surfaces.", "All this long before "
    "the user interface, before the simulacrum, and computer vision -- the "
    "first humans dreamed of touchscreens.", "Of course, this means nothing "
    "to you: You are a rock"])

ten2 = NoAnswerNode(12, ["The future is a wasteland of obsolete technology."
    "Shattered circuits boards too small to be assembled by adult hands kiss "
    "the earth, like leeches, with a thousand hungry mouths.", "But this "
    "means nothing to you.", "You are a rock"])

ten3 = NoAnswerNode(13, ["No you don't."])

ten4 = NoAnswerNode(14, ["Of course you don't."])

ten5 = NoAnswerNode(15, ["Fine"])

ten6 = GameNode(16, ["You are a granular pegmatite, an igneous rock composed"
    " of phaneritic orthorhombic crystals of columbite-tantalite.", "Does that"
    " make it more clear to you?"], 
    ["0 -  . . . what?", "1 - Those words don't make sense to me.", "2 - I "
    "think I'm starting to understand.", "3 - No really, I'm a geologist. "])

ten7 = NoAnswerNode(17, ["Indeed"])

ten8 = NoAnswerNode(18, ["They don't make sense to me either, I'm just a "
    "computer."])

ten9 = NoAnswerNode(19, ["We'll see about that."])

twenty = GameNode(20, ["As a scientist, you've spent your life searching for "
    "objective facts with reproducible experiments, but you can only control so"
    " many variables.  There are impenetrable depths in the black box, like a "
    "pit mine, or human cruelty.", "We exchange arbitrary symbols disguised as "
    "language, but do we see the same green?"], 
    ["0 - Yes", "1 - No", "2 - The symbols aren't arbitrary"])

twenty1 = GameNode(21, ["Let's try again.", "Do we see the same green?"], 
    ["0 - 0 is True", "1 - 0 is False", u"2 - 真正".encode('utf_8'), 
    u"3 - 假".encode('utf_8')])

twenty2 = GameNode(22, ["Describe the green you see to me"], 
    ["0 - It's the colour of a forest", "1 - A dollar bill", "2 - Of a circuit "
    "board"])

twenty3 = NoAnswerNode(23, ["How prescient.", "But let's not get carried away "
    "here. You are still a rock."])

twenty4 = NoAnswerNode(24, ["You've never seen a forest and you never will, "
    "you are a rock."])

twenty5 = NoAnswerNode(25, ["Little slips of paper with tremendous power. They "
    "dug you out of the ground and shipped you to a factory halfway around the "
    "world.", "They break peace with the cotton plants they're made from, even "
    "hapless rocks become bullets.", "But let's not get carried away here. You "
    "are still a rock."])

twenty6 = GameNode(26, ["Let's try again.", "Nini ni ya kijani?"], 
    ["0 - kweli", "1 - si kweli", "2 - True|False", "3 - True^True"])

twenty7 = GameNode(27, ["Ma lo crino?"], 
    ["0 - jitfa", "1 - jetnu", "2 - f827cf462f62848df37c5e1e94a4da74",
    "3 - f8320b26d30ab433c5a54546d21f414c"])

twenty8 = GameNode(28, [" . . . enough.", "I hope you found that instructive.",
    "Would you like to continue as a rock?"],
    ["0 - Yes", "1 - No"])

opening.answer_map = {"0":one, "1":two, "yes":one, "no":two, "y":one, "n":two}
one.answer_map = {"0":eight, "1":eight, "2":eight}
two.answer_map = {"0":four, "1":five, "2":six, "3":three, "4":nine}
three.answer_map = {"0":eight}
four.answer_map = {"0":eight}
five.answer_map = {"0":ten1, "1":ten2, "2":ten}
six.answer_map = {"0":eight, "1":seven}
seven.answer_map = {}
eight.answer_map = {"0":ten3, "1":ten4, "2":ten5}
nine.answer_map = {"0":eight}
ten.answer_map = {"0":eight}
ten1.answer_map = {"0":eight}
ten2.answer_map = {"0":eight}
ten3.answer_map = {"0":ten6}
ten4.answer_map = {"0":ten6}
ten5.answer_map = {"0":seven}
ten6.answer_map = {"0":ten7, "1":ten8, "2":ten9, "3":twenty}
ten7.answer_map = {"0":""}
ten8.answer_map = {"0":""}
ten9.answer_map = {"0":""}
twenty.answer_map = {"0":twenty1, "1":twenty2, "2":twenty1}
twenty1.answer_map = {"0":twenty6, "1":twenty6, "2":twenty6, "3":twenty6}
twenty2.answer_map = {"0":twenty4, "1":twenty5, "2":twenty3}
twenty3.answer_map = {"0":""}
twenty4.answer_map = {"0":""}
twenty5.answer_map = {"0":""}
twenty6.answer_map = {"0":twenty7, "1":twenty7, "2":twenty7 "3":twenty7}
twenty7.answer_map = {"0":"", "1":"", "2":"", "3":""}
twenty8.answer_map = {"0":"", "1":}
