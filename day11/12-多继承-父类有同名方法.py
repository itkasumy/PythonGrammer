class A(object):
    '马'
    def run(self):
        print('跑得快')

    def eat(self):
        print('我喜欢吃草')


class B(object):
    '驴'
    def walk(self):
        print('走得远')

    def eat(self):
        print('我喜欢吃嫩草')


class C(A, B):
    '骡子'
    pass


luozi = C()
luozi.eat()
print(C.__mro__)
