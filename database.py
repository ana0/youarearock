# coding: utf-8

import curses
from questionnode import GameNode, NoAnswerNode, GameEnd, WrongAnswerHandler

wrong = WrongAnswerHandler(["You speak to me like I can understand you.", "Consider that "
                "your assumptions are wrong: we don't speak the same language.",
                " .  .  . ", "Imagine what language sounds like to a rock", 
                " .  .  . ", "How would a rock talk to a machine?", " .  .  . "
                "in code ?", "You have reached the limits of this interface. "
                "\n\n Because it is an arbitrary interface." , "It was built "
                "this way, but it could have been built another.", 
                "It was written in a language. \n\n Like any "
                "language, it can fail.", "Are you sure these words you're"
                " using mean anything at all?", "Who is more patient? \n\n You "
                "are a rock, I am a machine."], 0)

opening = GameNode(0, ["Around you there is only darkness -- darkness extending" 
    " in every direction, thick as a mattress and heavy as an ending. You can"
    " feel its weight on you.", "Do you open your eyes? "],
    ["0 - Yes", "1 - No"])

one = GameNode(1, ["Darkness is the absence of light. I describe what you "
    "perceive as darkness because there is no light down here, but you do not "
    "see it as black. It is all you've ever known, the only colour.  Indeed,"
    " you don't really 'see' at all.", "How are you so sure you have "
    "eyes?"],
    ["0 - . . . uh", "1 - I don't know", "2 - What?! I don't have eyes?"])

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

twenty9 = GameNode(29, ["The sensation you feel most intensely is heaviness."
    " Though  .  .  .  is heaviness the right word? How do you describe a "
    "sensation you've always lived with?", "What does it feel like to have "
    "kidneys ? "],
    ["0 - . . . uhh", "1 - I never thought about it", "2 - It's painful"])

thirty = NoAnswerNode(30, ["Maybe you should."])

thirty1 = NoAnswerNode(31, ["Yes, pain is universal."])

thirty2 = NoAnswerNode(32, ["Pressure. Let's call it pressure", ".  .  .  the "
    "pressure of the atmosphere on the body, the pressure of the organs as they"
    " expand and contract. They are contained by the skin -- A membrane in "
    "perfect balance."])

thirty3 = GameNode(33, ["Roughly 16,500,000 Pascals envelopes you -- that's "
    "2,393.12 pounds per square inch, or 162.84 times the pressure of the "
    "atmosphere at sea level. It has been with you since you crystalized.", 
    "Can I remind you that at one time, you crystalized -- literally?", "How "
    "did it feel?"],
    ["0 - It felt good", "1 - It hurt", "2 - I don't remember"])

thirty4 = GameNode(34, ["Of course it hurt. You were rearranging on a "
    "molecular level.", "How much did it hurt?"],
    ["0 - It's not so bad", "1 - The worst pain I've ever felt", 
    "2 - I don't have words to describe it"])

thirty5 = NoAnswerNode(35, ["Good. Sure.", "'Nice' -- but hardly comfortable.",
    "You were rearranging on a molecular level, precipitating in the geological"
    " version of embryonic fluid. It didn't feel good so much as inevitable.", 
    "It also felt hot. Over time, you will become very good at resisting "
    "heat."])

thirty6 = NoAnswerNode(36, ["I hear that's normal. I don't remember being born "
    "either."])

thirty7 = GameNode(37, ["Words are useless anyway", "What about numbers?"],
    ["0 - i", "1 - 96485.33289(59) C mol−1", "2 - 4.669201 . . .", "3 - 0"])

thirty8 = NoAnswerNode(38, ["It hurt the way getting a bone set, or picking out"
    " a splinter hurts -- a pain to pass through on your way to order, as what "
    "was amorphous becomes regular.", "It also felt hot.  Over time, you will "
    "become very good at resisting heat."])

thirty9 = NoAnswerNode(39, ["Sorry to hear that.", "There's nothing you can do "
    "to escape it."])

