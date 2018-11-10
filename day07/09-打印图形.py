def prtLine():
    print('<>' * 60)


def prtNumLine(num):
    i = 0
    while i < num:
        prtLine()
        i += 1


prtNumLine(10)
