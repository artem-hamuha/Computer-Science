from python_review7 import Vehicle

class Motercycle(Vehicle):
    def __init__(self, center_stand_out=False):
        self.center_stand_out = center_stand_out
        super().__init__()
    
    def start(self):
        return 'sorry our of fuel'