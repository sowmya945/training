class Cricket:
    def info(self):
        print("Cricket score info")  # Cricket's version

class Football:
    def info(self):
        print("Football score info")  # Football's version

c = Cricket()
f = Football()
c.info()   # runs Cricket's info()
f.info()   # runs Football's info() — same method name, different result


class Cricket:
    def play(self):
        print("Rohit hits a six!")      # Cricket's version of play()

class Football:
    def play(self):
        print("Arjun scores a goal!")   # Football's version of play()

c = Cricket()
f = Football()
c.play()   # Rohit hits a six!
f.play()   # Arjun scores a goal!


cricket  = Cricket("Rohit",  85)
football = Football("Arjun", 2)

for sport in (cricket, football):
    sport.info()   # Cricket runs its info(); Football runs its info()
    sport.play()   # Cricket runs its play(); Football runs its play()
    print()

# Output:
# Cricket  - Player: Rohit, Score: 85
# Rohit hits a six!
#
# Football - Player: Arjun, Score: 2
# Arjun scores a goal!

