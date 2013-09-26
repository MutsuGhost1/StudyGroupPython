

class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, element):
        self._items.insert(0,element)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def isEmpty(self):
        return self._items == []

    def __str__(self):
        return str(self._items[:])