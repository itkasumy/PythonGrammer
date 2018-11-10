class A(object):
    '马'
    def run(self):
        print('跑得快')


class B(object):
    '驴'
    def walk(self):
        print('走得远')


class C(A, B):
    '骡子'
    pass


luozi = C()
luozi.run()
luozi.walk()

