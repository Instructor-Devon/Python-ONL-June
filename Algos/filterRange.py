def filterRange(arr, minz, maxz):
    ''' filters out nums < min and > max '''

    # move target nums to end, pop them

    # loop it, look for target nums
    eIdx = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < minz or arr[i] > maxz:
            temp = arr[i]
            arr[i] = arr[eIdx]
            arr[eIdx] = temp

            eIdx -= 1
    
    # pop len(arr) - eIdx times
    killz = len(arr) - 1 - eIdx
    while killz > 0:
        arr.pop()
        killz -= 1
    

    # end: 0
    #  i
testArr = [2,4,6,8,10,12]
filterRange(testArr, 6, 8)
print(testArr)