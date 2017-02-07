def prime(x):
if x >= 2:
    for n in range(2, x, 1):
        if (x % n == 0):
            return False
            break
    else:
        return True
else:
    return False