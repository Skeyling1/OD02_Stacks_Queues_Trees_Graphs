

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

    def upper_elmt(self):
        return self.stack[-1]


stack = Stack()

print("список Stack пуст: ", stack.is_empty())
stack.add_item(12)
print(stack.upper_elmt())
stack.add_item(13)
print(stack.upper_elmt())
stack.add_item(14)
print(stack.upper_elmt())
stack.add_item(15)
print(stack.upper_elmt())
stack.add_item(16)
print(stack.upper_elmt())
print("список Stack пуст: ", stack.is_empty())
print(stack.take_item())
print(stack.take_item())
print(stack.take_item())
print(stack.take_item())
print(stack.take_item())
print("список Stack пуст: ", stack.is_empty())



# last in, last out
class Queue():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==[]

    def queue_add(self, item):
        return self.items.insert(0, item)

    def queue_goes(self):
        return self.items.pop()

    def upper_elmt(self):
        return self.items[-1]


queue = Queue()

print("список Queue пуст: ", queue.is_empty())
queue.queue_add(12)
queue.queue_add(13)
queue.queue_add(14)
queue.queue_add(15)
queue.queue_add(16)
print(queue.upper_elmt())
print("список Queue пуст: ", stack.is_empty())
print(queue.queue_goes())
print(queue.queue_goes())
print(queue.queue_goes())
print(queue.queue_goes())
print(queue.queue_goes())
print("список Queue пуст: ", queue.is_empty())










