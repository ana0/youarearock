class Sequence(object):
    
    def __init__(self, query, *answers):
        self.query = query
        self.answers = answers

    def game_play(self):
        print(self.query)
        tries = 0
        as_list = list(self.answers)
        answer = input(" . . . ?").strip()
        while tries <= 2:
            if int(answer) in range(1, len(as_list)):
                print(as_list[int(answer)-1])
                break
            else:
                print("You speak to me like I can understand you. Try again")
                tries += 1
                answer = input(" . . . ?").strip()
        else:
            while int(answer) not in range(1, len(as_list)):
                print("Imagine what language sounds like to a rock.")
                answer = input(" . . . ?").strip()
            else:
                print(as_list[int(answer)])
                    
