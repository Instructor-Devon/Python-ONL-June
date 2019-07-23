def sigma(num):

    # num = 5 
        # -> 5 + 4 + 3 + 2 + 1

    summy = 0
    while num > 0:
        summy += num
        num -= 1

    return summy

