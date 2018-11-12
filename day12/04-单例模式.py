class Cat(object):

    instance = None

    def __init__(self, name):
        self.name = name
        print('__init__', self)

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = object.__new__(cls)

        return cls.instance

    def setName(self, name):
        self.name = name


cat = Cat('小白')
print("创建了对象 %s" % cat)

cat2 = Cat('小黑')
print("创建了对象 %s" % cat2)

print(cat.name)
