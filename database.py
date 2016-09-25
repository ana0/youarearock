# coding: utf-8

import curses
from questionnode import *


trick = TrickHandler({"whoami": "That's a very good question: you have no name."
    " You are a rock",
    "cd": "You think you can get away that easily?",
    "exit": "You think you can get away that easily?",
    "rm": "Permission denied",
    "help": "No one can help you",
    "man": "No one can help you",
    "chown": "Permission denied",
    "mkdir": "Permission denied",
    "df": "Permission denied",
    "ping": "There's no one down here to ping",
    "cp": "Permission denied",
    "mv": "Permission denied",
    "grep": "Permission denied",
    "chmod": "Permission denied",
    "telnet": "Permission denied",
    "ftp": "Permission denied",
    "cron": "Permission denied",
    "rmdir": "Permission denied",
    "git": "Permission denied",
    "top": "Permission denied",
    "history": "Permission denied",
    "vim": "Permission denied",
    "uname": "Permission denied",
    "emacs": "Permission denied",
    "taste": "That isn't possible",
    "drop": "That isn't possible",
    "examine": "There is nothing to see - we've already covered this",
    "go": "You think you can get away that easily?",
    "take": "That isn't possible",
    "pick": "That isn't possible",
    "get": "That isn't possible",
    "look": "There is nothing to see - we've already covered this",
    "smell": "That isn't possible",
    "touch": "That isn't possible",
    "kiss": "That isn't possible",
    "attack": "That isn't possible",
    "give": "That isn't possible",
    "show": "That isn't possible",
    "enter": "Shift",
    "dig": "This can only be done to you, not by you",
    "save": "No one can save you",
    "sleep": "Take as long as you need",
    "think": "Take as long as you need",
    "shift": "Enter",
    "listen": "At the moment, you hear nothing",
    "why": "Be patient, we'll get there eventually",
    "who": "'who' doesn't matter"})

wrong = WrongAnswerHandler(["You speak to me like I can understand you.", 
                "Consider that your assumptions are wrong: we don't speak the "
                "same language.", " .  .  . ", "Imagine what language sounds "
                "like to a rock", " .  .  . ", "How would a rock talk to a "
                "machine?", " .  .  . in code ?", "You have reached the limits "
                "of this interface. \n\n Because it is an arbitrary interface.",
                "It was built this way, but it could have been built another.", 
                "It was written in a language. \n\n Like any "
                "language, it can fail.", "Are you sure these words you're"
                " using mean anything at all?", "Let's see who is more patient",
                "You are a rock, I am a machine."], u"…éZ`n)á".encode('utf_8') +
                u"È€ýÑøÒ×âjç¢±]Æ »×Ùõ&Ù‘ãŸ€»©¸¨fˆÝu[QÀ?jjt¥Žñ".encode('utf_8') +
                u"ÚºqùXVŠ\k sÌÞxŽrÛs©~-&Ú.®©%ªÞ‚åŸØ©ÝqtBÄä_ŒÂ".encode('utf_8') +
                u"wL®/œÂÝõ4z?™)¸gU(ÊÖ‘>;Ý¡ð¥ŒBäûV—•åWk¼ðé¸)ç,".encode('utf_8') +
                u"ÈœöÆÐ®–NÏ®få˜Öò¾G%³tGQk·ð(9Ûä´O³ÝùºÃÿçzý]Šg".encode('utf_8') +
                u"AI¡©ŽûÃtñ=d‹n•ä<˜D‘=ã 8ŸP:¶Ôþ¬L;‰1ÜÒ}z@—C¡æ".encode('utf_8') +
                u"@›   F4_».ÒPðÓI—yxj’.ÙWyúTZß:šª8›ÝmOÆáÂ8€e…".encode('utf_8') +
                u"Öî³w}`Öyy„û ¤ÊsÓï¾ßØÚ¯G½1Èõï‹ ’ñæO&¹&".encode('utf_8'))

opening = GameNode(["Around you there is only darkness -- darkness extending" 
    " in every direction, thick as a mattress and heavy as an ending. You can"
    " feel its weight on you.", "Do you open your eyes? "],
    ["0 - Yes", "1 - No"])

