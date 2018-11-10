class Test1(object):

    num = 0

    def __init__(self):
        Test1.num += 1


t1 = Test1()

t2 = Test1()

print('创建了 %d 个对象' % t2.num)
