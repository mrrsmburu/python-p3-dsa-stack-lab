class Stack:

    def __init__(self, limit=None):
        self.stack = []
        self.limit = limit
    
    def push(self, value):
        if self.limit is not None and len(self.stack) >= self.limit:
            raise OverflowError("Stack is full")
        self.stack.append(value)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return self.limit is not None and len(self.stack) >= self.limit
    
    def search(self, value):
        try:
            # Finds the position of the value (0-based index) from the top
            # Subtracting from the length gives the distance from the top
            return len(self.stack) - 1 - self.stack[::-1].index(value)
        except ValueError:
            return -1
