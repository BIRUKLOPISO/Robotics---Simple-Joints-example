class Bird:
    def fly(self):
        return "Flying high"

class Fish:
    def swim(self):
        return "Swimming deep"

def action(creature):
    return creature.fly()

bird = Bird()
print(action(bird))