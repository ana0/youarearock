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
                    
