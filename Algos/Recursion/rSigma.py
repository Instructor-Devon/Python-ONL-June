def rSigma(num):

    # base case!
    if num <= 1:
        return num

    return rSigma(num - 1) + num

def rFactorial(num):
    # num * num-1 => num == 1


    # !0 == 1 (says mathamaticians)
    if num <= 1:
        return 1

    # num 1 => return num
    return num * rFactorial(num - 1)
