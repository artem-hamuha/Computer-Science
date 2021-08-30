class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next_node = next

    def get_next(self):
        return self.next_node

    def set_next(self, next):
        self.next_node = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True