class Animal(object):

    def __init__(self):
        self.age = 1

    def eat(self):
        print('我能吃东西')

    def drink(self):
        print('我能喝饮料')


class Cat(Animal):

    def catch(self):
        print('我能捉老鼠')


class BoSiMao(Cat):

    def play(self):
        print('我能唱歌')


tom = Cat()
tom.catch()
tom.eat()
tom.drink()
print(tom.age)
print('=' * 30)

dw = Animal()
dw.eat()
dw.drink()
print('=' * 30)

bsm = BoSiMao()
bsm.catch()
bsm.eat()
bsm.drink()
print(bsm.age)
bsm.play()
