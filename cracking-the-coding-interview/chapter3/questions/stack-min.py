import sys

class MultiStack:
    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.numOfStacks = 3
        self.array = [0] * (self.stacksize * self.numOfStacks)
        self.size = [0] * self.numOfStacks
        self.minvals = [sys.maxsize] * (stacksize * self.numOfStacks)

    def IsEmpty(self,stacknum):
        return self.size[stacknum] == 0

    def IsFull(self,stacknum):
        return self.size[stacknum] == self.stacksize

    def IndexOfTop(self,stacknum):
        return stacknum*(self.stacksize)+self.size[stacknum]

    def push(self,stacknum,val):
        if self.IsFull(stacknum):
            raise Exception("Stack is Full")
        #new
        if self.IsEmpty(stacknum):
            self.minvals[self.IndexOfTop(stacknum)] = val
        else:
            self.minvals[self.IndexOfTop(stacknum)] = min(
                val, self.minvals[self.IndexOfTop(stacknum) - 1])
        ######
        self.array[self.IndexOfTop(stacknum)] = val
        self.size[stacknum] +=1

    #new function
    def min(self, stacknum):
        return self.minvals[self.IndexOfTop(stacknum)-1]

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




newstack = MultiStack(10)
newstack.push(0, 3)
newstack.push(0, 4)
newstack.push(0, 5)
newstack.push(0, 6)
newstack.push(0, 7)
newstack.push(0, 8)
newstack.push(0, 9)
newstack.push(0, 10)
newstack.push(0, 1)
newstack.push(0, 2)


newstack.pop(0)
print(newstack.minvals)

newstack.pop(0)



print( newstack.minvals)

