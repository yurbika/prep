arr = [
[1,2,3],
[4,5,6],
[7,8,9]
]

def rotate(arr):
    temp = 0
    temp2 = 0
    counter = 0

    for i in range(1):
        for j in range(len(arr)-1): 
            temp = arr[i][len(arr) - 1 - j]
            arr[i][len(arr) - 1 - j] = arr[i][j]

            temp2 = arr[len(arr) - 1][len(arr) - 1]
            arr[len(arr) - 1][len(arr) - 1] = temp

            temp = arr[len(arr) - 1 - j][0]
            arr[len(arr) - 1 - j][0] = temp2

            arr[i][j] = temp
            
            


    return arr

print(rotate(arr))