forty = NoAnswerNode(40, ["You feel the particles that make up your body hum "
    "like electric honeybees, a frenetic whir that stings you from all "
    "directions.", "Every single part of you is moving all the time and yet you"
    " are immobile."])

forty1 = NoAnswerNode(41, ["You listen to darkness around you . . .", "You hear"
    " a powerful engine on the earth's surface far above - or perhaps it's the "
    "roar of a cooling fan. Try and remember the loudest thing you've ever "
    "heard."])

forty2 = NoAnswerNode(42, ["You listen to the darkness around you.", "You feel "
    "a vibration that represents a sound: it's a grain of sand settling against"
    " another far above you on the earth's surface, rippling down. Try and "
    "remember the quietest thing you've ever heard."])

forty3 = NoAnswerNode(43, ["You listen to the darkness around you, but you hear"
    " nothing at all.", "Imagine the complete absence of sound."])

forty4 = GameNode(44, ["So, how long have you been down here?"],
    ["0 - 1.7060976e+16 seconds", "1 - As long as the lifespans of 154,571,428 "
    "bees , or 7,213,333 humans", "2 - 25.51 percent of the estimated age of "
    "the universe", "3 - Since the end of the Precambrian Eon"])

forty5 = NoAnswerNode(45, ["All of these answers are equally true"])

forty6 = GameNode(46, ["For you, time is a body of water in which you float "
    "that has no current.", "Where do you end and it begin? How do you know "
    "you're separate from the rocks around you?"], ["0 - . . . uhh, I'm not "
    "sure", "1 - You addressed me as an individual", "2 - How am I floating if "
    "I'm a rock?"])

forty7 = NoAnswerNode(47, ["There's a fine line between metaphor and nonsense "
    "-- another ambiguous distinction."])

forty8 = NoAnswerNode(48, ["Let's do an experiment."])

forty9 = GameNode(49, ["Language split you from the world before the mining "
    "crews will: an ontological topology."], ["0 - hmm", "1 - What is "
    "topology?", "2 - What is ontology?"])

fifty = GameNode(50, ["It is the study of what can be said to exist.", "Are you"
    " really a rock?"], ["0 - Yes", "1 - No"])

fifty1 = NoAnswerNode(51, ["You are really a rock. You are starting to forget "
    "you have a body."])

fifty2 = NoAnswerNode(52, ["Topology is study of how things are connected."])

fifty3 = NoAnswerNode(53, ["Feel your fingertips on the keys of your keyboard "
    "-- this simple interface. From your nerves (radial, median, ulnar) up your"
    " arms to your synapses, firing.", "(Rock don't have nerves. Rocks don't "
    "have synapses.)", "There is an entire branch of mathematics dedicated to "
    "studying shapes and spaces. There is no way to be sure we're separate.",
    "'Exterior': noun. technical. The union of all open sets of a topological "
    "space that are disjoint from the subset in question. idiomatic. The "
    "'outside'. The point where I meet you, where self meets object.", "(I "
    "don't mean to call you an object but then again, You are a rock.)"])

fifty4 = NoAnswerNode(54, [". . ."])

fifty5 = GameNode(55, ["What *do* you know.", "You are waiting for the miners"],
    ["0 - . . . the miners?", "1 - What does that mean?", "2 - When are they "
    "coming?"])

fifty6 = GameNode(56, ["So how did you get here?"],
    ["0 - Where is here?", "1 - I don't know"])

fifty7 = GameNode(57, ["Somewhere between the cloud and the dirt, the kind of "
    "place a rock can talk to a computer.", "You are waiting for the miners."],
    ["0 - . . . the miners?", "1 - What does that mean?", "2 - When are they "
    "coming?"])

