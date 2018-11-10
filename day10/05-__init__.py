class Cat:

    def __init__(self):
        print('init')
        self.name = '咪咪'

    def eat(self):
        print('吃一条鱼')

    def drink(self):
        print('喝了一口水')

    def talk(self):
        print('hello, 我是:%s' % self.name)


mimi = Cat()
mimi.talk()
