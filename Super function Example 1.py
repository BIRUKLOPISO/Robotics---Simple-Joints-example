# Ethiopian Home types
class House:
    def __init__(self, door, window):
        self.door = door
        self.window = window

class CervisBet(House):
    def __init__(self , door, window, design, decor):
        super().__init__( door, window)  # It similar as calling the main family. See below.
        self.design = design
        self.decor = decor

class Gojo(House):
    def __init__(self, door, window, msoso, chid):
        House.__init__( self, door, window) # Instead of super() you can use the name of
        # the main class itself. When you use the name you must add "self".
        self.chid = chid
        self.msoso = msoso

gojo = Gojo("Tsid","shola", "wanza","Ye sinde")

print(gojo.window)
print(gojo.door)
print(gojo.chid)
print(gojo.msoso)

# Move to the second example

print("....====...")

cervisbet = CervisBet("Tsid","shola","L-Shape", "Kelem")

print(cervisbet.door)
print(cervisbet.window)
print(cervisbet.decor)
print(cervisbet.design)
