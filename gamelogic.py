class Sequence(object):
    
    def __init__(self, query, **answers):
        self.query = query
        self.answers = answers

    def game_play(self):
        print(self.query)
        tries = 0
        as_list = self.answers.keys()
        answer = input(" . . . ?").strip()
        while tries <= 2:
            if answer in as_list:
                print(self.answers[answer])
                break
            else:
                print("You speak to me like I can understand you. Try again")
                tries += 1
                answer = input(" . . . ?").strip()
        else:
            while answer not in as_list:
                print("Imagine what language sounds like to a rock.")
                answer = input(" . . . ?").strip()
            else:
                print(self.answers[answer])
                    
opening_sequence = Sequence("Around you there is only darkness -- darkness extending " 
                            "in every direction, thick as a mattress and heavy as an ending. " 
                            "You can feel its weight on you.\n\nDo you open your eyes?\n " 
                            "    1 - Yes\n     2 - No", one = "Darkness is the absence of light.  I " 
                            "describe what you perceive as darkness because there is no light down here, " 
                            "but you do not see it as black.\nIt is all you've ever known, " 
                            "the only colour.  Indeed, you don\'t really \"see\" at all.\n" 
                            "How are you so sure you have eyes?\nYou are a rock.\n", two = "Yes, what is there " 
                            "to be curious about, anyway.\nAfter all -- you are a rock.\n")

opening_sequence.game_play()
