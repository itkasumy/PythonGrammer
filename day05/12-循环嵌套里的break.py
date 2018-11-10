i = 0

while i < 10:
    j = 0
    while j < 10:
        print("j = %d   " % j, end="")
        j += 1
        if j == 7:
            break

    print("i = %d" % i)
    i += 1

print("over...")