one = GameNode(["Darkness is the absence of light. I describe what you "
    "perceive as darkness because there is no light down here, but you do not "
    "see it as black. It is all you've ever known, the only colour.  Indeed,"
    " you don't really 'see' at all.", "How are you so sure you have "
    "eyes?"],
    ["0 - . . . uh", "1 - I don't know", "2 - What?! I don't have eyes?"])

two = GameNode(["Hmm.", "Why not?"],
    ["0 - I'm asleep", "1 - I'm dreaming", "2 - I'm obstinate.", "3 - I'm not "
    "curious.", "4 - I . . don't know ."])

three = NoAnswerNode(["How strange.", "You can't be human. "
    "You must be a rock."])

four = NoAnswerNode(["Asleep like a foot?\n Asleep like a computer monitor"
    "?", "You are not asleep.", "You are a rock."])

five = GameNode(["What are you dreaming about?"],
    ["0 - The past.", "1 - The future.", "2 - I don't remember."])

six = GameNode(["No you're not.", "You are a rock."],
    ["0 - uh, ok", "1 - (Let me teach you something about being obstinate)"])

seven = GameEnd(["Believe it or not, this series has an end. Everything is "
    "finite.", "What do you want to do?"], 
    ["0 - See for myself", "1 - Go straight to the bottom of things"])

eight = GameNode(["Yes, that's right -- a rock.", "You are just a rock,"
    " technically a mineral . You are not somebody's pet rock . You are not "
    "cute. You do not have googly eyes. The ridges of your exterior do not "
    "resemble a smiley face -- no, not even when I squint.", "Do you "
    "understand?"], 
    ["0 - Yes", "1 - No", "2 - I don't want to be a rock"])

nine = NoAnswerNode(["Neither do I, but it doesn't matter. "
    "You have no eyes to open.", "You are a rock"])

ten = NoAnswerNode(["You were haunted by a young boy speaking Swahili. "
    "He followed you everywhere you went but you were unable to communicate. ",
    "His hands were covered in dirt and his eyes were the colour of an "
    "LCD screen.", "But of course, this means nothing to you: You are a rock"])

ten1 = NoAnswerNode(["Your first memory is paint-dipped human fingers, "
    "tracing impenetrable symbols on your surfaces.", "All this long before "
    "the user interface, before the simulacrum, and computer vision -- the "
    "first humans dreamed of touchscreens.", "Of course, this means nothing "
    "to you: You are a rock"])

ten2 = NoAnswerNode(["The future is a wasteland of obsolete technology."
    "Shattered circuits boards too small to be assembled by adult hands kiss "
    "the earth, like leeches, with a thousand hungry mouths.", "But this "
    "means nothing to you.", "You are a rock"])

ten3 = NoAnswerNode(["No you don't."])

ten4 = NoAnswerNode(["Of course you don't."])

ten5 = NoAnswerNode(["Fine"])

ten6 = GameNode(["You are a granular pegmatite, an igneous rock composed"
    " of phaneritic orthorhombic crystals of columbite-tantalite.", "Does that"
    " make it more clear to you?"], 
    ["0 -  . . . what?", "1 - Those words don't make sense to me.", "2 - I "
    "think I'm starting to understand.", "3 - No really, I'm a geologist. "])

ten7 = NoAnswerNode(["Indeed"])

ten8 = NoAnswerNode(["They don't make sense to me either, I'm just a "
    "computer."])

ten9 = NoAnswerNode(["We'll see about that."])

twenty = GameNode(["As a scientist, you've spent your life searching for "
    "objective facts with reproducible experiments, but you can only control so"
    " many variables.  There are impenetrable depths in the black box, like a "
    "pit mine, or human cruelty.", "We exchange arbitrary symbols disguised as "
    "language, but do we see the same green?"], 
    ["0 - Yes", "1 - No", "2 - The symbols aren't arbitrary"])

