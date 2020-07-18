class MultiStack:
    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.numOfStacks = 3
        self.array = [0] * (self.stacksize * self.numOfStacks)
        self.size = [0] * self.numOfStacks

    def IsEmpty(self,stacknum):
        return self.size[stacknum] == 0

    def IsFull(self,stacknum):
        return self.size[stacknum] == self.stacksize

    def IndexOfTop(self,stacknum):
        return stacknum*(self.stacksize)+self.size[stacknum]

    def push(self,stacknum,val):
        if self.IsFull(stacknum):
            raise Exception("Stack is Full")
        
        self.array[self.IndexOfTop(stacknum)] = val
        self.size[stacknum] +=1

    def pop(self,stacknum):
        if self.IsEmpty(stacknum):
            raise Exception("Stack is empty")

        temp = self.array[self.IndexOfTop(stacknum)-1]
        self.array[self.IndexOfTop(stacknum)-1] = 0
        self.size[stacknum] -= 1
        return temp

    def peek(self,stacknum):
        return self.array[self.IndexOfTop(stacknum)-1]

    def __repr__(self):
        return f"{self.array}"




newstack = MultiStack(33)
print(newstack.IsEmpty(1))
newstack.push(1, 3)
print(newstack.peek(1))
print(newstack.IsEmpty(1))
newstack.push(0, 1)
print(newstack.peek(1))
print(newstack.pop(1))
print(newstack.peek(1))
newstack.push(1, 3)
print(newstack)

