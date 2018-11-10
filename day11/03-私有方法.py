class Person:

    def __init__(self):
        self.__age = 100

    def setAge(self, age):
        if age > 0:
            self.__age = age
            self.__myPrt('正确的年龄，已经设置')
            # print('Person类说: 正确的年龄，已经设置')

        else:
            self.__myPrt('错误的年龄，不能设置')
            # print('Person类说: 错误的年龄，不能设置')

    def getAge(self):
        return self.__age

    def __myPrt(self, content):
        print('Person类说: ' + content)


p = Person()
p.setAge(10)
p.setAge(-10)
# p.myPrt('哈哈哈哈')
# print(dir(p))
