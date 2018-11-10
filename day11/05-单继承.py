class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print('我能吃东西')

    def drink(self):
        print('我能喝饮料')


class Cat(Animal):

    def catch(self):
        print('我能捉老鼠')


tom = Cat()
tom.catch()
tom.eat()
tom.drink()
print(tom.age)

dw = Animal()
dw.eat()
dw.drink()
