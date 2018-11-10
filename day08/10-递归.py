def getJ(n):
    if n == 1:
        return 1

    return n * getJ(n - 1)


print(getJ(5))
