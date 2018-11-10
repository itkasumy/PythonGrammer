class Animal(object):

    def __init__(self):
        self.age = 100

    def eat(self):
        print('我能吃东西')

    def drink(self):
        print('我能喝饮料')


class Cat(Animal):

    def __init__(self):
        self.name = '小白'
        # 方式1
        # Animal.__init__(self)
        # 方式2
        # super().__init__()
        # 方式3
        super(Cat, self).__init__()

    def eat(self):
        print('我只吃鱼...')

    def catch(self):
        print('我能捉老鼠')


tom = Cat()
print(tom.name)
print(tom.age)
