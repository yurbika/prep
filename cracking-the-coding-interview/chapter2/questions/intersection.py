class Node:
    def __init__(self,val):
        self.next = None
        self.prev = None
        self.val = val

    def __repr__(self):
        return f"{self.val}"
    

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes=[]

        while node is not None:
            nodes.append(f"{node.val}")
            node = node.next

        nodes.append("None")
        return "->".join(nodes)
    
    def insert_end(self,node):
        n = self.head
        while n is not None:
            if n.next == None:
                break
            n = n.next
        n.next = node

    def insert_front(self,node):
        head = self.head
        self.head = node
        self.head.next = head


num1 = LinkedList()
num2 = LinkedList()

num1digit1 = Node(3)
num1digit2 = Node(6)
num1digit3 = Node(7)

num2digit1 = Node(2)
num2digit2 = Node(3)
num2digit3 = Node(6)
num2digit4 = Node(7)

num1digit1.next = num1digit2
num1digit2.next = num1digit3
num1digit3.next = num2digit2

num2digit1.next = num2digit2
num2digit2.next = num2digit3
num2digit3.next = num2digit4


num1.head = num1digit1
num2.head = num2digit1

n1 = num1.head
n2 = num2.head
intersection = False

while n1 is not None:
    n2 = num2.head
    if intersection:
        break

    while n2 is not None:
        if n1 == n2:
            print(f"intersection Node: {n1}")
            intersection = True
            break
        n2 = n2.next
    n1 = n1.next

n1 = num1.head
n2 = num2.head
intersection = False

while n2 is not None:
    n1 = num2.head.next
    if intersection:
        break
    while n1 is not None:
        if n1 == n2:
            print(f"intersection Node: {n1}")
            intersection = True
            break
        n1 = n1.next
    n2 = n2.next