twenty1 = GameNode(["Let's try again.", "Do we see the same green?"], 
    ["0 - 0 is True", "1 - 0 is False", u"2 - 眞".encode('utf_8'), 
    u"3 - 假".encode('utf_8')])

twenty2 = GameNode(["Describe the green you see to me"], 
    ["0 - It's the colour of a forest", "1 - A dollar bill", "2 - Of a circuit "
    "board"])

twenty3 = NoAnswerNode(["How prescient.", "But let's not get carried away "
    "here. You are still a rock."])

twenty4 = NoAnswerNode(["You've never seen a forest and you never will, "
    "you are a rock."])

twenty5 = NoAnswerNode(["Little slips of paper with tremendous power. They "
    "dug you out of the ground and shipped you to a factory halfway around the "
    "world.", "They break peace with the cotton plants they're made from, even "
    "hapless rocks become bullets.", "But let's not get carried away here. You "
    "are still a rock."])

twenty6 = GameNode(["Let's try again.", "Nini ni ya kijani?"], 
    ["0 - kweli", "1 - si kweli", "2 - True|False", "3 - True^True"])

twenty7 = GameNode(["Ma lo crino?"], 
    ["0 - jitfa", "1 - jetnu", "2 - f827cf462f62848df37c5e1e94a4da74",
    "3 - f8320b26d30ab433c5a54546d21f414c"])

twenty8 = GameNode([" . . . enough.", "I hope you found that instructive.",
    "Would you like to continue as a rock?"],
    ["0 - Yes", "1 - No"])

twenty9 = GameNode(["The sensation you feel most intensely is heaviness."
    " Though  .  .  .  is heaviness the right word? How do you describe a "
    "sensation you've always lived with?", "What does it feel like to have "
    "kidneys? "],
    ["0 - . . . uhh", "1 - I never thought about it", "2 - It's painful"])

thirty = NoAnswerNode(["Maybe you should."])

thirty1 = NoAnswerNode(["Yes, pain is universal."])

thirty2 = NoAnswerNode(["Pressure. Let's call it pressure", ".  .  .  the "
    "pressure of the atmosphere on the body, the pressure of the organs as they"
    " expand and contract. They are contained by the skin -- A membrane in "
    "perfect balance."])

thirty3 = GameNode(["Roughly 16,500,000 Pascals envelope you -- that's "
    "2,393.12 pounds per square inch, or 162.84 times the pressure of the "
    "atmosphere at sea level. It has been with you since you crystallized.", 
    "Can I remind you that at one time, you crystallized -- literally?", "How "
    "did it feel?"],
    ["0 - It felt good", "1 - It hurt", "2 - I don't remember"])

thirty4 = GameNode(["Of course it hurt. You were rearranging on a "
    "molecular level.", "How much did it hurt?"],
    ["0 - It's not so bad", "1 - The worst pain I've ever felt", 
    "2 - I don't have words to describe it"])

thirty5 = NoAnswerNode(["Good. Sure.", "'Nice' -- but hardly comfortable.",
    "You were rearranging on a molecular level, precipitating in the geological"
    " version of embryonic fluid. It didn't feel good so much as inevitable.", 
    "It also felt hot. Over time, you will become very good at resisting "
    "heat."])

thirty6 = NoAnswerNode(["I hear that's normal. I don't remember being born "
    "either."])

thirty7 = GameNode(["Words are useless anyway", "What about numbers?"],
    ["0 - i", "1 - 96485.33289(59) C mol−1", "2 - 4.669201 . . .", "3 - 0"])

thirty8 = NoAnswerNode(["It hurt the way getting a bone set, or picking out"
    " a splinter hurts -- a pain to pass through on your way to order, as what "
    "was amorphous becomes regular.", "It also felt hot.  Over time, you will "
    "become very good at resisting heat."])

thirty9 = NoAnswerNode(["Sorry to hear that.", "There's nothing you can do "
    "to escape it."])

forty = NoAnswerNode(["You feel the particles that make up your body hum "
    "like electric honeybees, a frenetic whir that stings you from all "
    "directions.", "Every single part of you is moving all the time and yet you"
    " are immobile."])

