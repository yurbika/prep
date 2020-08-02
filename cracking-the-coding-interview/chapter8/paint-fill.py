screen = [
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10,
    [0]*10, ]
#        y  x
start = [17, 8]
color = 255


def paintFill(screen, startY, startX, color):
    if startY == len(screen) or startX == len(screen[startY]) or startY == -1 or startX == -1:
        return

    screen[startY][startX] = color

    # up
    if startY > -1 and screen[startY-1][startX] != color:
        paintFill(screen, startY-1, startX, color)
    # left
    if startX > -1 and screen[startY][startX-1] != color:
        paintFill(screen, startY, startX-1, color)
    # down
    if startY < len(screen)-1 and screen[startY+1][startX] != color:
        paintFill(screen, startY+1, startX, color)
    # right
    if startX < len(screen[startY])-1 and screen[startY][startX+1] != color:
        paintFill(screen, startY, startX+1, color)


paintFill(screen, start[0], start[1], color)

for i in screen:
    print(i)
