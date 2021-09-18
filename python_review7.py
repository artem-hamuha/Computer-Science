class Car:
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