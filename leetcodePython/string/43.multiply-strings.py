class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        solution = '0'

        for i in range(len(num1)):
            for j in range(len(num2)):
                temp = str(int(num1[i]) * int(num2[j]))
                if i < len(num1) and j < len(num2):
                    temp += '0' * len(num1[i+1:]) + '0' * len(num2[j+1:])
                elif i < len(num1) and j == len(num2):
                    temp += '0' * len(num1[i+1:])
                solution = str(int(solution) + int(temp))

        return solution
