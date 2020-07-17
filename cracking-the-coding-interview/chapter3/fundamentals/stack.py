#last in => first out

class Node:
    def __init__(self,val):
        self.val = val
        self._next = None

    def __repr__(self):
        return self.val

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        node = self.head
        nodes=[]

        while node is not None:
            nodes.append(f"{node.val}")
            node = node.next

        return "->".join(nodes)    
    
    def is_empty(self):
        return self.head is None
    
    def pop(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp.val

    def push(self,val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        self.size += 1
        
    def peek(self):
        if self.is_empty():
            return None

        return self.head.val


test = Stack()


test.push(1)
test.push(2)
test.push(3)
test.push(4)


print(test)



print(test.pop(),test)