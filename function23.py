class dog():
    def family(self):
        print("I belongs to family of Dogs")

class germanShepherd(dog):
    def breed(self):
        print("I am a German Shepherd")
class husky(dog):
    def breed(self):
        print("I am a husky")
    def family(self):
        print("I am class apart")
g = germanShepherd()
g.family()
g.breed()

h = husky()
h.family()
h.breed()
