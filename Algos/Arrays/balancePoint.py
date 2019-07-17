def balance_point(arr):
    # [5,10,15] True
    # [243,2,53,2] False

    # [sum1][    sum41   ]
    
    sum1 = arr[0]
    sum41 = 0 # loop rest of array to find sum of elements
    for i in range(1,len(arr)):
        sum41 += arr[i]

    # check if sum1 == sum41
    if sum1 == sum41:
        return True

    for k in range(1, len(arr)):
        print("looping")
        # grab value from sum41
        sum1 += arr[k]
        sum41 -= arr[k]
        # give to sum1
        if sum1 == sum41:
            return True
        if sum1 > sum41:
            return False

    return False

test = [10,5,-2,-2,-2,-2,-2,5,20]
print(balance_point(test))
