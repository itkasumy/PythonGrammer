class Test1(object):

    def eat(self):
        print('吃东西...')


class Test2(Test1):

    def eat(self):
        print('吃土...')


class Test3(Test1):

    # def eat(self):
    #     print('吃草...')
    pass


def myEat(tmp):
    tmp.eat()


a = Test1()
myEat(a)

b = Test2()
myEat(b)

c = Test3()
myEat(c)
