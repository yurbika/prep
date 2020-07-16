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
                self.head = node.next
                return None

            if node.next.val == value:
                node.next = node.next.next
                return None

            node = node.next

    def insert_front(self,node):
        head = self.head
        self.head = node
        self.head.next = head
        head.prev = self.head

    def insert_end(self,node):
        n = self.head
        while n is not None:
            if n.next == None:
                break
            n = n.next
        n.next = node
        node.prev = n

llist = LinkedList()

one = Node(3)
two = Node(1)
three = Node(1)
four = Node(1)
five = Node(10)
six = Node(2)
seven = Node(1)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven

llist.head = one

p1 = llist.head
p2 = llist.head
partition = 11
size = 0
#she created a head list and tail list and didnt modify the given list -> way easier
while p2.next is not None:
    p2 = p2.next
    size += 1



while size != 0:
    if llist.head.val >= partition:
        temp = p1
        llist.head = p1.next
        p2.next = temp
        p2.next.next = None
        p2 = p2.next
        size -= 1
        p1 = llist.head

    elif p1.next.val >= partition:
        temp = p1.next
        p1.next = p1.next.next
        p2.next = temp
        p2.next.next = None
        p2 = p2.next
        size -= 1
    else:
        p1 = p1.next
        size -= 1


print(llist)