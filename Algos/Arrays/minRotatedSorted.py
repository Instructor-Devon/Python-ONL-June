def min_sorted_rotated(arr, start = 0, end=None):
    # start = 0
    if end == None:
        end = len(arr) - 1
    while start < end:
        mid = int((start + end)/2)

        if arr[start] == arr[end]:
            return min_sorted_rotated(arr, start+1, end-1)
        
        #check if mid is the one
        if arr[mid-1] > arr[mid]:
            return arr[mid]

        # look left
        if arr[mid] < arr[start]:
            end = mid - 1
        # look right
        elif arr[mid] > arr[end]:
            start = mid + 1
        else:
            return arr[0]
    return arr[end]

test0 = [2,3,4,5,1]
test1 = [5,1,2,3,4]
test2 = [4,5,1,2,3]
test3 = [3,3,3,1,2]
test4 = [2,2,2,2,2,1,2]
print(min_sorted_rotated(test0))
print(min_sorted_rotated(test1))
print(min_sorted_rotated(test2))
print(min_sorted_rotated(test3))
print(min_sorted_rotated(test4))
