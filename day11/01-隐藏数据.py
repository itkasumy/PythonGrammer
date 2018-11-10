class Person:

    def __init__(self):
        self.age = 100

    def setAge(self, age):
        if age > 0:
            self.age = age
        else:
            print('错误的年龄，不能设置')

    def getAge(self):
        return self.age


p = Person()
p.setAge(10)
print(p.getAge())