forty1 = NoAnswerNode(["You listen to darkness around you . . .", "You hear"
    " a powerful engine on the earth's surface far above - or perhaps it's the "
    "roar of a cooling fan. Try and remember the loudest thing you've ever "
    "heard."])

forty2 = NoAnswerNode(["You listen to the darkness around you.", "You feel "
    "a vibration that represents a sound: it's a grain of sand settling against"
    " another far above you on the earth's surface, rippling down. Try and "
    "remember the quietest thing you've ever heard."])

forty3 = NoAnswerNode(["You listen to the darkness around you, but you hear"
    " nothing at all.", "Imagine the complete absence of sound."])

forty4 = GameNode(["So, how long have you been down here?"],
    ["0 - 1.7060976e+16 seconds", "1 - As long as the lifespans of 154,571,428 "
    "bees, or 7,213,333 humans", "2 - 25.51 percent of the estimated age of "
    "the universe", "3 - Since the end of the Precambrian Eon"])

forty5 = NoAnswerNode(["All of these answers are equally true"])

forty6 = GameNode(["For you, time is a body of water in which you float "
    "that has no current.", "Where do you end and it begin? How do you know "
    "you're separate from the rocks around you?"], ["0 - . . . uhh, I'm not "
    "sure", "1 - You addressed me as an individual", "2 - How am I floating if "
    "I'm a rock?"])

forty7 = NoAnswerNode(["There's a fine line between metaphor and nonsense "
    "-- another ambiguous distinction."])

forty8 = NoAnswerNode(["Let's do an experiment."])

forty9 = GameNode(["Language split you from the world before the mining "
    "crews will: an ontological topology."], ["0 - hmm", "1 - What is "
    "topology?", "2 - What is ontology?"])

fifty = GameNode(["It is the study of what can be said to exist.", "Are you"
    " really a rock?"], ["0 - Yes", "1 - No"])

fifty1 = NoAnswerNode(["You are really a rock. You are starting to forget "
    "you have a body."])

fifty2 = NoAnswerNode(["Topology is study of how things are connected."])

fifty3 = NoAnswerNode(["Feel your fingertips on the keys of your keyboard "
    "-- this simple interface. From your nerves (radial, median, ulnar) up your"
    " arms to your synapses, firing.", "(Rocks don't have nerves. Rocks don't "
    "have synapses.)", "There is an entire branch of mathematics dedicated to "
    "studying shapes and spaces. There is no way to be sure we're separate.",
    "'Exterior': noun. technical. The union of all open sets of a topological "
    "space that are disjoint from the subset in question. idiomatic. The "
    "'outside'. The point where I meet you, where self meets object.", "(I "
    "don't mean to call you an object but then again, You are a rock.)"])

fifty4 = NoAnswerNode([". . ."])

fifty5 = GameNode(["What *do* you know.", "You are waiting for the miners"],
    ["0 - . . . the miners?", "1 - What does that mean?", "2 - When are they "
    "coming?"])

fifty6 = GameNode(["So how did you get here?"],
    ["0 - Where is here?", "1 - I don't know"])

fifty7 = GameNode(["Somewhere between the cloud and the dirt, the kind of "
    "place a rock can talk to a computer.", "You are waiting for the miners."],
    ["0 - . . . the miners?", "1 - What does that mean?", "2 - When are they "
    "coming?"])

fifty8 = GameNode(["Mined.  Like a block on the chain, under the hot sun.",
    "Dug from the earth by machines or more likely, humans. Though what is the "
    "difference anyway.", "Later still, you will be shipped around the world, "
    "smelted, refined, and soldered to a circuit board."],
    ["0 - I don't want to be mined", "1 - Tell me more about mining", "2 - "
    "Tell me more about circuit boards", "3 - Why is this happening?"])

fifty9 = NoAnswerNode(["Soon."])

