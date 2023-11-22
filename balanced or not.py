from pythonds import Stack

def parCheck(string: str) -> bool:
    memory = Stack()

    for symbol in string:
        if symbol == "(":
            memory.push(symbol)
        else:
            try:
                memory.pop()
            except:
                return False

    if memory.isEmpty():
        return True
    else:
        return False

print(parCheck("("))