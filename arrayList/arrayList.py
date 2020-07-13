class DynamicArray:
    def __init__(self,size=10):
        self.MAX_SIZE = size
        self.list = [None] * self.MAX_SIZE
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, index):

        if index < 0 or index > self.size:
            raise IndexError("Out of bounds!")

        return self.list[index]

    def append(self, val):
        if self.size == self.MAX_SIZE:
            self._increase_size()

        self.list[self.size] = val
        self.size += 1

    def _increase_size(self):
        newMaxSize = self.MAX_SIZE * 2
        newList = [None] * newMaxSize

        for i in range(self.list):
            newList[i] = self.list[i]

        self.MAX_SIZE = newMaxSize
        self.list = newList

    def insert(self,pos,val):

        if pos < 0 or pos > self.size:
            raise IndexError("Out of bounds")

        if self.size == self.MAX_SIZE:
            self._increase_size()

        for i in range(self.size-1, pos-1,-1):
            self.list[i+1] = self.list[i]

        self.list[pos] = val
        self.size += 1 

    def __repr__(self):
        return f"{self.list}"

arr = DynamicArray() 
arr.append(1)
arr.insert(1, 21431241) 
print(arr)