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



class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.head = self.stack1.head

    def is_empty(self):
        return self.stack1.head is None and self.stack2.head is None
    
    def push(self,val):
        if self.stack2.is_empty():
            self.stack1.push(val)
        else:
            self.stack2.push(val)


    def remove(self):
        if self.stack1.is_empty():
            n = self.stack2.head.next
            temp = self.stack2.head.val
            self.stack2.pop()
            while n is not None:
                self.stack1.push(self.stack2.pop())
                n = n.next
            return temp

        n = self.stack1.head
        while n.next is not None:
            self.stack2.push(self.stack1.pop())
            n = n.next
        temp = n.val
        self.stack1.pop()
        return temp

    def peek(self):
        return None

    def __repr__(self):
        node = self.stack1.head
        nodes=[]

        while node is not None:
            nodes.append(f"{node.val}")
            node = node.next

        string = "->".join(nodes)

        node = self.stack2.head
        nodes=[]

        while node is not None:
            nodes.append(f"{node.val}")
            node = node.next
        
        if not bool(string) and nodes != []:
            return "Stack1: " + "None" + "\n" + "Stack2: " +"->".join(nodes)

        elif nodes == [] and bool(string):
            return "Stack1: " + string + "\n" + "Stack2: " + "None"

        return "Stack1: " + "None" + "\n" + "Stack2: " + "None"
        

test = MyQueue()
test.push(1)
test.push(2)
test.push(3)
test.push(4)
test.push(5)

test.remove()
test.remove()
test.remove()
test.remove()
test.remove()







print(test)