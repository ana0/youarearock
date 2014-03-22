def opening_sequence():
    print "Around you there is only darkness -- darkness extending in every direction, thick as a mattress and heavy as an ending."
    print "You can feel its weight on you.  Do you open your eyes?"
    print "    1 - Yes"
    print "    2 - No"
    answer1 = raw_input(" . . . ?").lower()
    tries1 = 0
    if answer1 == "1":
        print "Darkness is the absence of light.  I describe what you perceive as darkness because there is no light down here, but you do not see it as black."
        print "It is all you've ever known, the only colour.  Indeed, you don't really \"see\" at all."
        print "How are you so sure you have eyes?"
        print "You are a rock."
    elif answer1 == "2":
        print "Yes, what is there to be curious about, anyway."
        print "After all -- you are a rock."
    else:
        print "You speak to me like I can understand you.  Try again."
        while tries1 <= 2:
            answer2 == raw_input(" . . . ?").lower()
            tries += 1
            return "Imagine what language sounds like to a rock."
            
        
    
