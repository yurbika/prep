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

    def __repr__(self):
        return f"{self.array}"


temp = MultiStack(3)

temp.push(1)
temp.push(2)
temp.push(3)
temp.push(4)
temp.push(4)
temp.push(4)
temp.push(4)
temp.push(4)
temp.push(4)
temp.push(4)
temp.push(4)

temp.pop()

print(temp)
