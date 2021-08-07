class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements =[]
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        return elements
    
    def get(self, index):
        if index >= self.lenght():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index==index: return cur_node.data 
            cur_index+=1

my_list = linked_list()

my_list.append(1)
my_list.append(2)

print(my_list.display())