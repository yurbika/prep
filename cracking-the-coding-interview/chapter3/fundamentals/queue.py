#last in => first out

class Node:
    def __init__(self,val):
        self.val = val
        self._next = None

    def __repr__(self):
        return self.val

class Queue:
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
    
    def remove(self):
        n = self.head
        if self.is_empty():
            return None
        if n.next is None:
            temp = n.val
            n.val = None
            n = None
            return temp
        while n.next.next is not None:
            n = n.next
        temp = n.next.val
        n.next = None
        return temp



    def push(self,val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        self.size += 1
        
    def peek(self):
        if self.is_empty():
            return None

        return self.head.val


test = Queue()


test.push(1)
test.push(2)
test.push(3)
test.push(4)


print(test)

print(test.remove(),test.remove(),test.remove(),test.remove(),test)