class Cat:

    def eat(self):
        print('吃一条鱼')

    def drink(self):
        print('喝了一口水')

    def talk(self):
        print('hello, 我是:%s' % self.name)


mimi = Cat()    # 创建对象
mimi.name = '咪咪'
mimi.talk()


tom = Cat()
tom.name = '汤姆'
tom.talk()
