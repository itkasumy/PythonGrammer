class Person:

    def __init__(self):
        self.__age = 100

    def setAge(self, age):
        if age > 0:
            self.__age = age
        else:
            print('错误的年龄，不能设置')

    def getAge(self):
        return self.__age


p = Person()
p.setAge(10)
print(p.getAge())
# print(p.__age)
print(dir(p))
"""
['_Person__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'getAge', 'setAge']
"""
print(p._Person__age)
