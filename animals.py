class Animal:
    def __init__(self, legs=4):
        self.legs=legs
        self.sound="Meh"

    def say(self):
        print (self.sound)

class Bird(Animal):
    def __init__(self, sound="Pip...pip"):
        self.legs=2
        self.sound=sound
        self.airborn=False

    def  fly(self):
        if self.airborn:
            pass
        else:
            print ('Taking off')
            self.airborn=True
