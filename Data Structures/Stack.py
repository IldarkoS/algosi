class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(list(self.items))


stck = Stack()
stck.push(1)
stck.push(2)
stck.push(3)
stck.push(4)
print(stck)
stck.pop()
print(stck.peek())
print(stck.size())