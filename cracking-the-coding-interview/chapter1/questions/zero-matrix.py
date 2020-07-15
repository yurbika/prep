arr = [
[1,2,3,4,5,0],
[6,0,8,9,10,0],
[11,12,13,14,15,0],
[16,17,18,0,20,0],
[21,22,23,24,25,0],
]

length = len(arr)

def row(arr,i):
    for x in range(length):
        arr[i][x] = 0

def column(arr,i):
    for x in range(length):
        arr[x][i] = 0

for i in range(length):
    for j in range(length):
        if arr[i][j] == 0:
            arr[0][j] = 0
            arr[i][0] = 0


for i in range(length):
    if arr[0][i] == 0:
        row(arr,i)
    if arr[i][0] == 0:
        column(arr,i)


print(arr)