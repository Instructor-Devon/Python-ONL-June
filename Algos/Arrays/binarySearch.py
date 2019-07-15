def arrayContains(arr, value):
    # return True/False if value is contained int the array/list

    # loop through array, comparing each element

    for thing in arr:
        if value == thing:
            return True


    return False


def binarySearch(sortedArr, value):

    #  s   m   e
    # [2,4,6,8,10]
    start = 0
    end = len(sortedArr) - 1

    while True:

        middle = int((start + end)/2)
        # find the middle

        if sortedArr[middle] == value:
            return True

        elif sortedArr[middle] < value:
            start = middle + 1
           

        elif sortedArr[middle] > value:
            end = middle - 1

        if start > end:
            break

    return False





print(binarySearch([0,2,4,6,8,10],2))
    
