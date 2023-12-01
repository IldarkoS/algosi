class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, elem):
        self.items.append(elem)

    def addRear(self, elem):
        self.items.insert(0, elem)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)

