class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None



class DoubleLinkedList():
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    
    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1

        return node.value

    
    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            
        self.length -= 1

        return temp

    
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
        return True

    
    def pop_first(self):

        if self.head is None:
            return None
        
        temp = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        
        self.length -= 1
        return temp.value

    
    def get(self, index):

        if index < 0 or index >= self.length:
            return None

        if index < self.length // 2:
            
            temp = self.head

            for _ in range(index):
                temp = temp.next
            
            return temp
        
        else:
            tail = self.tail

            for _ in range(self.length - 1, index, - 1):
            
                tail = tail.prev
            
            return tail

        
    def set(self, value, index):
        node = self.get(index)

        if node:
            node.value = value
            return True
        return False

    
    def insert(self, value, index):

        before = self.get(index - 1)
        after = before.next

        if self.head == None:
            self.head = node
            self.tail = node
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            """
            insertar en la cola
            """
            return self.append(value)
        
        new_node = Node(value)
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node

        self.length += 1

        return new_node.value

    
    def remove(self, index):

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        before = self.get(index - 1)
        after = before.next

        before.next = after.next
        after.next.prev = before
        after.next = None
        after.prev = None

        self.length -= 1

        return True

    
    def print_reverse_list(self):

        temp = self.tail

        for _ in range(self.length - 1, -1, -1):
            print(temp.value)
            temp = temp.prev

    
    def clear(self):
        if self.length == 0:
            return True

        for _ in range(self.length):
            self.pop()
        
        return True

 

        
my_doubly_linked_list = DoubleLinkedList(value=0)
my_doubly_linked_list.append(value=1)
my_doubly_linked_list.append(value=2)
my_doubly_linked_list.append(value=3)
my_doubly_linked_list.append(value=4)
my_doubly_linked_list.append(value=5)
my_doubly_linked_list.append(value=6)

my_doubly_linked_list.print_list()

my_doubly_linked_list.append(value=7)
my_doubly_linked_list.pop_first()
my_doubly_linked_list.pop()
my_doubly_linked_list.set(value=0, index=0)
my_doubly_linked_list.insert(value=12, index=3)
my_doubly_linked_list.prepend(value=199)
my_doubly_linked_list.remove(index=2)
my_doubly_linked_list.remove(index=5)
my_doubly_linked_list.remove(index=0)

my_doubly_linked_list.clear()

print("......")


my_doubly_linked_list.print_reverse_list()
