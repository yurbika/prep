#in place swap -> no additional array 

arr = [
[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25],

]

length = len(arr)

for i in range(length):
    for j in range(i,length):
        temp = arr[i][j]
        arr[i][j] = arr[j][i]
        arr[j][i] = temp

for i in range(length):
    for j in range(round(length/2)):
        temp = arr[i][j]
        arr[i][j] = arr[i][length - 1 - j]
        arr[i][length - 1 - j] = temp

print(arr)


