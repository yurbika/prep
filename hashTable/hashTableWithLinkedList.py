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
        nodes = []
        while node is not None:
            nodes.append(f"{node.val}")
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

class Node:
    def __init__(self,val,key):
        self.val = val
        self.key = key
        self.next = None
        
    def __repr__(self):
        return f"{self.key}, {self.val}"

    def __str__(self):
        return f"{self.key}, {self.val}"


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr= [LinkedList() for i in range(self.MAX)]

    def getHashValue(self,key):
        hasVal = 0
        for i in key:
            hasVal += ord(i)
        return hasVal % self.MAX

    def __setitem__(self,key,val):
        hashValue = self.getHashValue(key)
        temp = Node(val,key)
        if self.arr[hashValue].head == None:
            self.arr[hashValue].head = temp
        else:
            for node in self.arr[hashValue]:
                if node.next == None:
                    node.next = temp
                    break

    def __getitem__(self,key):
        for node in self.arr[self.getHashValue(key)]:
            if node.key == key:
                return node.val


p = HashTable()

p["march 6"] = "a"
p["march 17"] = "b"


print(p.arr)