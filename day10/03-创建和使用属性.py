class Cat:

    def eat(self):
        print('吃一条鱼')

    def drink(self):
        print('喝了一口水')


mimi = Cat()    # 创建对象
mimi.name = '咪咪'
mimi.color = '白色'
print(mimi.name, mimi.color)

tom = Cat()
tom.name = '汤姆'
tom.color = '黑色'
print(tom.name, tom.color)

print(mimi.name, mimi.color)
