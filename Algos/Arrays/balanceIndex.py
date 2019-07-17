def balance_index(arr):

    if len(arr) == 0:
        return False
    if len(arr) == 1:
        return 0

    # [2,2,5,2,2] => 2 (balanced at index 2)
    # [23,4,5] => False
    # [10,15,7,25] => 2

    # remember to not include pivot point in sums

    sum1 = arr[0]
    sum41 = 0 # loop rest of array to find sum of elements
    for i in range(1,len(arr)):
        sum41 += arr[i]

    for k in range(1,len(arr)-1):
        temp = arr[k]

        # subtract arr[k] from sum41
        sum41 -= temp

        # compare, return k if True
        if sum1 == sum41:
            return k

        # if False, add arr[k] to sum1
        sum1 += temp

    return False
        
test = [0,0,0]
print(balance_index(test))