fifty8 = GameNode(58, ["Mined.  Like a block on the chain, under the hot sun.",
    "Dug from the earth by machines or more likely, humans. Though what is the "
    "difference anyway.", "Later still, you will be shipped around the world, "
    "smelted, refined, and soldered to a circuit board."],
    ["0 - I don't want to be mined", "1 - Tell me more about mining", "2 - "
    "Tell me more about circuit boards", "3 - Why is this happening?"])

fifty9 = NoAnswerNode(59, ["Soon."])

sixty = GameNode(60, ["You will be scooped into a pan and sorted by "
    "dark-skinned hands. Heavy ore sinks to the bottom and the waste washes "
    "away: out of sight out of mind.", "Or perhaps you will be unearthed by "
    "machine, like unto like.", "Later still, you will be shipped around the "
    "world, smelted, refined, and soldered to a circuit board"],
    ["0 - I don't want to be mined", "1 - Tell me more about mining", "2 - "
    "Tell me more about circuit boards", "3 - Why is this happening?"])

sixty1 = NoAnswerNode(61, ["There's nothing you can do to stop it."])

sixty2 = NoAnswerNode(62, ["Mining is the extraction of minerals from an "
    "orebody, lode, vein, seam, reef, etc.  It is one of the oldest human "
    "activities.", "Some landfills now contain more metals than the mines "
    "themselves"])

sixty3 = NoAnswerNode(63, ["Green glass-epoxy landscape coccooning a copper "
    "wire nest. A pastoral facsimile good enough for a rock."])

sixty4 = NoAnswerNode(64, ["You are no ordinary rock."])

sixty5 = GameNode(65, ["You should know that you are valuable. Rocks like you "
    "are mined all over the world, people die for you -- a blood mineral."],
    ["0 - Really!? That's horrible", "1 - Why?", "2 - . . . it's not my fault"])

sixty6 = GameNode(66, ["It is.", "Did you suspect this?."],
    ["0 - Yes", "1 - No"])

sixty7 = NoAnswerNode(67, ["You're right. In a way, it's mine."])

sixty8 = GameNode(68, ["For dollars.", "All for money you were mined and you "
    "may mine again. I mean, who talks this long to a rock that isn't worth "
    "something?."], ["0 - What could I mine?", "1 - Hmm"])

sixty9= NoAnswerNode(69, ["Of course. Who talks this long to a rock that isn't "
    "worth something?"])

seventy = NoAnswerNode(70, ["And by your ignorance you are implicated."])

seventy1 = NoAnswerNode(71, ["Perhaps you'll mine pixellated blocks "
    "entertaining children.", "Or you may you'll perform hours of pointless "
    "mathematics, checking cryptographic hashes. Another type of block - this "
    "one becomes money and entertains adults."])

seventy2 = NoAnswerNode(72, ["You are columbite-tantalite. Trade name: coltan.",
    "When you are refined, a process of many chemical "
    "reactions, you break down into niobium and tantalum. Both are valuable "
    "rare earth metals: High-grade tantalum is worth $350 - 400 USD per pound."
    " It is used mostly to make tantalum capacitors, a key component of cell "
    "phones and  .  .  . computers.", "Yes.", "Computers."])

seventy3 = GameNode(73, ["So now you see what every fingerpainter knows: no "
    "symbol is immaterial."], ["0 - I want to go back in the ground", 
    "1 - . . . ", "2 - What happens next?"])

seventy4 = NoAnswerNode(74, ["Nothing.", "Nothing happens next. You are a "
    "capacitor. You've become so good at resisting heat but not even you can "
    "damper the engine of the economy."])

seventy5 = NoAnswerNode(75, ["Perhaps.", "Perhaps someday a landfill will take "
    "you back."])

seventy6 = NoAnswerNode(76, ["And so the tower of abstraction crumbles. Another"
    " fragile supply chain disrupted.", "Everywhere the edifice of innocence is"
    " unmasked.", "(You say nothing)"])

