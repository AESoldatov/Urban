from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        if dz >= 0:
            self._cords[2] = dz * self.speed
        else:
            print("It's too deep, i can't dive :(" )
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {randint(1,4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] -= abs(dz)
        self.speed /= 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"



db = Duckbill(10)

print(db._DEGREE_OF_DANGER)
print(Duckbill.mro())
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(50)
db.get_cords()
db.lay_eggs()

# ani = Animal(10)
# ani.move(1,2,-1)
# ani.get_cords()
# ani.attack()
# ani.speak()
# brd = Bird(10)
# brd.get_cords()
# brd.lay_eggs()
# sel = AquaticAnimal(10)
# sel.dive_in(-2)
# sel.get_cords()
# print(sel.speed)

