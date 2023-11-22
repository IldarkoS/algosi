class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return True if len(self.item) == 0 else False

    def enqueue(self, elem):
        self.item.insert(0, elem)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)

    def __repr__(self):
        return str(self.item)