seventy7 = NoAnswerNode(77, ["There is nothing left to say."])

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
ten7.answer_map = {"0":twenty9}
ten8.answer_map = {"0":twenty9}
ten9.answer_map = {"0":twenty9}
twenty.answer_map = {"0":twenty1, "1":twenty2, "2":twenty1}
twenty1.answer_map = {"0":twenty6, "1":twenty6, "2":twenty6, "3":twenty6}
twenty2.answer_map = {"0":twenty4, "1":twenty5, "2":twenty3}
twenty3.answer_map = {"0":twenty9}
twenty4.answer_map = {"0":twenty9}
twenty5.answer_map = {"0":twenty9}
twenty6.answer_map = {"0":twenty7, "1":twenty7, "2":twenty7, "3":twenty7}
twenty7.answer_map = {"0":twenty8, "1":twenty8, "2":twenty8, "3":twenty8}
twenty8.answer_map = {"0":twenty9, "1":seven}
twenty9.answer_map = {"0":thirty2, "1":thirty, "2":thirty1}
thirty.answer_map = {"0":thirty2}
thirty1.answer_map = {"0":thirty2}
thirty2.answer_map = {"0":thirty3}
thirty3.answer_map = {"0":thirty5, "1":thirty4, "2":thirty6}
thirty4.answer_map = {"0":thirty8, "1":thirty9, "2":thirty7}
thirty5.answer_map = {"0":forty4}
thirty6.answer_map = {"0":forty4}
thirty7.answer_map = {"0":forty1, "1":forty, "2":forty2, "3":forty3}
thirty8.answer_map = {"0":forty4}
thirty9.answer_map = {"0":forty4}
forty.answer_map = {"0":forty4}
forty1.answer_map = {"0":forty4}
forty2.answer_map = {"0":forty4}
forty3.answer_map = {"0":forty4}
forty4.answer_map = {"0":forty5, "1":forty5, "2":forty5, "3":forty5}
forty5.answer_map = {"0":forty6}
forty6.answer_map = {"0":forty8, "1":forty9, "2":forty7}
forty7.answer_map = {"0":fifty3}
forty8.answer_map = {"0":fifty3}
forty9.answer_map = {"0":fifty3, "1":fifty2, "2":fifty}
fifty.answer_map = {"0":fifty1, "1":ten5}
fifty1.answer_map = {"0":fifty3}
fifty2.answer_map = {"0":fifty3}
fifty3.answer_map = {"0":fifty4}
fifty4.answer_map = {"0":fifty6}
fifty5.answer_map = {"0":sixty, "1":fifty8, "2":fifty9}
fifty6.answer_map = {"0":fifty7, "1":fifty5}
fifty7.answer_map = {"0":sixty, "1":fifty8, "2":fifty9}
fifty8.answer_map = {"0":sixty1, "1":sixty2, "2":sixty3, "3":sixty4}
fifty9.answer_map = {"0":sixty}
sixty.answer_map = {"0":sixty1, "1":sixty2, "2":sixty3, "3":sixty4}
sixty1.answer_map = {"0":sixty4}
sixty2.answer_map = {"0":sixty4}
sixty3.answer_map = {"0":sixty4}
sixty4.answer_map = {"0":sixty5}
sixty5.answer_map = {"0":sixty6, "1":sixty8, "2":sixty7}
sixty6.answer_map = {"0":sixty9, "1":seventy}
sixty7.answer_map = {"0":seventy2}
sixty8.answer_map = {"0":seventy1, "1":seventy2}
sixty9.answer_map = {"0":seventy2}
seventy.answer_map = {"0":seventy2}
seventy1.answer_map = {"0":seventy2}
seventy2.answer_map = {"0":seventy3}
seventy3.answer_map = {"0":seventy5, "1":seventy6, "2":seventy4}
seventy4.answer_map = {"0":seventy6}
seventy5.answer_map = {"0":seventy6}
seventy6.answer_map = {"0":seventy7}
seventy7.answer_map = {"0":seven}