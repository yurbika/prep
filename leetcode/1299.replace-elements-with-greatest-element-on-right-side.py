class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
            temp = arr[i+1:]
            if temp:
                arr[i] = max(temp)

        return arr
