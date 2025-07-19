class Stack:

    def __init__(self, items=None, limit=100):
        """
        Initialize the stack with an optional list of items and a limit.
        """
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        """
        Return True if the stack is empty.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Add an item to the stack if it is not full.
        """
        if self.full():
            return  # Do nothing if stack is full
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.
        If empty, return None.
        """
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        If empty, return None.
        """
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        """
        Return the number of items in the stack.
        """
        return len(self.items)

    def full(self):
        """
        Return True if the stack has reached its limit.
        """
        return len(self.items) >= self.limit

    def search(self, target):
        """
        Return how far the target is from the top of the stack (1-based index).
        Return -1 if the target is not found.
        """
        if target not in self.items:
            return -1
        return len(self.items) - self.items.index(target) - 1



