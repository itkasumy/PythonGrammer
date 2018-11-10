class Animal(object):

    def __init__(self, age):
        self.age = age
        self.name = '小黑'


class Cat(Animal):

    def __init__(self, name, age):
        self.name = name
        super(Cat, self).__init__(age)


tom = Cat('小白', 10)
print(tom.name)
print(tom.age)
