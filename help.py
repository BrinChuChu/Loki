# Single Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"Node({self.value})"
    
    def __repr__(self):
        return self.__str__()
# end of Node

class LinkedList:
    def __init__(self):
        self.__head = None
        self._size = 0
        # self.__index = 0

    @property
    def head(self):
        return self.__head
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        self._size = value
    
    def isEmpty(self):
        return self.__head is None

    # Making our linkedlist iterable
    def __iter__(self):
        self.__ptr = self.__head
        return self
    
    def __next__(self):
        if self.__head is None:
            return None
        elif self.__ptr is None:
            self.__ptr = self.__head
            raise StopIteration
        else:
            current = self.__ptr
            self.__ptr = current.next
            return current
    # end of iterable override
    
    def find(self, value):
        if self.__head is None:
            raise ValueError(f"{value} not found.")
        else:
            j = 0
            current = self.__head
            while current is not None:
                if current.value == value:
                    return j
                else:
                    current = current.next
                    j += 1
            raise ValueError(f"{value} not found.")

    def get(self, i):
        if self.__head is None or i >= self.size:
            raise IndexError("Index out of bounds.")
        else:
            j = 0
            current = self.__head
            while i != j:
                current = current.next
                j += 1
            
            return current.value
    
    def addAt(self, i, value):
        if i < 0:
            raise IndexError("Index cannot be negative.")
        elif i == 0:
            self.addFirst(value)
        elif i >= self.size:
            self.addLast(value)
        else:
            j = 0
            current = self.__head
            while i != j:
                current = current.next
                j += 1
            
            tail = current.next
            current.next = Node(value)
            current.next.next = tail
            self.size += 1
    
    def removeAt(self, i):
        if i < 0:
            raise IndexError("Index cannot be negative.")
        elif i == 0:
            self.removeFirst()
        elif i >= self.size:
            self.removeLast()
        else:
            j = 0
            prev = None
            current = self.__head
            while i != j:
                prev = current
                current = current.next
                j += 1
            
            prev.next = current.next
            self.size -= 1

    def addFirst(self, value):
        if self.__head is None:
            self.__head = Node(value)
            self.size = 1
        else:
            tail = self.__head
            self.__head = Node(value)
            self.__head.next = tail
            self.size += 1
    
    def removeFirst(self):
        if self.__head is not None:
            tail = self.__head.next
            self.__head = tail
            self.size -= 1
        
            
    def addLast(self, value):
        if self.__head is None:
            self.size = 1
            self.__head = Node(value)
        else:
            current_node = self.__head

            while current_node.next is not None:
                current_node = current_node.next
            
            # update current_node.next to a new node obj
            current_node.next = Node(value)
            self.size += 1
    
    def removeLast(self):
        # This could have been written better, but this is more readable
        if self.__head is not None:
            # there is only a Node at head
            grand_parent = None
            parent = self.__head
            child = self.__head.next

            if child is None:
                self.__head = None
            else:
                while child is not None:
                    grand_parent = parent
                    parent = child
                    child = parent.next
                
                grand_parent.next = None
            
            self.size -= 1

    def toList(self):
        if self.__head is None:
            return []
        else:
            result = []
            current_node = self.__head
            while current_node is not None:
                result.append(current_node.value)
                current_node = current_node.next
            return result        
# end of LinkedList