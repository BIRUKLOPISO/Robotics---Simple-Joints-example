class Person:
    def sing(self):
        return "I can sing a song"

class Bird:
    def sing(self):
        return "I can make a sound in the morning!"

class Car:
    def sing(self):
        return "I can say peeep!"

def ducktyping(method):
    print(method.sing())

person = Person()
bird = Bird()
car = Car()

ducktyping(person)
ducktyping(bird)
ducktyping(car)
