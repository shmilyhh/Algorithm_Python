class Queue():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(items) == 0
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeuq(self):
        return self.items.pop()
    
    def size(self):
        return len(items)