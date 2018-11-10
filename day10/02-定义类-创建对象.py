class Cat:

    def eat(self):
        print('吃一条鱼')

    def drink(self):
        print('喝了一口水')


mimi = Cat()    # 创建对象
mimi.eat()  # 调用方法时，不需要为self传值
mimi.drink()

tom = Cat()
tom.eat()
tom.drink()
