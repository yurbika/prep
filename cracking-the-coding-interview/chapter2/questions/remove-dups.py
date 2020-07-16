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

one = Node(1)
two = Node(1)
three = Node(1)
four = Node(1)
five = Node(1)
six = Node(1)
seven = Node(1)
eight = Node(2)
nine = Node(1)
ten = Node(1)

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
p1 = llist.head.next

def deleteNode(node):
    head = llist.head
    while head is not None:
        if head.next == node:
            break
        head = head.next
    head.next = head.next.next
    


while p2 is not None:
    p1 = p2.next

    while p1 is not None:
        if p1.next is not None and p1.next.val == p2.val:
            deleteNode(p1.next)
        elif p1.val == p2.val:
            deleteNode(p1)
            p1 = p1.next
        else:
            p1 = p1.next

    p2 = p2.next

print(llist)