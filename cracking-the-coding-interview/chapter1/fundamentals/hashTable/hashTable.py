class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr= [[] for i in range(self.MAX)]

    def getHashValue(self,key):
        return hash(key) % self.MAX

    def __setitem__(self,key,val):
        hashValue = self.getHashValue(key)
        self.arr[hashValue].append((key,val))

    def __getitem__(self,key):
        for ele in self.arr[self.getHashValue(key)]:
            if ele[0] == key:
                return ele[1]

    def __delitem__(self,key):
        for ele in self.arr[self.getHashValue(key)]:
            if ele[0] == key:
                self.arr[self.getHashValue(key)].remove(ele)
                return None

p = HashTable()

p["march 6"] = 1
p["march 17"] = 2
del p["march 6"]

print(p["march 6"], p.arr)