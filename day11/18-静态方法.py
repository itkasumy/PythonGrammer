class Test(object):

    num = 0

    def eat(self):
        print('吃土...')

    @classmethod
    def leiFangFa(cls):
        print(cls)
        print(Test.num)
        print(cls.num)

    @staticmethod
    def add(a, b):
        return a + b


t = Test()
print(t)

res = t.add(10, 20)
print(res)
