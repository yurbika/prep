#my solution

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            temp = []
            for i in range(round(n/2)):
                i += 1
                temp += [i,-i]
                
            return temp
        
        else:
            temp = []
            for i in range(round((n-1)/2)):
                i +=1
                temp += [i,-i]
                   
            temp.append(0)
            return temp

#clever solution

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return range(1-n,n,2)