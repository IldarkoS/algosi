from pythonds import Stack

def divideByBase(number: int, base: int) -> str:
    digits = '0123456789ABCDEF'

    memory = Stack()
    while number > 0:
        memory.push(number % base)
        number //= base

    result = ''
    while not memory.isEmpty():
        result += digits[memory.pop()]

    return result