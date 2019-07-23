def floodFill(canvas, x, y, newColor, oldColor = None):

    if oldColor == None:
        oldColor = canvas[y][x]

    # main action: paint a tile
    canvas[y][x] = newColor

    # base case 1: cant go up any more
    if y > 0:
        # should we?
        if canvas[y-1][x] == oldColor:
            floodFill(canvas, x, y-1, newColor, oldColor)

    # base case 2: cant go down anymore
    if y < len(canvas) - 1:
        # should we
        if canvas[y+1][x] == oldColor:
            floodFill(canvas, x, y+1, newColor, oldColor)

    # base case 3: cant go left anymore
    if x > 0:
        # should we
        if canvas[y][x-1] == oldColor:
            floodFill(canvas, x-1, y, newColor, oldColor)

    # base case 4: cant go right anymore
    if x < len(canvas[y]) - 1:
        # should we
        if canvas[y][x+1] == oldColor:
            floodFill(canvas, x+1, y, newColor, oldColor)


canvas = [
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,1,0,1,0],
    [0,1,1,1,1],
    [0,0,0,1,0],
]

# going right
# canvas[1][1] => canvas[1][2]

# going up
# canvas[1][1] => canvas[0][2]

floodFill(canvas, 1, 1, 2)

print(canvas)
# [0,0,0,0,0],
# [0,2,2,2,0],
# [0,2,2,2,0],
# [0,2,2,2,0],
# [0,0,0,0,0],
