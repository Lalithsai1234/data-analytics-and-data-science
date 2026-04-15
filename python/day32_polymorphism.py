"""
polymorphism -- means many types
1) Duck typing
2) Method Overriding
3) Method Overloading
4) Operator Overloading
"""
# 1) Duck typing
class robo: #here we are the creating the main class to reduce the redundancy
    def walk(self):
        print("walk")
    def talk(self):
        print("talk")
class fighter_robo(robo):
    def fight(self):
        print("fight")
    # def walk(self):
    #     print("walk")
    # def talk(self):
    #     print("talk")
class drive_robo(robo):
    def drive(self):
        print("drive")
    # def walk(self):
    #     print("walk")
    # def talk(self):
    #     print("talk")
def access(r):
    r.walk()
    r.talk()
    if isinstance(r, fighter_robo):
        r.fight()
    elif isinstance(r, drive_robo):
        r.drive()
f=fighter_robo()
# d=drive_robo() instead of using this we can use access(drive_robo())
# f.walk()
# f.talk()
# d.walk()
# d.talk()
access(f)
print("="*32)
access(drive_robo())