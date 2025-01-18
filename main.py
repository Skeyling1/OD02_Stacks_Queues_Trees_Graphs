

# last in, first out
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def add_item(self, item):
        return self.stack.append(item)

    def take_item(self):
        return self.stack.pop()


stack = Stack()

print("список пуст: ", stack.is_empty())
stack.add_item(12)
stack.add_item(13)
stack.add_item(14)
stack.add_item(15)
stack.add_item(16)
print("список пуст: ", stack.is_empty())
print(stack.take_item())
print(stack.take_item())
print(stack.take_item())
print(stack.take_item())
print(stack.take_item())
print("список пуст: ", stack.is_empty())

class Queue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue ==[]










