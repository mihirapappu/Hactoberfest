class car:
    def start(self):
        print("engine statrted")
    def move(self):
        print("car staterd moving")
    def stop(self):
        print("car stoped")
class clock:
    def start(self):
        print("clock started tik tok")
    def move(self):
        print("clock moved")
    def stop(self):
        print("clocked stoped running")
Car= car()
Clock=clock()

def do_something(x):
    x.move()
    x.stop()
