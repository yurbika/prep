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

    def deleteNode(self,value):
        node = self.head

        while node is not None:    
            if node.val == value:
                self.head = node.next
                node.next.prev = None
                return None

            if node.next.val == value:
                node.next.next.prev = node.next.prev
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

    def insert_between(self,node,targetNode):
        n = self.head
        while n is not None:
            if n.next == targetNode:
                break
            n = n.next
        if n == None:
            return None
        node.next = n.next
        n.next.prev = node
        n.next = node
        node.prev = n
        
        

llist = LinkedList()

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)

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

#llist.deleteNode(5)
#llist.insert_front(seven)
#llist.insert_end(eight)
llist.insert_between(eight,two)


print(llist,eight.prev, eight.next,two.prev, two.next)


        