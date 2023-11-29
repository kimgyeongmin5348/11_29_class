import pickle
class NPC:
    def __init__(self, name, x, y, size):
        self.name, self.x, self.y, self.size = name, x, y, size


npc1 = NPC('jeni', 1, 2, 4.5)
npc2 = NPC('jisu', 100, 300, 2.5)

print(type(npc1.__dict__))
print(npc1.__dict__)

group = [npc1, npc2]
with open('npc.pickle', 'wb') as f:
    pickle.dump(group, f)

