

# last in, first out
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]


stack = Stack()

print("список Stack пуст: ", stack.is_empty())
stack.push(12)
print(stack.peak())
stack.push(13)
print(stack.peak())
stack.push(14)
print(stack.peak())
stack.push(15)
print(stack.peak())
stack.push(16)
print(stack.peak())
print("список Stack пуст: ", stack.is_empty())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("список Stack пуст: ", stack.is_empty())



# last in, last out
class Queue():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==[]

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


queue = Queue()

print("список Queue пуст: ", queue.is_empty())
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)
queue.enqueue(16)
print(queue.size())
print("список Queue пуст: ", stack.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print("список Queue пуст: ", queue.is_empty())



class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

root = Node(70)

root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)
print(root.value)
print(root.left)
print(root.left.right.left.value)




class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(node,'->', ' -> '.join(map(str, self.graph[node])))

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.print_graph()
