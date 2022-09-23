class Player:

    # Number of players in the game
    count = 0  # Leo: actually this is class variable

    def __init__(self, name):
        self.name = name
        self.count += 1


p1 = Player("Leo")
print(p1.count)
print(Player.count)

p2 = Player("Abhi")
print(p2.count)
'''
Takeaways:
Class Variables remain unchanged
Object count has changed
'''
