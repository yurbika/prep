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


one = Node("n")
two = Node("o")
three = Node("o")
four = Node("n")

one.next = two
two.next = three
three.next = four

llist.head = one

#one word check not a sentence
#nerver odd or even wouldnt work

def reverseList(llist):
    n = llist.head
    newList = LinkedList()
    while n is not None:
        if n == llist.head:
            temp = Node(n.val)
            newList.head = temp
        else:
            temp = Node(n.val)
            newList.insert_front(temp)
        n = n.next
    return newList

reversedLList = reverseList(llist)

def checkLists(l1,l2):
    n = l1.head
    n2 = l2.head

    while n is not None:
        if n.val != n2.val:
            return False
        n = n.next
        n2 = n2.next

    return True

print(checkLists(llist,reversedLList))