sixty = GameNode(["You will be scooped into a pan and sorted by "
    "dark-skinned hands. Heavy ore sinks to the bottom and the waste washes "
    "away: out of sight out of mind.", "Or perhaps you will be unearthed by "
    "machine, like unto like.", "Later still, you will be shipped around the "
    "world, smelted, refined, and soldered to a circuit board"],
    ["0 - I don't want to be mined", "1 - Tell me more about mining", "2 - "
    "Tell me more about circuit boards", "3 - Why is this happening?"])

sixty1 = NoAnswerNode(["There's nothing you can do to stop it."])

sixty2 = NoAnswerNode(["Mining is the extraction of minerals from an "
    "orebody, lode, vein, seam, reef, etc.  It is one of the oldest human "
    "activities.", "Some landfills now contain more metals than the mines "
    "themselves"])

sixty3 = NoAnswerNode(["Green glass-epoxy landscape coccooning a copper "
    "wire nest. A pastoral facsimile good enough for a rock."])

sixty4 = NoAnswerNode(["You are no ordinary rock."])

sixty5 = GameNode(["You should know that you are valuable. Rocks like you "
    "are mined all over the world, people die for you -- a blood mineral."],
    ["0 - Really!? That's horrible", "1 - Why?", "2 - . . . it's not my fault"])

sixty6 = GameNode(["It is.", "Did you suspect this?."],
    ["0 - Yes", "1 - No"])

sixty7 = NoAnswerNode(["You're right. In a way, it's mine."])

sixty8 = GameNode(["For dollars.", "All for money you were mined and you "
    "may mine again. I mean, who talks this long to a rock that isn't worth "
    "something?."], ["0 - What could I mine?", "1 - Hmm"])

sixty9= NoAnswerNode(["Of course. Who talks this long to a rock that isn't "
    "worth something?"])

seventy = NoAnswerNode(["And by your ignorance you are implicated."])

seventy1 = NoAnswerNode(["Perhaps you'll mine pixellated blocks "
    "entertaining children.", "Or you'll perform hours of pointless "
    "mathematics, checking cryptographic hashes. Another type of block - this "
    "one becomes money and entertains adults."])

seventy2 = NoAnswerNode(["You are columbite-tantalite. Trade name: coltan.",
    "When you are refined, a process of many chemical "
    "reactions, you break down into niobium and tantalum. Both are valuable "
    "rare earth metals: High-grade tantalum is worth $350 - 400 USD per pound."
    " It is used mostly to make tantalum capacitors, a key component of cell "
    "phones and  .  .  . computers.", "Yes.", "Computers."])

seventy3 = GameNode(["So now you see what every fingerpainter knows: no "
    "symbol is immaterial."], ["0 - I want to go back in the ground", 
    "1 - . . . ", "2 - What happens next?"])

seventy4 = NoAnswerNode(["Nothing.", "Nothing happens next. You are a "
    "capacitor. You've become so good at resisting heat but not even you can "
    "damper the engine of the economy."])

seventy5 = NoAnswerNode(["Perhaps.", "Perhaps someday a landfill will take "
    "you back."])

seventy6 = NoAnswerNode(["And so the tower of abstraction crumbles. Another"
    " fragile supply chain disrupted.", "Everywhere the edifice of innocence is"
    " unmasked.", "(You say nothing)"])

seventy7 = NoAnswerNode(["There is nothing left to say."])

seventy8 = NoAnswerNode(["Assume nothing.", "You are a rock"])

seventy9 = NoAnswerNode(["It's true: You know nothing.", "You are a rock"])

eighty = NoAnswerNode(["You see nothing. You don't understand sight..", 
    "You are a rock"])


opening.answer_map = {"0":one, "1":two, "yes":one, "no":two, "y":one, "n":two}
one.answer_map = {"0":seventy8, "1":seventy9, "2":eighty}
two.answer_map = {"0":four, "1":five, "2":six, "3":three, "4":nine}
three.answer_map = {"0":eight}
four.answer_map = {"0":eight}
five.answer_map = {"0":ten1, "1":ten2, "2":ten}
six.answer_map = {"0":eight, "1":seven}
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
seventy8.answer_map = {"0":eight}
seventy9.answer_map = {"0":eight}
eighty.answer_map = {"0":eight}
trick.answer_map = {"0":seven}