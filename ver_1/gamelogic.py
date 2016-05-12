class Sequence(object):
    
    def __init__(self, query, *answers):
        self.query = query
        self.answers = answers

    def game_play(self):
        print(self.query)
        tries = 0
        as_list = list(self.answers)
        answer = input(" . . . ?").strip()
        range_check = [i for i in range(1, len(as_list)+1)]
        while tries <= 2:
            if answer in str(range_check):
                print(as_list[int(answer)-1])
                break
            else:
                print("You speak to me like I can understand you. Try again")
                tries += 1
                answer = input(" . . . ?").strip()
        else:
            while answer not in str(range_check):
                print("Imagine what language sounds like to a rock.")
                answer = input(" . . . ?").strip()
            else:
                print(as_list[int(answer)-1])
                    

