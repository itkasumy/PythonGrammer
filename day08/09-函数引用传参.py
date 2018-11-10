def modifyNum(a):
    print('1------', a)
    a = 200
    print('2------', a)


def modifyLs(a):
    print('1------', a)
    a[0] = 22
    print('2------', a)


num = 100
modifyNum(num)
print('3------', num)

ls = [11]
modifyLs(ls)
print('3------', ls)
