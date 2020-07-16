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
eight = Node(8)
nine = Node(9)
ten = Node(10)

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


def kth(val,node):
    if node == None:
        return 0
    index = kth(val,node.next) + 1
    if index == val:
        print(node)
    return index

print(kth(3,llist.head))
