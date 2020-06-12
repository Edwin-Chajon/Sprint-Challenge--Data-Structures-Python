class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.counter = 0

    def append(self, item):
        self.storage[self.counter] = item
        self.counter += 1

        if self.counter == self.capacity:
            self.counter = 0
        
    def get(self):
        storage = self.storage
        new_item = [item for item in storage if item is not None]
        return new_item