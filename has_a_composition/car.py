from engine import Engine

class Car:

    def __init__(self):
        self.engine = Engine()
    
    def useCar(self):
        print(self.engine.useEngine('1.0 TSI Engine'))


c = Car()
c.useCar()