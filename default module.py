

class Sequence(object):

    def __init__(self, query, answer1, answer2, answer3, answer4, answerwrong):
        self.query = query
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.answerwrong = answerwrong

    def input():
        answer = raw_input(" . . . ?").strip()

    def game_play():
        for line in query:
            print line
        tries = 0
        answer = ""
        input()
        while tries <= 2:
            if answer not in ("1", "2", "3", "4"):
                print "You speak to me like I can understand you.  Try again."
                input()
                tries += 1  
            elif answer == "1":
                for line in answer1:
                    print line
                break
            elif answer == "2":
                for line in answer2:
                    print line
                break
            elif answer == "3":
                for line in answer3:
                    print line
                break
            else:
                for line in answer4:
                    print line
                break
        else:
            while answer not in ("1", "2", "3", "4"):
                print "Imagine what language sounds like to a rock."
                input()
            else:
                if answer == "1":
                    for line in answer1:
                        print line
                elif answer == "2":
                    for line in answer2:
                        print line
                elif answer == "3":
                    for line in answer3:
                        print line
                else:
                    for line in answer4:
                        print line

opening_sequence()
            
        
    
