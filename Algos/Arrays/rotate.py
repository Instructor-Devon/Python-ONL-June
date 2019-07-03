
def rotate(arr, shiftBy):
    ''' arr: any old list; shiftBy: number of rotations '''

    # arr: [4,6,6,8], shiftBy: 1 => [4,6,8,2]

    # EDGE CASE: shiftBy > len(arr) | we can use % yay
    shifty = shiftBy % len(arr)

    while shifty > 0:
        firstEl = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
        arr[len(arr) - 1] = firstEl
        shifty -= 1

testArr = [2,4,6,8]
rotate(testArr, 3)
print(testArr)