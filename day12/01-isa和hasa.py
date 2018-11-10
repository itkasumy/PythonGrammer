class Cat(object):

    def eat(self):
        print('吃东西')


class BoSiMao(Cat):

    def __init__(self):
        self.nose = ''


class Nose(object):

    def smell(self):
        print('闻味道')


mao = BoSiMao()
mao.eat()
