class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]
        self.counter = 0

    def append(self, item):
        self.storage[self.counter] = item
        self.counter += 1

        if self.counter == self.capacity:
            self.counter = 0
        
    def get(self):
        storage = self.storage
        item = [x for x in storage if x is not None]
        return item
'''
    
    class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in xrange(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data
'''