
class Sequence(object):

    """Default gameplay sequence, takes four answers. answerwrong has yet to
    be worked into its own function"""

    def __init__(self, query, answer1, answer2, answer3, answer4, answerwrong):
        self.query = query
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.answerwrong = answerwrong

    def blank_input(self):
        answer = raw_input(" . . . ?").strip()
        
    def answer1_func(self):
        print self.answer1

    def answer2_func(self):
        print self.answer2

    def answer3_func(self):
        print self.answer3

    def answer4_func(self):
        print self.answer4

    def game_play(self):
        print self.query
        tries = 0
        answer = raw_input(" . . . ?").strip()
        while tries <= 2:
            if answer not in ("1", "2", "3", "4"):
                print "You speak to me like I can understand you.  Try again."
                answer = raw_input(" . . . ?").strip()
                tries += 1  
            elif answer == "1":
                self.answer1_func()
                break
            elif answer == "2":
                self.answer2_func()
                break
            elif answer == "3":
                self.answer3_func()
                break
            else:
                self.answer4_func()
                break
        else:
            while answer not in ("1", "2", "3", "4"):
                print "Imagine what language sounds like to a rock."
                answer = raw_input(" . . . ?").strip()
            else:
                if answer == "1":
                    self.answer1_func()
                elif answer == "2":
                    self.answer2_func()
                elif answer == "3":
                    self.answer3_func()
                else:
                    self.answer4_func()

class TwoAnswers(Sequence):

    """Instance of class Sequence that takes only two correct answers.  For y/n
    questions"""

    def override_function(self):
        tries = 1
        print "You speak to me like I can understand you.  Try again."
        answer = raw_input(" . . . ?").strip()
        while tries <= 2:
            if answer not in ("1", "2"):
                print "You speak to me like I can understand you.  Try again."
                answer = raw_input(" . . . ?").strip()
                tries += 1
            elif answer == "1":
                self.answer1_func()
                break
            else:
                self.answer2_func()
                break
        else:
            while answer not in ("1", "2"):
                print "Imagine what language sounds like to a rock."
                answer = raw_input(" . . . ?").strip()
            else:
                if answer == "1":
                    self.answer1_func()
                else:
                    self.answer2_func()

    def answer3_func(self):
        self.override_function()

    def answer4_func(self):
        self.override_function()

class OneAnswer(Sequence):

    """Instance of class Sequence that takes only one possible answer"""

    def override_function(self):
        tries = 1
        print "You speak to me like I can understand you.  Try again."
        answer = raw_input(" . . . ?").strip()
        while tries <= 2:
            if answer != "1":
                print "You speak to me like I can understand you.  Try again."
                answer = raw_input(" . . . ?").strip()
                tries += 1
            else:
                self.answer1_func()
                break
        else:
            while answer != "1":
                print "Imagine what language sounds like to a rock."
                answer = raw_input(" . . . ?").strip()
            else:
                self.answer1_func()

    def answer2_func(self):
        self.override_function()

    def answer3_func(self):
        self.override_function()

    def answer4_func(self):
        self.override_function()

class ThreeAnswers(Sequence):

    def answer4_func(self):
        tries = 1
        print "You speak to me like I can understand you.  Try again."
        answer = raw_input(" . . . ?").strip()
        while tries <= 2:
            if answer not in ("1", "2", "3"):
                print "You speak to me like I can understand you.  Try again."
                answer = raw_input(" . . . ?").strip()
                tries += 1
            elif answer == "1":
                self.answer1_func()
                break
            elif answer == "2":
                self.answer2_func()
                break
            else:
                self.answer3_func()
                break
        else:
            while answer not in ("1", "2", "3"):
                print "Imagine what language sounds like to a rock."
                answer = raw_input(" . . . ?").strip()
            else:
                if answer == "1":
                    self.answer1_func()
                elif answer == "2":
                    self.answer2_func()
                else:
                    self.answer3_func()
        
opening_sequence = TwoAnswers("Around you there is only darkness -- darkness extending " +
                            "in every direction, thick as a mattress and heavy as an ending. " +
                            "You can feel its weight on you.\n Do you open your eyes?\n " +
                            "    1 - Yes\n     2 - No", "Darkness is the absence of light.  I " +                            "describe what you perceive as darkness because there is no light down here, " \
                            "but you do not see it as black.\nIt is all you've ever known, " +
                            "the only colour.  Indeed, you don\'t really \"see\" at all.\n" +
                            "How are you so sure you have eyes?\nYou are a rock.", "Yes, what is there " +
                            "to be curious about, anyway.\nAfter all -- you are a rock.", "", "", "")

opening_sequence.game_play()
#opening_sequence.blank_input()
