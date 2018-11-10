class Person:

    def __init__(self):
        print('Person -- init')
        self.age = 100

    def __del__(self):  # 当对象被删除时自动调用,一般由于释放被对象删除的资源
        print('Person -- del')


p = Person()
p1 = p
p2 = p
print(p.age)
print(p.age)

del p1
print('删除了p1...')

del p2
print('删除了p2...')

del p

print('over...')
