def test01():
    global a
    a = 200
    print(a)


def test02():
    print(a)


a = 10
test01()
# a = 20
test02()
