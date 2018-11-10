class Test(object):

    num = 0

    def eat(self):
        print('吃土...')

    @classmethod
    def leiFangFa(cls):
        print(cls)
        print(Test.num)
        print(cls.num)


t = Test()
print(t)
# t.eat()
t.leiFangFa()
