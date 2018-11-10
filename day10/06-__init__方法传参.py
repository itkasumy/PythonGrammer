class Cat:

    def __init__(self, newName):
        print('init')
        self.name = newName

    def eat(self):
        print('吃一条鱼')

    def drink(self):
        print('喝了一口水')

    def talk(self):
        print('hello, 我是:%s' % self.name)


mimi = Cat('咪咪')
mimi.talk()
