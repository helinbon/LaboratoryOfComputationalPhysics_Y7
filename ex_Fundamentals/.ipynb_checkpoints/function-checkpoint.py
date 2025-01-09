def summation(x):
    if x <= 0:
        return 0
    else:
        y = 0
        while x > 0:
            y += x
            x -= 1
        return y
################
