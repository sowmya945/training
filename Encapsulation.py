class Cricket:
    def __init__(self, player, score):
        self.__player = player   # private — locked inside the class
        self.__score  = score    # private — locked inside the class

    def get_score(self):         # approved way to READ the score
        return self.__score

    def set_score(self, new_score):   # approved way to CHANGE the score
        if new_score >= 0:
            self.__score = new_score


cricket = Cricket("Rohit", 85)

# Attempt to change the private attribute directly from outside:
cricket.__score = 999        # looks like it worked — but it did NOT

print(cricket.get_score())   # still prints: 85
# Python created a brand-new attribute called __score
# The real private attribute _Cricket__score was never touched
# 

class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score  = score

    def set_score(self, new_score):
        if new_score >= 0:              # validation check
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")  # rejected safely

cricket = Cricket("Rohit", 85)
cricket.set_score(100)    # Score updated to 100
cricket.set_score(-5)     # Score cannot be negative.


