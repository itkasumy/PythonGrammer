class Animal(object):

    def __init__(self):
        self.__age = 100

    def eat(self):
        print('我能吃东西')

    def drink(self):
        print('我能喝饮料')

    def getAge(self):
        return self.__age


class Cat(Animal):

    def __init__(self):
        self.name = '小白'
        super(Cat, self).__init__()

    def eat(self):
        print('我只吃鱼...')
        # print('我的年龄是: %d' % self.getAge())
        print('我的年龄是: %d' % self._Animal__age)

    def catch(self):
        print('我能捉老鼠')


tom = Cat()
print(tom.name)
tom.eat()
