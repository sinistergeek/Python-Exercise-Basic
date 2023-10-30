class dog():
    def family(self):
        print("I belong to family of Dogs")

class germanShepard(dog):
    def breed(self):
        print("I am a German Shepherd")

class husky(dog):
    def breed(self):
        print("I am a husky")


g = germanShepard()
g.family()
g.breed()
h = husky()
h.family()
h.breed()
