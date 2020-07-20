class Node:
    def __init__(self,val):
        self.val = val
        self._next = None

    def __repr__(self):
        return self.val

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        node = self.head
        nodes=[]

        while node is not None:
            nodes.append(f"{node.val}")
            node = node.next

        return "->".join(nodes)    
    
    def is_empty(self):
        return self.head is None
    
    def remove(self):
        n = self.head
        if self.is_empty():
            return None
        if n.next is None:
            temp = n.val
            n.val = None
            n = None
            return temp
        while n.next.next is not None:
            n = n.next
        temp = n.next.val
        n.next = None
        return temp



    def push(self,val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        self.size += 1
        
    def peekFront(self):
        if self.is_empty():
            return None

        n = self.head

        while n.next is not None:
            n = n.next

        return n.val
    
    def peekEnd(self):
        if self.is_empty():
            return None

        return self.head.val


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.cnt = 0

    def enqueue(self,animal):
        if animal == "dogs":
            self.cnt += 1
            self.dogs.push(self.cnt)  

        if animal == "cats":
            self.cnt += 1
            self.cats.push(self.cnt)  

    def dequeueAny(self):
        if self.dogs.peekFront()<= self.cats.peekFront():
            return f"Dog: {self.dogs.remove()}"
        else:
            return f"Cat: {self.cats.remove()}"

    def dequeueDog(self):
            return f"Dog: {self.dogs.remove()}"
    
    def dequeueCat(self):
            return f"Cat: {self.cats.remove()}"

    def __repr__(self):
        node = self.dogs.head
        dogs=[]
        cats=[]

        while node is not None:
            dogs.append(f"{node.val}")
            node = node.next

        dogs = "->".join(dogs)  

        node = self.cats.head

        while node is not None:
            cats.append(f"{node.val}")
            node = node.next

        cats = "->".join(cats)

        return "Dogs: " + dogs + "\n" + "Cats: " + cats

test = AnimalShelter()
test.enqueue("dogs")
test.enqueue("cats")
test.enqueue("cats")


test.enqueue("dogs")
test.enqueue("cats")
test.enqueue("cats")

test.enqueue("dogs")
test.enqueue("cats")

test.enqueue("dogs")
test.enqueue("cats")







print(test.dequeueAny(),test.dequeueAny(),test.dequeueAny(), test.dequeueCat(),test)