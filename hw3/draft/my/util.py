
class Stack:
    def __init__(self):
        '''A new empty stack'''
        self._items = []
    
    def push(self, o):
        '''Make o the new top item in this Stack.'''
        self._items.append(o)
        
    def pop(self):
        '''Remove and return the top item.'''
        return self._items.pop()
    
    def peek1(self):
        '''Return the top item.'''
        return self._items[-1]
    
    def isEmpty(self):
        '''Return whether this stack is empty.'''
        return self._items == []
    
    def size(self):
        '''Return the number of _items in this stack.'''
        return len(self._items)

    def __str__(self):
        '''Return a copy of the element of self as a list'''
        return str(self._items[:])
        
class Queue:
    " implement Queue to make __myWalkBfs work correctly "
    pass