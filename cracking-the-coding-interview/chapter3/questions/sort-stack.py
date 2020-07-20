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


s1 = Stack()
s2 = Stack()

s1.push(71)
s1.push(101)
s1.push(981)
s1.push(21)
s1.push(64)
s1.push(31)
s1.push(981)
s1.push(27)
s1.push(55)
s1.push(89)




print(s1)


def sortStack(s1,s2):
    temp = None
    while not s1.is_empty():
        temp = s1.pop()

        if s2.is_empty():
            s2.push(temp)

        elif temp > s2.peek():
            cnt = 0
            while not s2.is_empty() and temp > s2.peek():
                s1.push(s2.pop())
                cnt += 1
            
            s2.push(temp)

            while cnt != 0:
                s2.push(s1.pop())
                cnt -= 1

        else:
            s2.push(temp)

            
sortStack(s1,s2)

print(s2)