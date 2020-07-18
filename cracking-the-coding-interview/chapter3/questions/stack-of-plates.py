class MultiStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = []


    def push(self,val):
        if self.array == []:
            self.array.append([val])
        else:
            if len(self.array[-1]) >= self.capacity:
                self.array.append([val])
            else:
                self.array[-1].append(val)

    def pop(self):
        if self.array == []:
            raise Exception("Stack is empty")
        else:
            temp = self.array[-1][len(self.array[-1])-1]
            self.array[-1].remove(temp)
            if self.array[-1] == []:
                self.array = [ele for ele in self.array if ele != []]
            return temp

    def popAt(self,stacknum):
        if self.array == []:
            raise Exception("Stack is empty")
        else:
            temp = self.array[stacknum][len(self.array[stacknum])-1]
            self.array[stacknum].remove(temp)
            flattenedArray = [item for sublist in self.array for item in sublist]
            shiftedArray = []
            for i in flattenedArray:
                if shiftedArray == []:
                    shiftedArray.append([i])
                elif len(shiftedArray[-1]) >= self.capacity:
                    shiftedArray.append([i])
                else:
                    shiftedArray[-1].append(i)

            self.array = shiftedArray
            return temp
        



    def __repr__(self):
        return f"{self.array}"


temp = MultiStack(3)

temp.push(1)
temp.push(2)
temp.push(3)
temp.push(4)
temp.push(5)
temp.push(6)
temp.push(7)
temp.push(8)
temp.push(9)
temp.push(10)
temp.push(11)
temp.push(11)
temp.push(11)



temp.popAt(1)
temp.popAt(1)
temp.popAt(1)
temp.popAt(1)
temp.popAt(1)
temp.popAt(1)
# temp.popAt(1)
# temp.popAt(1)
# temp.popAt(1)
# temp.popAt(1)
#temp = [1,2,3]

print(temp)
