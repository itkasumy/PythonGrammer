def test1():
    x = 1 / 0
    print('test1执行了')


def test2():
    try:
        test1()
    except:
        print('捕获到了异常')
        raise

    print('test2执行了')


def test3():
    test2()
    print('test3执行了')

test3()
print('over...')
