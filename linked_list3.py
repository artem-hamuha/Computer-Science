class data:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.next = pointer
    def get_data(self):
        return self.data
    def set data(self, data):
        self.data = data
    def get_next(self):
        return self.next
    def set_next(self, pointer):
        self.next = pointer