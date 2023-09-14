class Batsman:
    def __init__(self, name):
        self.name = name

    def play(self):
        return f"{self.name} is batting"

class Bowler:
    def __init__(self, name):
        self.name = name

    def play(self):
        return f"{self.name} is bowling"
batsman = Batsman("John")
bowler = Bowler("Alice")
print(batsman.play()) 
print(bowler.play())  