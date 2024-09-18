class PartyAnimal:
    x = 0
    name = ""
    def __init__(a, b):
        a.name = b
        print(a.name, 'constructed')
        print(b, 'constructed')

    def party(c):
        c.x = c.x + 1
        print(c.name, "party count", c.x)


s = PartyAnimal('Sally')
j = PartyAnimal('Jim')
j.party()
s.party()
print('..................................')
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

k = FootballFan('Kofi')
l = FootballFan('Ama')
k.touchdown()
l.touchdown()