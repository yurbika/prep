class Node:
    def __init__(self,val):
        self.next = None
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

    def deleteNode(self,value):
        node = self.head

        while node is not None:    
            if node.val == value:
                print("here")
                self.head = node.next
                return None

            if node.next.val == value:
                node.next = node.next.next
                return None

            node = node.next
        
        

llist = LinkedList()

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)


one.next = two
two.next = three
three.next = four
four.next = five
five.next = six

two.prev = one
three.prev = two
four.prev = three
five.prev = four
six.prev = five

llist.head = one

llist.deleteNode(2)
llist.deleteNode(3)
llist.deleteNode(4)
llist.deleteNode(5)
llist.deleteNode(6)



print(llist)


        