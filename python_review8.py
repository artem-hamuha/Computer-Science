class Vehicle:
    def __init__(self, started=False, speed=0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        return 'Car started'
    
    def accelerate(self, rate=None):
        if self.started:
            if rate == None:
                return 'You cant accelarete by 0!!!'
            if rate == 0:
                return 'You cant accelarete by 0!!!'
            self.speed = self.speed + rate
            return 'Accelarated by {} miles. Current speed is {} mph'.format(rate, self.speed)
        else:
            return 'To accelerate Car needs to be started'
    
    def stop(self):
        if self.started == False:
            return 'Car already off'
        else:
            self.speed = 0
            return 'Car is off'

class Car(Vehicle):
    def __init__(self, trunk_open=False):
        self.trunk_open = trunk_open
    
    def open_trunk(self):
        if self.trunk_open == False:
            self.trunk_open = True
            return 'Trunk open'
        else:
            return 'Trunk already open'
    
    def close_trunk(self):
        if self.trunk_open == True:
            self.trunk_open = False
            return 'Trunk closed'
        else:
            return 'Trunk already closed'

car = Car()
print(car.start()) # we can use Vehicle methods in the class Car(inheritence)
print(car.open_trunk())