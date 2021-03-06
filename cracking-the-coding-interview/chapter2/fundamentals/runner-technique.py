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


llist = LinkedList()

one = Node("a1")
two = Node("a2")
three = Node("a3")
four = Node("a4")
five = Node("a5")
six = Node("b1")
seven = Node("b2")
eight = Node("b3")
nine = Node("b4")
ten = Node("b5")

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eight
eight.next = nine
nine.next = ten

llist.head = one

p2 = llist.head
p1 = p2.next

print(llist)

while p1.next is not None:
    p2 = p2.next
    p1 = p1.next.next

p1 = llist.head
p2 = p2.next
n1 = ""
n2 = ""

while p2.next is not None :
    temp = llist.head
    while temp is not None:
        if temp.next == p1.next:
            n1 = temp
        if temp.next == p2:
            n2 = temp
        temp = temp.next

    linkAfterP2 = p2.next
    temp = p1.next
    n1.next = p2
    p2.next = temp
    n2.next = linkAfterP2
    p2 = n2
    p1 = p1.next.next
    p2 = p2.next
    

print(llist)