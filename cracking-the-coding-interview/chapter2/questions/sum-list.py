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

num1digit1 = Node(9)
num1digit2 = Node(9)
num1digit3 = Node(9)

num2digit1 = Node(2)
num2digit2 = Node(3)
num2digit3 = Node(6)
num2digit4 = Node(7)

num1digit1.next = num1digit2
num1digit2.next = num1digit3

num2digit1.next = num2digit2
num2digit2.next = num2digit3
num2digit3.next = num2digit4


num1.head = num1digit1
num2.head = num2digit1


#assume no digit is higher than 9 or less than 0

def addTwoLList(llist1,llist2):
    n1 = llist1.head
    n2 = llist2.head
    overflow = 0
    newList = LinkedList()
    while n1 is not None or n2 is not None:
            if n1 is None:
                temp = Node((0 + n2.val + overflow) % 10)
                if (0 + n2.val + overflow) >= 10:
                    overflow = 1
                else:
                    overflow = 0

            elif n2 is None:
                temp = Node((n1.val + 0 + overflow) % 10)
                if (n1.val + 0 + overflow) >= 10:
                    overflow = 1
                else:
                    overflow = 0

            else:
                temp = Node((n1.val + n2.val + overflow) % 10)
                if (n1.val + n2.val + overflow) >= 10:
                    overflow = 1
                else:
                    overflow = 0

            if n1 == llist1.head:
                newList.head = temp
            else:
                newList.insert_end(temp)
            
            if n1 is not None:
                n1 = n1.next

            if n2 is not None:
                n2 = n2.next

            
    if overflow > 0:
        temp = Node(1)
        newList.insert_end(temp)
    
    return newList



num3 = addTwoLList(num1,num2)
print(num3)

#digits are in forward order
overflow = 0

num1digit1 = Node(7)
num1digit2 = Node(6)
num1digit3 = Node(3)
num1digit4 = Node(2)


num2digit1 = Node(9)
num2digit2 = Node(9)
num2digit3 = Node(9)

num1.head = num1digit1
num2.head = num2digit1

num1digit1.next = num1digit2
num1digit2.next = num1digit3
num1digit3.next = num1digit4


num2digit1.next = num2digit2
num2digit2.next = num2digit3

n1 = num1.head
n2 = num2.head
num3 = LinkedList()


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

num1reversed = reverseList(num1)
num2reversed = reverseList(num2)

num3reversed = reverseList(addTwoLList(num1reversed,num2reversed))

print(num3reversed)